"""
完整的RAG流程管道
功能：整合Markdown处理、知识图谱构建和RAG系统
"""

from typing import List, Dict, Any
from pathlib import Path
import logging
import networkx as nx

# 配置文件
try:
    from config import LLM_CONFIG
except ImportError:
    LLM_CONFIG = {}

from knowledge_graph import KnowledgeGraphBuilder
from rag_system import RAGSystem

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class CompleteRAGPipeline:
    """完整的RAG流程管道"""
    
    def __init__(self, use_openai: bool = False, api_key: str = None, 
                 use_vllm: bool = True, vllm_base_url: str = None, vllm_model_name: str = None):
        """
        初始化完整流程
        
        Args:
            use_openai: 是否使用OpenAI模型
            api_key: OpenAI API密钥
            use_vllm: 是否使用vLLM（默认True）
            vllm_base_url: vLLM服务地址（如 "http://127.0.0.1:8910/v1"）
            vllm_model_name: vLLM模型名称（如果为None，将从服务获取）
        """
        self.kg_builder = KnowledgeGraphBuilder()
        
        # 确定使用哪个LLM
        if use_openai:
            llm_model = "openai"
        elif use_vllm:
            llm_model = "vllm"
        else:
            llm_model = "local"
        
        # 从配置文件读取vLLM配置
        if use_vllm and not vllm_base_url:
            try:
                if LLM_CONFIG.get("provider") == "vllm" and "vllm" in LLM_CONFIG:
                    vllm_config = LLM_CONFIG["vllm"]
                    vllm_base_url = vllm_base_url or vllm_config.get("base_url", "http://127.0.0.1:8910/v1")
                    vllm_model_name = vllm_model_name or vllm_config.get("model")
                    api_key = api_key or vllm_config.get("api_key", "EMPTY")
            except:
                pass
        
        self.rag_system = RAGSystem(
            embedding_model="openai" if use_openai else "local",
            llm_model=llm_model,
            api_key=api_key,
            vllm_base_url=vllm_base_url,
            vllm_model_name=vllm_model_name
        )
        
        self.markdown_contents = {}
        self.knowledge_graph = None
    
    def _expand_markdown_inputs(self, markdown_inputs: List[str]) -> List[str]:
        """支持传入文件与目录，自动展开为Markdown文件列表"""
        collected = []
        for item in markdown_inputs:
            path = Path(item).expanduser()
            if path.is_dir():
                dir_mds = sorted(path.rglob("*.md"))
                if not dir_mds:
                    logger.warning(f"目录中未找到Markdown文件: {path}")
                collected.extend(dir_mds)
            elif path.is_file() and path.suffix.lower() in [".md", ".markdown"]:
                collected.append(path)
            else:
                logger.warning(f"无效的Markdown输入: {path}")
        unique_paths = []
        seen = set()
        for md_path in collected:
            resolved = str(md_path.resolve())
            if resolved not in seen:
                seen.add(resolved)
                unique_paths.append(resolved)
        return unique_paths
    
    def _load_markdown_files(self, markdown_paths: List[str]) -> Dict[str, str]:
        """
        从文件路径加载Markdown内容
        
        Args:
            markdown_paths: Markdown文件路径列表
            
        Returns:
            Dict[str, str]: 键为文件路径，值为Markdown内容
        """
        markdown_contents = {}
        for md_path in markdown_paths:
            try:
                path_obj = Path(md_path)
                if not path_obj.exists():
                    logger.warning(f"Markdown文件不存在: {md_path}")
                    continue
                
                with open(path_obj, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                markdown_contents[str(path_obj.resolve())] = content
                logger.info(f"已加载Markdown文件: {md_path}")
            except Exception as e:
                logger.error(f"加载Markdown文件失败 {md_path}: {e}")
                markdown_contents[md_path] = None
        
        return markdown_contents
    
    def _process_markdown_contents(self, markdown_contents: Dict[str, str]):
        """
        处理Markdown内容的通用流程（构建知识图谱和RAG系统）
        
        Args:
            markdown_contents: Dict[str, str]，键为文档标识（路径），值为Markdown内容
        """
        # 过滤掉None值
        valid_contents = {k: v for k, v in markdown_contents.items() if v is not None}
        if not valid_contents:
            raise ValueError("没有有效的Markdown内容可处理")
        
        self.markdown_contents = valid_contents
        
        # Step 1: 构建知识图谱
        logger.info("Step 1: 构建知识图谱...")
        self.knowledge_graph = self.kg_builder.build_graph_from_documents(self.markdown_contents)
        self.kg_builder.visualize_graph("knowledge_graph.html")
        
        # Step 2: 创建RAG系统
        logger.info("Step 2: 设置RAG系统...")
        self.rag_system.load_and_process_documents(self.markdown_contents)
        self.rag_system.create_vector_store()
        self.rag_system.setup_qa_chain()
        self.rag_system.integrate_knowledge_graph(self.knowledge_graph)
        
        logger.info("=== RAG流程完成 ===")

    def run_from_markdown(self, markdown_inputs: List[str] = None, markdown_contents: Dict[str, str] = None):
        """
        从Markdown文件或内容直接开始处理流程
        
        可以接受两种输入方式：
        1. markdown_inputs: Markdown文件路径列表（可以是文件或目录）
        2. markdown_contents: 直接提供Markdown内容字典（键为文档标识，值为内容）
        
        如果两者都提供，markdown_contents优先。
        
        Args:
            markdown_inputs: Markdown文件路径列表（可选）
            markdown_contents: Markdown内容字典（可选）
        """
        logger.info("=== 开始RAG流程（从Markdown开始） ===")
        
        if markdown_contents is not None:
            # 直接使用提供的Markdown内容
            logger.info("使用提供的Markdown内容...")
            self._process_markdown_contents(markdown_contents)
        elif markdown_inputs is not None:
            # 从文件加载Markdown内容
            expanded_paths = self._expand_markdown_inputs(markdown_inputs)
            if not expanded_paths:
                raise ValueError("未找到可处理的Markdown文件，请检查输入路径")
            
            logger.info(f"从 {len(expanded_paths)} 个Markdown文件加载内容...")
            markdown_contents = self._load_markdown_files(expanded_paths)
            self._process_markdown_contents(markdown_contents)
        else:
            raise ValueError("必须提供 markdown_inputs 或 markdown_contents 参数之一")
    
    def prepare_from_existing_vectorstore(self, persist_directory: str = "./vectorstore"):
        """
        直接加载已有的向量数据库并准备问答链
        """
        logger.info("=== 使用已有向量库进行检索 ===")
        self.rag_system.load_vector_store(persist_directory=persist_directory)
        self.rag_system.setup_qa_chain()
    
    def answer_question(self, question: str) -> Dict[str, Any]:
        """回答问题"""
        return self.rag_system.query(question)
    
    def interactive_qa(self):
        """交互式问答会话"""
        print("\n" + "="*50)
        print("RAG问答系统已启动")
        print("输入 'exit' 或 'quit' 退出")
        print("输入 'graph' 查看知识图谱统计")
        print("="*50 + "\n")
        
        while True:
            question = input("\n请输入您的问题: ").strip()
            
            if question.lower() in ['exit', 'quit']:
                print("感谢使用，再见！")
                break
            
            if question.lower() == 'graph':
                if self.knowledge_graph:
                    print(f"\n知识图谱统计:")
                    print(f"- 节点数: {len(self.knowledge_graph.nodes)}")
                    print(f"- 边数: {len(self.knowledge_graph.edges)}")
                    print(f"- 连通分量数: {nx.number_weakly_connected_components(self.knowledge_graph)}")
                else:
                    print("知识图谱未构建")
                continue
            
            if not question:
                continue
            
            # 获取答案
            result = self.answer_question(question)
            
            print("\n" + "="*50)
            print(f"问题: {result['question']}")
            print("-"*50)
            print(f"答案: {result['answer']}")
            
            if result.get('graph_context') and result['graph_context']['entities']:
                print(f"\n相关实体: {', '.join(result['graph_context']['entities'][:5])}")
            
            if result.get('source_documents'):
                print(f"\n参考来源 ({len(result['source_documents'])} 个文档片段):")
                for i, doc in enumerate(result['source_documents'][:2], 1):
                    source = doc.metadata.get('source', 'Unknown')
                    print(f"  {i}. {source}")
            
            print("="*50)

