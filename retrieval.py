"""
RAG 检索模块（唯一实现）

特性：
- 语义检索 + 关键词检索混合策略
- 基于内容的去重与多样性控制，减少重复段落
- 可选的简单重排序，提升相关性
"""

from typing import List, Dict, Optional, Any
from dataclasses import dataclass
import logging
import re
import math
import hashlib

try:
    from langchain.schema import Document
except ImportError:  # pragma: no cover - 环境缺少langchain时的兜底
    @dataclass
    class Document:
        page_content: str
        metadata: Optional[Dict[str, Any]] = None

# 配置文件
try:
    from config import ADVANCED_FEATURES
except ImportError:
    ADVANCED_FEATURES = {"hybrid_search": False, "reranking": False}

logger = logging.getLogger(__name__)


class Retriever:
    """支持混合搜索、去重和重排序的检索器"""

    def __init__(self, vectorstore,
                 documents: Optional[List[Document]] = None,
                 config: Optional[Dict] = None,
                 k: int = 10,
                 llm: Optional[Any] = None):
        """
        Args:
            vectorstore: 向量存储
            documents: 所有文档列表（可选，用于关键词搜索）
            config: 配置字典（可选，默认从 ADVANCED_FEATURES 读取）
            k: 默认返回的文档数量
            llm: 大语言模型实例（可选，用于智能文件名提取）
        """
        self.vectorstore = vectorstore
        self.documents = documents or []
        self.config = config if config is not None else ADVANCED_FEATURES
        self.k = k
        self.llm = llm  # 用于智能文件名提取

        # 检索策略配置
        self.use_hybrid = self.config.get("hybrid_search", False)
        self.hybrid_weight = self.config.get("hybrid_weight", 0.3)
        self.use_reranking = self.config.get("reranking", False)
        self.reranking_top_k = self.config.get("reranking_top_k", 20)

        # 去重和多样性参数
        self.similarity_threshold = 0.9  # 内容相似度阈值
        self.diversity_threshold = 0.3   # 多样性阈值

        logger.info(f"检索器初始化: hybrid={self.use_hybrid}, "
                    f"reranking={self.use_reranking}, k={k}, llm={'可用' if llm else '不可用'}")

    def retrieve(self, query: str, k: Optional[int] = None) -> List[Document]:
        """执行检索并返回文档列表"""
        if k is None:
            k = self.k

        retrieve_k = self.reranking_top_k if self.use_reranking else k * 3

        if self.use_hybrid:
            docs = self.hybrid_search(query, keyword_weight=self.hybrid_weight, k=retrieve_k)
        else:
            docs = self._semantic_search(query, k=retrieve_k)

        # 文件名匹配优化（在去重之前，确保匹配文档优先）
        docs = self._boost_file_name_matches(query, docs)

        docs = self._deduplicate_documents(docs)
        docs = self._ensure_diversity(docs, min_docs=k)

        if self.use_reranking and len(docs) > k:
            docs = self._simple_rerank(query, docs, top_k=k)
        else:
            docs = docs[:k]

        logger.info(f"检索完成: 候选={retrieve_k}, 去重后={len(docs)}, 返回={len(docs[:k])}")
        return docs

    def _semantic_search(self, query: str, k: int) -> List[Document]:
        return self.vectorstore.similarity_search(query, k=k)

    def hybrid_search(self, query: str,
                      keyword_weight: Optional[float] = None,
                      k: Optional[int] = None) -> List[Document]:
        """语义 + 关键词混合检索"""
        if keyword_weight is None:
            keyword_weight = self.hybrid_weight
        if k is None:
            k = self.k

        semantic_docs = self.vectorstore.similarity_search_with_score(query, k=k)
        keyword_docs = self._keyword_search(query, k=k)

        merged_docs = self._merge_and_rerank(
            semantic_docs,
            keyword_docs,
            keyword_weight
        )

        return merged_docs

    def _keyword_search(self, query: str, k: int) -> List[tuple]:
        """关键词检索（支持中文及特殊标识符）"""
        keywords = self._extract_keywords(query)
        if not keywords:
            return []

        if self.documents:
            candidate_docs = self.documents
        else:
            candidate_docs = self.vectorstore.similarity_search(query, k=k * 5)

        scored_docs = []
        for doc in candidate_docs:
            score = self._calculate_keyword_score(doc.page_content, keywords, query)
            if score > 0:
                scored_docs.append((doc, score))

        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return scored_docs[:k]

    def _extract_keywords(self, query: str) -> List[str]:
        """提取中文专有名词、数字、英文单词和特殊标识符"""
        keywords: List[str] = []

        keywords.extend(re.findall(r'[\u4e00-\u9fa5]{2,}', query))           # 中文词
        keywords.extend(re.findall(r'\d+(?:\.\d+)?%?', query))               # 数字/百分比

        stopwords = {'the', 'is', 'in', 'and', 'of', 'to', 'a', 'for', 'on', 'at',
                     'by', 'from', 'with', 'as', 'an', 'be', 'was', 'were', 'been',
                     'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                     'should', 'could', 'may', 'might', 'must', 'can'}
        english_words = re.findall(r'[a-zA-Z]+', query.lower())
        keywords.extend([w for w in english_words if w not in stopwords and len(w) > 2])

        keywords.extend(re.findall(r'[A-Z]+[\d/\-\\.]+[\dA-Z]*', query))     # 特殊标识

        logger.debug(f"提取关键词: {keywords}")
        return keywords

    def _calculate_keyword_score(self, text: str, keywords: List[str], original_query: str) -> float:
        """根据匹配程度计算关键词得分"""
        text_lower = text.lower()
        score = 0.0

        if original_query.lower() in text_lower or original_query in text:
            score += 10.0

        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword in text or keyword_lower in text_lower:
                count = text.count(keyword) + text_lower.count(keyword_lower)
                score += math.log1p(count) * 3.0

                if re.match(r'\d+', keyword) or re.match(r'[\u4e00-\u9fa5]{3,}', keyword):
                    score += 2.0

        return score

    def _merge_and_rerank(self,
                          semantic_docs: List[tuple],
                          keyword_docs: List[tuple],
                          keyword_weight: float) -> List[Document]:
        """合并语义与关键词得分"""

        def doc_hash(doc: Document) -> str:
            content = doc.page_content[:500]
            return hashlib.md5(content.encode('utf-8')).hexdigest()

        def normalize_scores(docs):
            if not docs:
                return {}
            max_score = max(score for _, score in docs)
            if max_score == 0:
                return {}
            return {doc_hash(doc): score / max_score for doc, score in docs}

        semantic_scores = normalize_scores(semantic_docs)
        keyword_scores = normalize_scores(keyword_docs)

        all_doc_hashes = set(semantic_scores.keys()) | set(keyword_scores.keys())
        semantic_weight = 1.0 - keyword_weight

        merged_scores = []
        doc_map = {}

        for doc, _ in semantic_docs:
            doc_map[doc_hash(doc)] = doc
        for doc, _ in keyword_docs:
            h = doc_hash(doc)
            if h not in doc_map:
                doc_map[h] = doc

        for doc_h in all_doc_hashes:
            semantic_score = semantic_scores.get(doc_h, 0.0)
            keyword_score = keyword_scores.get(doc_h, 0.0)

            if keyword_score > 0.7:
                final_score = semantic_score * 0.3 + keyword_score * 0.7
            else:
                final_score = (semantic_score * semantic_weight +
                               keyword_score * keyword_weight)

            merged_scores.append((doc_map[doc_h], final_score))

        merged_scores.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in merged_scores]

    def _deduplicate_documents(self, docs: List[Document]) -> List[Document]:
        """基于内容片段去重"""
        seen_hashes = set()
        unique_docs = []

        for doc in docs:
            content_sample = doc.page_content[:200]
            content_hash = hashlib.md5(content_sample.encode('utf-8')).hexdigest()
            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_docs.append(doc)

        logger.debug(f"去重: {len(docs)} -> {len(unique_docs)}")
        return unique_docs

    def _ensure_diversity(self, docs: List[Document], min_docs: int) -> List[Document]:
        """避免返回高度相似的文档"""
        if len(docs) <= min_docs:
            return docs

        diverse_docs = [docs[0]]
        for doc in docs[1:]:
            is_diverse = True
            for selected_doc in diverse_docs:
                similarity = self._calculate_content_similarity(
                    doc.page_content[:300],
                    selected_doc.page_content[:300]
                )
                if similarity > self.similarity_threshold:
                    is_diverse = False
                    break

            if is_diverse:
                diverse_docs.append(doc)
                if len(diverse_docs) >= min_docs * 2:
                    break

        logger.debug(f"多样性过滤: {len(docs)} -> {len(diverse_docs)}")
        return diverse_docs

    def _calculate_content_similarity(self, text1: str, text2: str) -> float:
        """基于字符集合的简单相似度"""
        set1 = set(text1)
        set2 = set(text2)
        if not set1 or not set2:
            return 0.0

        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union > 0 else 0.0

    def _llm_extract_file_names(self, query: str) -> List[str]:
        """
        使用大模型智能提取问题中涉及的文件名

        Args:
            query: 用户问题

        Returns:
            LLM提取的文件名列表
        """
        if not self.llm:
            logger.debug("LLM不可用，跳过智能文件名提取")
            return []

        try:
            # 构造提示词，要求LLM识别问题中提到的文件、文档或标准
            prompt = f"""**任务：** 从以下问题中提取文件名、文档名、报告名或标准编号。

**问题：** {query}

**要求：**
1. 识别问题中明确提到的文件、文档、报告、标准
2. 注意关键词："在...报告里"、"根据文档"、"标准"、"规范"等
3. 如果问题没有明确提到任何文件，直接返回"无"
4. 只返回文件名，每行一个，不要解释

**格式：**
```
文件名1
文件名2
```

**回答：**"""

            # 调用LLM
            from langchain.schema import HumanMessage

            # 根据不同的LLM类型调用
            try:
                if hasattr(self.llm, 'invoke'):
                    # 新版LangChain API
                    response = self.llm.invoke(prompt)
                    if hasattr(response, 'content'):
                        llm_output = response.content
                    else:
                        llm_output = str(response)
                elif hasattr(self.llm, 'predict'):
                    # 旧版API
                    llm_output = self.llm.predict(prompt)
                else:
                    # 直接调用
                    llm_output = self.llm(prompt)
            except Exception as e:
                logger.warning(f"LLM调用方法不匹配，尝试直接调用: {e}")
                llm_output = str(self.llm(prompt))

            # 从LLM输出中提取文件名
            # 移除可能的代码块标记
            llm_output = re.sub(r'```.*?```', lambda m: m.group(0).replace('```', ''), llm_output, flags=re.DOTALL)
            llm_output = llm_output.replace('```', '')

            lines = llm_output.strip().split('\n')
            file_names = []

            for line in lines:
                line = line.strip()
                # 跳过空行、"无"、"没有"等
                if not line or line in ['无', '没有', 'None', 'N/A', '无明确文件', '回答：', '**回答：**']:
                    continue
                # 移除序号（如"1. "、"- "、"* "等）
                line = re.sub(r'^[\d\.\-\*\s]+', '', line)
                line = line.strip()
                # 移除markdown格式标记
                line = re.sub(r'^\*\*|^\*|^-', '', line)
                line = line.strip()

                if len(line) >= 3:  # 至少3个字符
                    file_names.append(line)

            logger.info(f"LLM提取文件名: {file_names}")
            return file_names

        except Exception as e:
            logger.warning(f"LLM文件名提取失败: {e}")
            return []

    def _extract_file_names_regex(self, query: str) -> List[str]:
        """
        使用正则表达式从问题中提取文件名

        支持多种模式：
        - 在...报告里/文档里/的报告中
        - 根据文档《...》
        - 文件名模式（包括中文、英文、标准编号等）

        Args:
            query: 用户问题

        Returns:
            提取的文件名列表
        """
        file_names = []

        # 模式1: 在...报告里/文档里/中
        patterns = [
            r'在[《\"\']*([^》\"\'\n，。！？]{3,30}?)[》\"\']*(?:的)?(?:报告|文档|文件|事件调查报告|分析报告|技术报告)(?:里|中|内)',
            r'根据[《\"\']*([^》\"\'\n，。！？]{3,30}?)[》\"\']*(?:报告|文档|文件)',
            r'文档[《\"\']*([^》\"\'\n，。！？]{3,30}?)[》\"\']*',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, query)
            file_names.extend(matches)

        # 模式2: 《文件名》
        matches = re.findall(r'《([^》]{3,50})》', query)
        file_names.extend(matches)

        # 模式3: 标准编号和技术文档（IEEE, GB/T, ISO等）
        standard_patterns = [
            r'(IEEE\s+[\d.]+(?:-[\d]+)?)',
            r'(GB/T\s+\d+(?:-\d+)?)',
            r'(ISO\s+\d+(?:-\d+)?)',
            r'(IEC\s+\d+(?:-\d+)?)',
            r'(EN\s+\d+(?:-\d+)?)',
        ]

        for pattern in standard_patterns:
            matches = re.findall(pattern, query, re.IGNORECASE)
            file_names.extend(matches)

        # 模式4: 年份+英文词组（如"2024_Communications-Based Train Control"）
        matches = re.findall(r'(\d{4}[_-][A-Za-z][A-Za-z0-9_\-\s]{5,40})', query)
        file_names.extend(matches)

        # 清理和规范化
        cleaned_names = []
        for name in file_names:
            name = name.strip()
            # 移除可能的标点符号
            name = re.sub(r'^[，。、：:；;]+', '', name)
            name = re.sub(r'[，。、：:；;]+$', '', name)
            if len(name) >= 3:  # 至少3个字符
                cleaned_names.append(name)

        logger.debug(f"正则提取文件名: {cleaned_names}")
        return cleaned_names

    def _extract_file_names(self, query: str) -> List[str]:
        """
        综合提取文件名（正则 + LLM）

        策略：
        1. 使用正则表达式提取明确的模式
        2. 使用LLM提取语义层面的文件引用
        3. 合并去重

        Args:
            query: 用户问题

        Returns:
            提取的文件名列表（已去重）
        """
        # 1. 正则提取
        regex_names = self._extract_file_names_regex(query)

        # 2. LLM提取
        llm_names = self._llm_extract_file_names(query)

        # 3. 合并去重（保持顺序，LLM的结果优先级更高）
        all_names = []
        seen = set()

        # 先添加LLM提取的（语义理解更准确）
        for name in llm_names:
            name_lower = name.lower()
            if name_lower not in seen:
                all_names.append(name)
                seen.add(name_lower)

        # 再添加正则提取的（补充遗漏）
        for name in regex_names:
            name_lower = name.lower()
            if name_lower not in seen:
                all_names.append(name)
                seen.add(name_lower)

        logger.info(f"文件名提取完成: 正则={len(regex_names)}, LLM={len(llm_names)}, 合并后={len(all_names)}")
        if all_names:
            logger.info(f"提取的文件名: {all_names}")

        return all_names

    def _boost_file_name_matches(self, query: str, docs: List[Document]) -> List[Document]:
        """
        根据文件名匹配提升文档优先级

        策略：
        1. 从问题中提取可能的文件名
        2. 对每个文档，检查其source是否匹配提取的文件名
        3. 匹配的文档移到列表前面

        Args:
            query: 用户问题
            docs: 文档列表

        Returns:
            重排序后的文档列表（匹配文档优先）
        """
        if not docs:
            return docs

        # 提取问题中的文件名
        extracted_names = self._extract_file_names(query)

        if not extracted_names:
            logger.debug("未从问题中提取到文件名，跳过文件名匹配")
            print("  [文件名提取] 未提取到文件名")
            return docs

        # ========== 输出提取的文件名并验证存在性 ==========
        print(f"\n{'='*60}")
        print(f"[文件名提取] 从问题中提取到 {len(extracted_names)} 个文件名:")
        for i, name in enumerate(extracted_names, 1):
            print(f"  {i}. {name}")

        # 收集所有文档的source路径用于验证
        all_sources = set()
        for doc in docs:
            source = doc.metadata.get('source', '')
            if source:
                all_sources.add(source)

        # 验证每个提取的文件名是否在文档库中存在
        print(f"\n[文件验证] 检查文件是否存在于文档库:")
        verified_names = []
        for name in extracted_names:
            exists = False
            matched_source = None

            # 检查是否有文档source包含这个文件名
            for source in all_sources:
                source_lower = source.lower()
                name_lower = name.lower()

                # 多种匹配方式
                if name in source or name_lower in source_lower:
                    exists = True
                    matched_source = source
                    break

                # 移除特殊字符后匹配
                name_clean = name.replace(' ', '').replace('_', '').replace('-', '')
                source_clean = source.replace(' ', '').replace('_', '').replace('-', '')
                if len(name_clean) >= 5 and name_clean in source_clean:
                    exists = True
                    matched_source = source
                    break

            if exists:
                print(f"  ✓ '{name}' -> 找到: {matched_source}")
                verified_names.append(name)
            else:
                print(f"  ✗ '{name}' -> 未找到匹配文档")

        print(f"\n[匹配结果] 验证通过: {len(verified_names)}/{len(extracted_names)} 个文件")
        print(f"{'='*60}\n")
        # ========== 验证完成 ==========

        # 分类文档：匹配的和不匹配的
        matched_docs = []
        unmatched_docs = []

        for doc in docs:
            # 获取文档的source（文件路径）
            source = doc.metadata.get('source', '')

            # 检查是否有任何提取的文件名匹配source
            is_matched = False
            for file_name in extracted_names:
                # 多种匹配方式
                file_name_lower = file_name.lower()
                source_lower = source.lower()

                # 方式1: 直接包含
                if file_name in source or file_name_lower in source_lower:
                    is_matched = True
                    logger.debug(f"文件名匹配（直接）: '{file_name}' in '{source}'")
                    break

                # 方式2: 移除空格后匹配（处理可能的编码问题）
                file_name_no_space = file_name.replace(' ', '').replace('_', '').replace('-', '')
                source_no_space = source.replace(' ', '').replace('_', '').replace('-', '')
                if len(file_name_no_space) >= 5 and file_name_no_space in source_no_space:
                    is_matched = True
                    logger.debug(f"文件名匹配（无空格）: '{file_name}' ~ '{source}'")
                    break

                # 方式3: 模糊匹配（至少60%字符相同）
                if len(file_name) >= 5:
                    # 简单的字符重叠度计算
                    set_name = set(file_name_lower)
                    set_source = set(source_lower)
                    if set_name and set_source:
                        overlap = len(set_name & set_source) / len(set_name)
                        if overlap >= 0.6:
                            is_matched = True
                            logger.debug(f"文件名匹配（模糊{overlap:.2f}）: '{file_name}' ~ '{source}'")
                            break

            if is_matched:
                matched_docs.append(doc)
            else:
                unmatched_docs.append(doc)

        if matched_docs:
            logger.info(f"文件名匹配: 找到{len(matched_docs)}个匹配文档，将优先返回")
            # 匹配的文档放在前面，然后是未匹配的
            return matched_docs + unmatched_docs
        else:
            logger.debug("没有文档匹配提取的文件名")
            return docs

    def _simple_rerank(self, query: str, docs: List[Document], top_k: int) -> List[Document]:
        """基于关键词重叠的重排序"""
        query_keywords = set(self._extract_keywords(query))
        if not query_keywords:
            return docs[:top_k]

        scored_docs = []
        for doc in docs:
            doc_keywords = set(self._extract_keywords(doc.page_content[:500]))
            if not doc_keywords:
                similarity = 0.0
            else:
                intersection = len(query_keywords & doc_keywords)
                union = len(query_keywords | doc_keywords)
                similarity = intersection / union if union > 0 else 0.0

            scored_docs.append((doc, similarity))

        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored_docs[:top_k]]


def create_retriever(vectorstore,
                     documents: Optional[List[Document]] = None,
                     config: Optional[Dict] = None,
                     k: int = 10,
                     llm: Optional[Any] = None) -> Retriever:
    """创建检索器实例的工厂函数"""
    return Retriever(vectorstore, documents, config, k, llm)


class QueryExpander:
    """查询扩展器，用于生成语义相近的查询"""

    @staticmethod
    def expand_query(query: str) -> List[str]:
        expanded = [query]
        synonyms = {
            "中标": ["获得", "承揽", "签约"],
            "金额": ["价格", "费用", "总额"],
            "百分比": ["比例", "占比", "百分率"],
            "目标": ["指标", "要求", "计划"],
        }

        for word, syns in synonyms.items():
            if word in query:
                for syn in syns:
                    expanded.append(query.replace(word, syn))

        return expanded[:3]


class Reranker:
    """基于关键词重叠的简单重排序器"""

    @staticmethod
    def rerank_by_question_similarity(documents: List[Document],
                                      question: str,
                                      top_k: int = 5) -> List[Document]:
        question_words = set(question.lower().split())
        scored_docs = []

        for doc in documents:
            doc_words = set(doc.page_content.lower().split())
            intersection = len(question_words & doc_words)
            union = len(question_words | doc_words)
            similarity = intersection / union if union > 0 else 0
            scored_docs.append((doc, similarity))

        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored_docs[:top_k]]


class QueryExpander:
    """查询扩展器，用于改进查询质量"""

    @staticmethod
    def expand_query(query: str) -> List[str]:
        """
        扩展查询，生成多个相关查询

        Args:
            query: 原始查询

        Returns:
            扩展后的查询列表
        """
        expanded = [query]

        # 1. 添加同义词（这里简化处理，实际应使用词库）
        synonyms = {
            "中标": ["获得", "承揽", "签约"],
            "金额": ["价格", "费用", "总额"],
            "百分比": ["比例", "占比", "百分率"],
            "目标": ["指标", "要求", "计划"],
        }

        for word, syns in synonyms.items():
            if word in query:
                for syn in syns:
                    expanded.append(query.replace(word, syn))

        return expanded[:3]  # 限制扩展数量


class Reranker:
    """重排序器"""

    @staticmethod
    def rerank_by_question_similarity(
        documents: List[Document],
        question: str,
        top_k: int = 5
    ) -> List[Document]:
        """
        根据与问题的相似度重排序

        Args:
            documents: 文档列表
            question: 问题
            top_k: 返回前k个文档

        Returns:
            重排序后的文档列表
        """
        # 简单的相似度计算：基于关键词重叠
        question_words = set(question.lower().split())

        scored_docs = []
        for doc in documents:
            doc_words = set(doc.page_content.lower().split())
            # Jaccard相似度
            intersection = len(question_words & doc_words)
            union = len(question_words | doc_words)
            similarity = intersection / union if union > 0 else 0
            scored_docs.append((doc, similarity))

        # 排序并返回
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored_docs[:top_k]]


