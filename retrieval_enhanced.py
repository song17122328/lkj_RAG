"""
增强版RAG检索功能
修复问题：
1. 基于内容的去重（而非对象ID）
2. 改进的中文关键词提取
3. 文档多样性约束
4. 更好的混合搜索策略
"""

from typing import List, Dict, Any, Optional, Set
import logging
import re
import math
import hashlib
from langchain.schema import Document

# 配置文件
try:
    from config import ADVANCED_FEATURES
except ImportError:
    ADVANCED_FEATURES = {"hybrid_search": False, "reranking": False}

logger = logging.getLogger(__name__)


class EnhancedRetriever:
    """增强版检索器，支持去重、多样性和改进的混合检索"""

    def __init__(self, vectorstore, documents: Optional[List[Document]] = None,
                 config: Optional[Dict] = None, k: int = 10):
        """
        初始化检索器

        Args:
            vectorstore: 向量存储
            documents: 所有文档列表（可选，用于关键词搜索）
            config: 配置字典（可选，默认从 ADVANCED_FEATURES 读取）
            k: 返回的文档数量
        """
        self.vectorstore = vectorstore
        self.documents = documents or []
        self.config = config if config is not None else ADVANCED_FEATURES
        self.k = k

        # 从配置获取参数
        self.use_hybrid = self.config.get("hybrid_search", False)
        self.hybrid_weight = self.config.get("hybrid_weight", 0.3)
        self.use_reranking = self.config.get("reranking", False)
        self.reranking_top_k = self.config.get("reranking_top_k", 20)

        # 去重和多样性参数
        self.similarity_threshold = 0.9  # 内容相似度阈值（超过此值认为重复）
        self.diversity_threshold = 0.3   # 多样性阈值（低于此值的文档将被过滤）

        logger.info(f"增强检索器初始化: hybrid={self.use_hybrid}, reranking={self.use_reranking}, k={k}")

    def retrieve(self, query: str, k: Optional[int] = None) -> List[Document]:
        """
        执行检索（带去重和多样性约束）

        Args:
            query: 查询文本
            k: 返回文档数（如果为None，使用初始化时的k值）

        Returns:
            去重后的文档列表
        """
        if k is None:
            k = self.k

        # 如果启用重排序，先检索更多候选
        retrieve_k = self.reranking_top_k if self.use_reranking else k * 3  # 增加候选数量

        # 1. 执行检索
        if self.use_hybrid:
            docs = self.hybrid_search(query, keyword_weight=self.hybrid_weight, k=retrieve_k)
        else:
            docs = self._semantic_search(query, k=retrieve_k)

        # 2. 去重（基于内容哈希）
        docs = self._deduplicate_documents(docs)

        # 3. 多样性过滤
        docs = self._ensure_diversity(docs, min_docs=k)

        # 4. 重排序
        if self.use_reranking and len(docs) > k:
            docs = self._simple_rerank(query, docs, top_k=k)
        else:
            docs = docs[:k]

        logger.info(f"检索完成: 原始候选={retrieve_k}, 去重后={len(docs)}, 最终返回={len(docs[:k])}")
        return docs

    def _semantic_search(self, query: str, k: int) -> List[Document]:
        """语义搜索"""
        return self.vectorstore.similarity_search(query, k=k)

    def hybrid_search(self, query: str, keyword_weight: Optional[float] = None, k: Optional[int] = None) -> List[Document]:
        """
        混合检索：结合语义搜索和关键词搜索

        Args:
            query: 查询文本
            keyword_weight: 关键词搜索的权重（0-1之间）
            k: 返回的文档数量

        Returns:
            检索到的文档列表
        """
        if keyword_weight is None:
            keyword_weight = self.hybrid_weight
        if k is None:
            k = self.k

        # 1. 语义搜索
        semantic_docs = self.vectorstore.similarity_search_with_score(query, k=k)

        # 2. 关键词匹配
        keyword_docs = self._keyword_search(query, k=k)

        # 3. 合并结果并重排序（使用内容哈希去重）
        merged_docs = self._merge_and_rerank(
            semantic_docs,
            keyword_docs,
            keyword_weight
        )

        return merged_docs

    def _keyword_search(self, query: str, k: int) -> List[tuple]:
        """
        改进的关键词搜索（专门优化中文专有名词）

        Args:
            query: 查询文本
            k: 返回文档数

        Returns:
            (文档, 分数)元组列表
        """
        # 提取关键词（改进版：支持中文专有名词）
        keywords = self._extract_keywords_enhanced(query)

        if not keywords:
            return []

        # 如果有文档列表，使用文档列表；否则从向量存储获取
        if self.documents:
            candidate_docs = self.documents
        else:
            candidate_docs = self.vectorstore.similarity_search(query, k=k*5)

        # 计算关键词匹配分数
        scored_docs = []
        for doc in candidate_docs:
            score = self._calculate_keyword_score_enhanced(doc.page_content, keywords, query)
            if score > 0:
                scored_docs.append((doc, score))

        # 按分数排序
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return scored_docs[:k]

    def _extract_keywords_enhanced(self, query: str) -> List[str]:
        """
        增强版关键词提取（专门优化中文）

        Args:
            query: 查询文本

        Returns:
            关键词列表
        """
        keywords = []

        # 1. 提取中文专有名词（连续的中文字符）
        chinese_patterns = re.findall(r'[\u4e00-\u9fa5]{2,}', query)
        keywords.extend(chinese_patterns)

        # 2. 提取数字（年份、金额、百分比等）
        number_patterns = re.findall(r'\d+(?:\.\d+)?%?', query)
        keywords.extend(number_patterns)

        # 3. 提取英文单词（过滤停用词）
        stopwords = {'the', 'is', 'in', 'and', 'of', 'to', 'a', 'for', 'on', 'at',
                    'by', 'from', 'with', 'as', 'an', 'be', 'was', 'were', 'been',
                    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                    'should', 'could', 'may', 'might', 'must', 'can'}

        english_words = re.findall(r'[a-zA-Z]+', query.lower())
        keywords.extend([w for w in english_words if w not in stopwords and len(w) > 2])

        # 4. 提取特殊标识符（如GB/T 43267、S7等）
        special_patterns = re.findall(r'[A-Z]+[\d/\-\\.]+[\dA-Z]*', query)
        keywords.extend(special_patterns)

        logger.debug(f"提取的关键词: {keywords}")
        return keywords

    def _calculate_keyword_score_enhanced(self, text: str, keywords: List[str], original_query: str) -> float:
        """
        增强版关键词评分（考虑完整匹配和位置权重）

        Args:
            text: 文档文本
            keywords: 关键词列表
            original_query: 原始查询

        Returns:
            匹配分数
        """
        text_lower = text.lower()
        score = 0.0

        # 1. 完整查询匹配（最高优先级）
        if original_query.lower() in text_lower or original_query in text:
            score += 10.0

        # 2. 关键词匹配
        for keyword in keywords:
            keyword_lower = keyword.lower()

            # 完整匹配（高权重）
            if keyword in text or keyword_lower in text_lower:
                count = text.count(keyword) + text_lower.count(keyword_lower)
                # 使用对数尺度，避免过度偏向高频词
                score += math.log1p(count) * 3.0

                # 如果是数字或专有名词，额外加分
                if re.match(r'\d+', keyword) or re.match(r'[\u4e00-\u9fa5]{3,}', keyword):
                    score += 2.0

        return score

    def _merge_and_rerank(self,
                          semantic_docs: List[tuple],
                          keyword_docs: List[tuple],
                          keyword_weight: float) -> List[Document]:
        """
        合并语义搜索和关键词搜索结果（使用内容哈希去重）

        Args:
            semantic_docs: 语义搜索结果 [(doc, score), ...]
            keyword_docs: 关键词搜索结果 [(doc, score), ...]
            keyword_weight: 关键词搜索的权重

        Returns:
            重排序后的文档列表
        """
        # 使用内容哈希代替对象ID
        def doc_hash(doc: Document) -> str:
            """计算文档内容的哈希值"""
            content = doc.page_content[:500]  # 使用前500字符
            return hashlib.md5(content.encode('utf-8')).hexdigest()

        # 归一化分数
        def normalize_scores(docs):
            if not docs:
                return {}
            max_score = max(score for _, score in docs)
            if max_score == 0:
                return {}
            return {doc_hash(doc): score/max_score for doc, score in docs}

        semantic_scores = normalize_scores(semantic_docs)
        keyword_scores = normalize_scores(keyword_docs)

        # 合并分数
        all_doc_hashes = set(semantic_scores.keys()) | set(keyword_scores.keys())
        semantic_weight = 1.0 - keyword_weight

        merged_scores = []
        doc_map = {}

        # 构建文档映射（使用哈希）
        for doc, _ in semantic_docs:
            doc_map[doc_hash(doc)] = doc
        for doc, _ in keyword_docs:
            h = doc_hash(doc)
            if h not in doc_map:  # 避免覆盖
                doc_map[h] = doc

        # 计算合并分数
        for doc_h in all_doc_hashes:
            semantic_score = semantic_scores.get(doc_h, 0.0)
            keyword_score = keyword_scores.get(doc_h, 0.0)

            # 如果关键词得分很高，给予额外权重
            if keyword_score > 0.7:
                final_score = semantic_score * 0.3 + keyword_score * 0.7
            else:
                final_score = (semantic_score * semantic_weight + keyword_score * keyword_weight)

            merged_scores.append((doc_map[doc_h], final_score))

        # 排序
        merged_scores.sort(key=lambda x: x[1], reverse=True)

        return [doc for doc, _ in merged_scores]

    def _deduplicate_documents(self, docs: List[Document]) -> List[Document]:
        """
        基于内容的文档去重

        Args:
            docs: 文档列表

        Returns:
            去重后的文档列表
        """
        seen_hashes = set()
        unique_docs = []

        for doc in docs:
            # 使用文档前200字符计算哈希
            content_sample = doc.page_content[:200]
            content_hash = hashlib.md5(content_sample.encode('utf-8')).hexdigest()

            if content_hash not in seen_hashes:
                seen_hashes.add(content_hash)
                unique_docs.append(doc)

        logger.debug(f"去重: {len(docs)} -> {len(unique_docs)} 文档")
        return unique_docs

    def _ensure_diversity(self, docs: List[Document], min_docs: int) -> List[Document]:
        """
        确保文档多样性（避免返回过于相似的文档）

        Args:
            docs: 文档列表
            min_docs: 最少保留的文档数

        Returns:
            多样化后的文档列表
        """
        if len(docs) <= min_docs:
            return docs

        diverse_docs = [docs[0]]  # 总是保留第一个（最相关的）

        for doc in docs[1:]:
            # 检查与已选文档的相似度
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
                if len(diverse_docs) >= min_docs * 2:  # 最多返回2倍所需数量
                    break

        logger.debug(f"多样性过滤: {len(docs)} -> {len(diverse_docs)} 文档")
        return diverse_docs

    def _calculate_content_similarity(self, text1: str, text2: str) -> float:
        """
        计算两段文本的相似度（Jaccard相似度）

        Args:
            text1: 文本1
            text2: 文本2

        Returns:
            相似度（0-1之间）
        """
        # 简单的字符级Jaccard相似度
        set1 = set(text1)
        set2 = set(text2)

        if not set1 or not set2:
            return 0.0

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union > 0 else 0.0

    def _simple_rerank(self, query: str, docs: List[Document], top_k: int) -> List[Document]:
        """
        简单重排序：基于查询-文档相似度

        Args:
            query: 查询文本
            docs: 文档列表
            top_k: 返回文档数

        Returns:
            重排序后的文档列表
        """
        query_keywords = set(self._extract_keywords_enhanced(query))

        if not query_keywords:
            return docs[:top_k]

        scored_docs = []
        for doc in docs:
            doc_keywords = set(self._extract_keywords_enhanced(doc.page_content[:500]))

            # 计算关键词重叠度
            if not doc_keywords:
                similarity = 0.0
            else:
                intersection = len(query_keywords & doc_keywords)
                union = len(query_keywords | doc_keywords)
                similarity = intersection / union if union > 0 else 0.0

            scored_docs.append((doc, similarity))

        # 排序
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return [doc for doc, _ in scored_docs[:top_k]]


def create_enhanced_retriever(vectorstore, documents: Optional[List[Document]] = None,
                              config: Optional[Dict] = None, k: int = 10) -> EnhancedRetriever:
    """
    创建增强版检索器的工厂函数

    Args:
        vectorstore: 向量存储
        documents: 文档列表（可选）
        config: 配置字典（可选）
        k: 返回文档数

    Returns:
        EnhancedRetriever实例
    """
    return EnhancedRetriever(vectorstore, documents, config, k)
