"""
增强版RAG系统
集成混合检索和重排序功能
"""

from typing import List, Dict, Any
import logging
from langchain.schema import Document

# 配置文件
try:
    from config import RETRIEVAL, ADVANCED_FEATURES
except ImportError:
    RETRIEVAL = {"k": 10}
    ADVANCED_FEATURES = {"hybrid_search": False, "reranking": False}

logger = logging.getLogger(__name__)


class EnhancedRetriever:
    """增强检索器，支持混合检索和重排序"""

    def __init__(self, vectorstore, documents: List[Document], config: Dict = None):
        """
        初始化增强检索器

        Args:
            vectorstore: 向量存储
            documents: 所有文档列表
            config: 配置字典
        """
        self.vectorstore = vectorstore
        self.documents = documents
        self.config = config or {}

        # 从配置获取参数
        self.use_hybrid = self.config.get("hybrid_search", False)
        self.hybrid_weight = self.config.get("hybrid_weight", 0.3)
        self.use_reranking = self.config.get("reranking", False)
        self.reranking_top_k = self.config.get("reranking_top_k", 20)

        logger.info(f"增强检索器初始化: hybrid={self.use_hybrid}, reranking={self.use_reranking}")

    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        """
        执行检索

        Args:
            query: 查询文本
            k: 返回文档数

        Returns:
            检索到的文档列表
        """
        # 如果启用重排序，先检索更多候选
        retrieve_k = self.reranking_top_k if self.use_reranking else k

        # 1. 执行检索
        if self.use_hybrid:
            docs = self._hybrid_search(query, k=retrieve_k)
        else:
            docs = self._semantic_search(query, k=retrieve_k)

        # 2. 重排序
        if self.use_reranking and len(docs) > k:
            docs = self._simple_rerank(query, docs, top_k=k)
        else:
            docs = docs[:k]

        return docs

    def _semantic_search(self, query: str, k: int) -> List[Document]:
        """语义搜索"""
        return self.vectorstore.similarity_search(query, k=k)

    def _hybrid_search(self, query: str, k: int) -> List[Document]:
        """
        混合搜索：结合语义搜索和关键词匹配

        Args:
            query: 查询文本
            k: 返回文档数

        Returns:
            文档列表
        """
        # 1. 语义搜索
        semantic_docs = self.vectorstore.similarity_search_with_score(query, k=k*2)

        # 2. 关键词匹配（简化版BM25）
        keyword_docs = self._keyword_match(query, k=k*2)

        # 3. 合并结果
        merged = self._merge_results(semantic_docs, keyword_docs)

        return merged[:k]

    def _keyword_match(self, query: str, k: int) -> List[tuple]:
        """
        简单的关键词匹配

        Args:
            query: 查询文本
            k: 返回文档数

        Returns:
            (文档, 分数)列表
        """
        # 提取查询关键词（简单分词）
        keywords = self._extract_keywords(query)

        if not keywords:
            return []

        # 计算每个文档的关键词匹配分数
        scored_docs = []
        for doc in self.documents:
            score = self._calculate_keyword_score(doc.page_content, keywords)
            if score > 0:
                scored_docs.append((doc, score))

        # 排序并返回top-k
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return scored_docs[:k]

    def _extract_keywords(self, query: str) -> List[str]:
        """
        提取查询关键词

        Args:
            query: 查询文本

        Returns:
            关键词列表
        """
        # 简单实现：分词 + 过滤停用词
        stopwords = {'的', '是', '在', '和', '与', '了', '吗', '呢', '啊', '等',
                    'the', 'is', 'in', 'and', 'of', 'to', 'a', 'for', 'on'}

        # 简单分词（按空格和标点分割）
        import re
        words = re.findall(r'\w+', query.lower())

        # 过滤停用词和短词
        keywords = [w for w in words if w not in stopwords and len(w) > 1]

        return keywords

    def _calculate_keyword_score(self, text: str, keywords: List[str]) -> float:
        """
        计算关键词匹配分数

        Args:
            text: 文档文本
            keywords: 关键词列表

        Returns:
            匹配分数
        """
        text_lower = text.lower()
        score = 0.0

        for keyword in keywords:
            # 完整匹配：更高分数
            if keyword in text_lower:
                count = text_lower.count(keyword)
                # TF权重（对数尺度）
                import math
                score += math.log1p(count) * 2.0

            # 部分匹配：较低分数
            elif any(keyword in word for word in text_lower.split()):
                score += 0.5

        return score

    def _merge_results(self,
                      semantic_docs: List[tuple],
                      keyword_docs: List[tuple]) -> List[Document]:
        """
        合并语义搜索和关键词搜索结果

        Args:
            semantic_docs: [(doc, score), ...]
            keyword_docs: [(doc, score), ...]

        Returns:
            合并后的文档列表
        """
        # 归一化分数
        def normalize_scores(docs):
            if not docs:
                return {}
            max_score = max(score for _, score in docs)
            if max_score == 0:
                return {id(doc): 0.0 for doc, _ in docs}
            return {id(doc): score/max_score for doc, score in docs}

        semantic_scores = normalize_scores(semantic_docs)
        keyword_scores = normalize_scores(keyword_docs)

        # 合并分数
        all_doc_ids = set(semantic_scores.keys()) | set(keyword_scores.keys())

        semantic_weight = 1.0 - self.hybrid_weight
        keyword_weight = self.hybrid_weight

        merged_scores = []
        doc_map = {}

        # 构建文档映射
        for doc, _ in semantic_docs:
            doc_map[id(doc)] = doc
        for doc, _ in keyword_docs:
            doc_map[id(doc)] = doc

        # 计算合并分数
        for doc_id in all_doc_ids:
            semantic_score = semantic_scores.get(doc_id, 0.0)
            keyword_score = keyword_scores.get(doc_id, 0.0)

            final_score = (semantic_score * semantic_weight +
                          keyword_score * keyword_weight)

            merged_scores.append((doc_map[doc_id], final_score))

        # 排序
        merged_scores.sort(key=lambda x: x[1], reverse=True)

        return [doc for doc, _ in merged_scores]

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
        query_words = set(self._extract_keywords(query))

        if not query_words:
            return docs[:top_k]

        scored_docs = []
        for doc in docs:
            doc_words = set(self._extract_keywords(doc.page_content[:500]))  # 只看前500字

            # 计算Jaccard相似度
            if not doc_words:
                similarity = 0.0
            else:
                intersection = len(query_words & doc_words)
                union = len(query_words | doc_words)
                similarity = intersection / union if union > 0 else 0.0

            scored_docs.append((doc, similarity))

        # 排序
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return [doc for doc, _ in scored_docs[:top_k]]


def create_enhanced_retriever(vectorstore, documents: List[Document]) -> EnhancedRetriever:
    """
    创建增强检索器的工厂函数

    Args:
        vectorstore: 向量存储
        documents: 文档列表

    Returns:
        EnhancedRetriever实例
    """
    return EnhancedRetriever(
        vectorstore=vectorstore,
        documents=documents,
        config=ADVANCED_FEATURES
    )
