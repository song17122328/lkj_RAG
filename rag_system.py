"""
RAG检索生成系统
功能：文档向量化、检索和问答生成
"""

import os
import shutil
from typing import List, Dict, Any
import logging
import networkx as nx
import requests

# 配置文件
try:
    from config import LLM_CONFIG, RETRIEVAL, PROMPTS, ADVANCED_FEATURES
except ImportError:
    LLM_CONFIG = {}
    RETRIEVAL = {"k": 5}
    PROMPTS = {}
    ADVANCED_FEATURES = {}

# LangChain核心组件
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document, BaseRetriever

# LLM模型
# 兼容新旧版本的langchain导入
try:
    from langchain_community.chat_models import ChatOpenAI
    from langchain_community.chat_models import ChatOllama
except ImportError:
    # 旧版本langchain
    from langchain.chat_models import ChatOpenAI
    try:
        from langchain_community.chat_models import ChatOllama
    except ImportError:
        ChatOllama = None

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class RAGSystem:
    """RAG检索生成系统"""
    
    def __init__(self, 
                 embedding_model: str = "local",
                 llm_model: str = "openai",
                 api_key: str = None,
                 vllm_base_url: str = None,
                 vllm_model_name: str = None):
        """
        初始化RAG系统
        
        Args:
            embedding_model: 嵌入模型选择 ("local" 或 "openai")
            llm_model: LLM模型选择 ("openai", "vllm", "ollama", "local")
            api_key: API密钥
            vllm_base_url: vLLM服务地址（如 "http://127.0.0.1:8910/v1"）
            vllm_model_name: vLLM模型名称（如果为None，将从服务获取）
        """
        self.documents = []
        self.vectorstore = None
        self.qa_chain = None
        self.knowledge_graph = None
        
        # 初始化嵌入模型
        if embedding_model == "local":
            # 使用本地嵌入模型
            self.embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
        else:
            # 使用OpenAI嵌入
            if not api_key:
                raise ValueError("使用OpenAI模型需要提供API密钥")
            os.environ["OPENAI_API_KEY"] = api_key
            self.embeddings = OpenAIEmbeddings()
        
        # 初始化LLM
        if llm_model == "openai" and api_key:
            # 从配置文件读取OpenAI配置
            try:
                openai_config = LLM_CONFIG.get("openai", {})
                openai_model = openai_config.get("model", LLM_CONFIG.get("model_name", "gpt-3.5-turbo"))
                openai_temperature = openai_config.get("temperature", LLM_CONFIG.get("temperature", 0.0))
                openai_max_tokens = openai_config.get("max_tokens", LLM_CONFIG.get("max_tokens", 2000))
            except:
                openai_model = "gpt-3.5-turbo"
                openai_temperature = 0.0
                openai_max_tokens = 2000
            
            self.llm = ChatOpenAI(
                temperature=openai_temperature,
                model=openai_model,
                api_key=api_key,
                max_tokens=openai_max_tokens
            )
            logger.info(f"已配置OpenAI，模型: {openai_model}, temperature: {openai_temperature}, max_tokens: {openai_max_tokens}")
        elif llm_model == "vllm":
            # 使用vLLM（OpenAI兼容API）
            # 从配置文件读取vLLM配置
            try:
                vllm_config = LLM_CONFIG.get("vllm", {})
                base_url = vllm_base_url or vllm_config.get("base_url", "http://127.0.0.1:8910/v1")
                model_name = vllm_model_name or vllm_config.get("model") or LLM_CONFIG.get("model_name", "gpt-3.5-turbo")
                vllm_api_key = api_key or vllm_config.get("api_key", "EMPTY")
                max_tokens = vllm_config.get("max_tokens", LLM_CONFIG.get("max_tokens", 2048))
                temperature = vllm_config.get("temperature", LLM_CONFIG.get("temperature", 0.0))
            except:
                # 如果无法导入配置，使用默认值
                base_url = vllm_base_url or "http://127.0.0.1:8910/v1"
                model_name = vllm_model_name or "gpt-3.5-turbo"
                vllm_api_key = api_key or "EMPTY"
                max_tokens = 2048
                temperature = 0.0
            
            # 如果没有提供模型名称，尝试从服务获取
            if not vllm_model_name:
                try:
                    response = requests.get(f"{base_url}/models", timeout=5)
                    if response.status_code == 200:
                        models = response.json()
                        if models.get("data") and len(models["data"]) > 0:
                            model_name = models["data"][0]["id"]
                            logger.info(f"从vLLM服务获取到模型: {model_name}")
                except Exception as e:
                    logger.warning(f"无法从vLLM服务获取模型列表，使用配置的模型名称: {e}")
            
            # 使用参考项目的参数格式
            self.llm = ChatOpenAI(
                api_key=vllm_api_key,
                base_url=base_url,
                model=model_name,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            logger.info(f"已配置vLLM，服务地址: {base_url}, 模型: {model_name}, max_tokens: {max_tokens}, temperature: {temperature}")
        elif llm_model == "ollama":
            # 使用Ollama
            if ChatOllama is None:
                logger.error("请安装langchain-community以使用Ollama: pip install langchain-community")
                self.llm = None
            else:
                # 从配置文件读取Ollama配置
                try:
                    ollama_config = LLM_CONFIG.get("ollama", {})
                    ollama_base_url = os.getenv("OLLAMA_BASE_URL", ollama_config.get("base_url", "http://127.0.0.1:11434"))
                    ollama_model = os.getenv("OLLAMA_MODEL", ollama_config.get("model", "llama3"))
                    streaming = ollama_config.get("streaming", False)
                except:
                    # 如果无法导入配置，使用默认值
                    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
                    ollama_model = os.getenv("OLLAMA_MODEL", "llama3")
                    streaming = False
                
                self.llm = ChatOllama(
                    model=ollama_model,
                    base_url=ollama_base_url,
                    streaming=streaming
                )
                logger.info(f"已配置Ollama，服务地址: {ollama_base_url}, 模型: {ollama_model}, streaming: {streaming}")
        else:
            # 可以替换为本地模型，如LLaMA、ChatGLM等
            logger.warning("未配置LLM，将使用模拟响应")
            self.llm = None
        
        # 初始化文本分割器
        # 结构感知的Markdown分割器 - 保留章节标题作为元数据
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
            ("####", "Header 4"),
        ]
        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on,
            strip_headers=False  # 保留标题在内容中
        )

        # 通用字符分割器（用于进一步切分大块）
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""]
        )
    
    def load_and_process_documents(self, markdown_contents: Dict[str, str]):
        """加载并处理Markdown文档（结构感知切分 + 表格提取 + 数值/地理增强）"""
        logger.info("加载文档到RAG系统（使用Markdown结构感知切分 + 表格提取 + 数值/地理增强）...")

        # 导入增强模块
        try:
            from table_extractor import TableExtractor
            from numerical_enricher import NumericalDataEnricher
            from geographical_tagger import GeographicalTagger

            table_extractor = TableExtractor()
            numerical_enricher = NumericalDataEnricher()
            geographical_tagger = GeographicalTagger()

            use_enhancement = True
            logger.info("启用表格提取、数值增强和地理标注功能")
        except ImportError as e:
            logger.warning(f"增强模块导入失败: {e}，将使用标准处理流程")
            use_enhancement = False

        for doc_name, content in markdown_contents.items():
            if not content:
                continue

            # === 阶段1: 表格提取（如果启用） ===
            table_documents = []
            if use_enhancement:
                try:
                    # 提取所有表格为独立的Documents
                    table_documents = table_extractor.extract_tables_from_markdown(content, doc_name)
                    logger.debug(f"{doc_name}: 提取了 {len(table_documents)} 个表格")
                except Exception as e:
                    logger.warning(f"表格提取失败({doc_name}): {e}")
                    table_documents = []

            # === 阶段2: 文本分割（Markdown结构感知） ===
            try:
                md_header_splits = self.markdown_splitter.split_text(content)

                # 为每个分割添加source元数据
                for split in md_header_splits:
                    split.metadata["source"] = doc_name

                # 步骤3: 对于仍然较大的chunk，使用RecursiveCharacterTextSplitter进一步分割
                # 这确保了每个chunk不会超过chunk_size，同时保留了header元数据
                final_chunks = []
                for md_doc in md_header_splits:
                    # 如果chunk大小超过限制，进一步分割
                    if len(md_doc.page_content) > 1000:
                        sub_chunks = self.text_splitter.split_documents([md_doc])
                        # 保留原有的header元数据
                        for chunk in sub_chunks:
                            chunk.metadata.update(md_doc.metadata)
                        final_chunks.extend(sub_chunks)
                    else:
                        final_chunks.append(md_doc)

                logger.debug(f"{doc_name}: {len(md_header_splits)}个章节 -> {len(final_chunks)}个chunks")

            except Exception as e:
                # 如果Markdown分割失败，降级到普通字符分割
                logger.warning(f"Markdown结构分割失败({doc_name}): {e}，降级到字符分割")
                doc = Document(
                    page_content=content,
                    metadata={"source": doc_name}
                )
                final_chunks = self.text_splitter.split_documents([doc])

            # === 阶段4: 数值和地理信息增强（如果启用） ===
            if use_enhancement:
                enhanced_chunks = []
                for chunk in final_chunks:
                    try:
                        # 数值增强
                        enriched_text, enriched_metadata = numerical_enricher.enrich_text(
                            chunk.page_content,
                            chunk.metadata
                        )

                        # 地理标注
                        enriched_metadata = geographical_tagger.extract_geographical_info(
                            chunk.page_content,
                            enriched_metadata
                        )

                        # 创建增强后的Document
                        enhanced_chunk = Document(
                            page_content=enriched_text,
                            metadata=enriched_metadata
                        )
                        enhanced_chunks.append(enhanced_chunk)

                    except Exception as e:
                        logger.warning(f"增强失败: {e}，保留原chunk")
                        enhanced_chunks.append(chunk)

                final_chunks = enhanced_chunks

            # === 阶段5: 合并所有chunks（文本 + 表格） ===
            self.documents.extend(final_chunks)
            self.documents.extend(table_documents)

            total_chunks = len(final_chunks) + len(table_documents)
            logger.debug(f"{doc_name}: 总计 {total_chunks} chunks (文本={len(final_chunks)}, 表格={len(table_documents)})")

        logger.info(f"文档处理完成，共 {len(self.documents)} 个chunks（含章节结构元数据、表格、数值和地理标注）")
    
    def create_vector_store(self, persist_directory: str = "./vectorstore"):
        """创建向量存储"""
        logger.info("创建向量存储...")
        
        # 如果目录已存在，先清空以确保重新构建
        if os.path.exists(persist_directory):
            logger.info(f"检测到已有向量存储目录，正在清空: {persist_directory}")
            try:
                shutil.rmtree(persist_directory)
            except Exception as e:
                logger.error(f"清空旧向量存储目录失败: {e}")
                raise

        # 使用Chroma作为向量数据库（支持持久化）
        self.vectorstore = Chroma.from_documents(
            documents=self.documents,
            embedding=self.embeddings,
            persist_directory=persist_directory
        )
        
        # 持久化
        self.vectorstore.persist()
        logger.info(f"向量存储已创建并持久化到: {persist_directory}")
    
    def load_vector_store(self, persist_directory: str = "./vectorstore"):
        """加载已有向量存储"""
        if not os.path.exists(persist_directory):
            raise ValueError(f"向量存储目录不存在: {persist_directory}")
        
        logger.info(f"加载已有向量存储: {persist_directory}")
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embeddings
        )
        logger.info("向量存储加载完成")
    
    def setup_qa_chain(self):
        """设置问答链"""
        if not self.vectorstore:
            raise ValueError("请先创建向量存储")

        # 从配置获取检索参数
        search_type = RETRIEVAL.get("search_type", "similarity")
        k = RETRIEVAL.get("k", 5)

        # 检查是否启用高级检索
        use_advanced = ADVANCED_FEATURES.get("hybrid_search", False) or ADVANCED_FEATURES.get("reranking", False)

        if use_advanced:
            # 使用统一检索入口
            try:
                from retrieval import Retriever

                retriever_instance = Retriever(
                    vectorstore=self.vectorstore,
                    documents=self.documents,
                    k=k,
                    llm=self.llm  # 传入LLM用于智能文件名提取
                )
                logger.info("使用定制检索器（带去重和多样性约束）")

                # 创建自定义检索器包装（兼容 Pydantic v2）
                class CustomRetriever(BaseRetriever):
                    retriever_instance: Any  # 使用类型注解定义字段
                    k: int

                    class Config:
                        arbitrary_types_allowed = True

                    def get_relevant_documents(self, query: str) -> List[Document]:
                        return self.retriever_instance.retrieve(query, k=self.k)

                    async def aget_relevant_documents(self, query: str) -> List[Document]:
                        # 异步版本（如果需要）
                        return self.get_relevant_documents(query)

                retriever = CustomRetriever(retriever_instance=retriever_instance, k=k)
                logger.info(f"已启用检索器 (k={k})")
            except Exception as e:
                logger.warning(f"高级检索器初始化失败，回退到向量库自带检索: {e}")
                retriever = self.vectorstore.as_retriever(
                    search_type=search_type,
                    search_kwargs={"k": k}
                )
        else:
            # 使用标准检索器
            retriever = self.vectorstore.as_retriever(
                search_type=search_type,
                search_kwargs={"k": k}
            )
            logger.info(f"使用标准检索器 (type={search_type}, k={k})")

        # 从配置获取提示模板
        prompt_template = PROMPTS.get("qa_template", """基于以下上下文回答问题。如果你不知道答案，请说"我不知道"，不要试图编造答案。

上下文信息:
{context}

问题: {question}

请提供详细且准确的回答:""")

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        if self.llm:
            # 创建问答链
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                chain_type_kwargs={"prompt": PROMPT},
                return_source_documents=True
            )
        else:
            # 创建简单的检索系统（无LLM）
            self.qa_chain = retriever

        logger.info("问答链设置完成")
    
    def integrate_knowledge_graph(self, knowledge_graph: nx.DiGraph):
        """集成知识图谱到RAG系统"""
        self.knowledge_graph = knowledge_graph
        logger.info("知识图谱已集成到RAG系统")
    
    def query(self, question: str) -> Dict[str, Any]:
        """
        执行查询

        Args:
            question: 用户问题

        Returns:
            包含答案和相关信息的字典
        """
        logger.info(f"处理问题: {question}")

        result = {
            "question": question,
            "answer": None,
            "source_documents": [],
            "graph_context": None
        }

        # 1. 从知识图谱获取相关信息
        if self.knowledge_graph:
            graph_context = self._get_graph_context(question)
            result["graph_context"] = graph_context

        # 2. 使用RAG检索相关文档
        if self.qa_chain:
            if self.llm:
                # 使用完整的问答链
                qa_result = self.qa_chain({"query": question})
                raw_answer = qa_result.get("result", "无法生成答案")
                # 清理答案，移除思考过程
                result["answer"] = self._clean_answer(raw_answer)
                result["source_documents"] = qa_result.get("source_documents", [])
            else:
                # 仅检索，不生成答案
                relevant_docs = self.qa_chain.get_relevant_documents(question)
                result["source_documents"] = relevant_docs

                # 简单的答案生成（基于检索结果）
                if relevant_docs:
                    result["answer"] = self._simple_answer_generation(question, relevant_docs)
                else:
                    result["answer"] = "未找到相关文档"

        return result
    
    def _get_graph_context(self, question: str) -> Dict[str, Any]:
        """从知识图谱获取相关上下文"""
        context = {
            "entities": [],
            "relations": [],
            "subgraph": None
        }
        
        # 简单的实体匹配
        question_lower = question.lower()
        relevant_nodes = []
        
        for node in self.knowledge_graph.nodes():
            if node.lower() in question_lower or question_lower in node.lower():
                relevant_nodes.append(node)
                context["entities"].append(node)
        
        # 获取相关的子图
        if relevant_nodes:
            # 获取相关节点的邻居
            subgraph_nodes = set(relevant_nodes)
            for node in relevant_nodes:
                neighbors = list(self.knowledge_graph.neighbors(node))[:5]
                subgraph_nodes.update(neighbors)
            
            # 提取子图
            context["subgraph"] = self.knowledge_graph.subgraph(subgraph_nodes)
            
            # 获取相关关系
            for edge in context["subgraph"].edges(data=True):
                relation_info = {
                    "subject": edge[0],
                    "object": edge[1],
                    "relation": edge[2].get("relation", "related_to")
                }
                context["relations"].append(relation_info)
        
        return context
    
    def _simple_answer_generation(self, question: str, documents: List[Document]) -> str:
        """简单的答案生成（不使用LLM）"""
        # 合并相关文档内容
        context = "\n\n".join([doc.page_content for doc in documents[:3]])

        # 返回相关内容摘要
        answer = f"根据检索到的文档，以下是相关信息：\n\n{context[:500]}..."

        if len(context) > 500:
            answer += f"\n\n（还有更多相关内容，共检索到 {len(documents)} 个相关文档段落）"

        return answer

    def _clean_answer(self, raw_answer: str) -> str:
        """
        清理LLM输出，移除思考过程和冗余内容

        策略：如果存在</think>标签，提取标签后的内容作为最终答案；
        否则使用正则清理思考过程标记

        Args:
            raw_answer: 原始LLM输出

        Returns:
            清理后的答案
        """
        import re

        # 策略1：如果存在</think>标签，提取标签后的内容
        if '</think>' in raw_answer.lower():
            # 查找最后一个</think>标签的位置（不区分大小写）
            # 使用正则找到所有</think>标签
            matches = list(re.finditer(r'</think>', raw_answer, flags=re.IGNORECASE))
            if matches:
                last_match = matches[-1]
                # 提取</think>之后的内容
                after_think = raw_answer[last_match.end():].strip()

                # 如果存在，跳过可能的换行符
                if after_think:
                    # 移除开头的多余空行
                    after_think = re.sub(r'^\s*\n+', '', after_think)

                    # 如果提取的内容足够长，使用它
                    if len(after_think) >= 10:
                        return after_think

        # 策略2：如果没有</think>标签或提取失败，使用原有清理逻辑
        cleaned = raw_answer

        # 尝试移除<think>...</think>标签及其内容
        cleaned = re.sub(r'<think>.*?</think>', '', cleaned, flags=re.DOTALL | re.IGNORECASE)

        # 移除常见的思考过程标记（中文和英文）
        thinking_patterns = [
            r'好的[，,].*?需要.*?[\n。]',
            r'让我.*?分析.*?[\n。]',
            r'首先[，,].*?[\n。]',
            r'根据.*?我.*?理解.*?[\n。]',
            r'我.*?认为.*?[\n。]',
            r'让我们.*?[\n。]',
            r'Ok[,，].*?need.*?[\n.]',
            r'Let me.*?[\n.]',
            r'First[,，].*?[\n.]',
        ]

        for pattern in thinking_patterns:
            # 只移除开头的思考过程
            cleaned = re.sub(r'^' + pattern, '', cleaned, flags=re.MULTILINE | re.IGNORECASE)

        # 移除多余的空行
        cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

        # 去除首尾空白
        cleaned = cleaned.strip()

        # 如果清理后为空，返回原始答案
        if not cleaned or len(cleaned) < 10:
            return raw_answer.strip()

        return cleaned

