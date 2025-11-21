"""
RAG检索功能
包含：重排序、混合检索、查询扩展等技术
"""

from typing import List, Dict, Any, Optional
import logging
import re
import math
from langchain.schema import Document

# 配置文件
try:
    from config import ADVANCED_FEATURES
except ImportError:
    ADVANCED_FEATURES = {"hybrid_search": False, "reranking": False}

logger = logging.getLogger(__name__)


class Retriever:
    """检索器，支持重排序和混合检索"""

    def __init__(self, vectorstore, documents: Optional[List[Document]] = None, 
                 config: Optional[Dict] = None, k: int = 10):
        """
        初始化检索器

        Args:
            vectorstore: 向量存储
            documents: 所有文档列表（可选，用于更好的关键词搜索）
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

        logger.info(f"检索器初始化: hybrid={self.use_hybrid}, reranking={self.use_reranking}, k={k}")

    def retrieve(self, query: str, k: Optional[int] = None) -> List[Document]:
        """
        执行检索（根据配置自动选择混合搜索或语义搜索）

        Args:
            query: 查询文本
            k: 返回文档数（如果为None，使用初始化时的k值）

        Returns:
            检索到的文档列表
        """
        if k is None:
            k = self.k

        # 如果启用重排序，先检索更多候选
        retrieve_k = self.reranking_top_k if self.use_reranking else k

        # 1. 执行检索
        if self.use_hybrid:
            docs = self.hybrid_search(query, keyword_weight=self.hybrid_weight, k=retrieve_k)
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

    def hybrid_search(self, query: str, keyword_weight: Optional[float] = None, k: Optional[int] = None) -> List[Document]:
        """
        混合检索：结合语义搜索和关键词搜索

        Args:
            query: 查询文本
            keyword_weight: 关键词搜索的权重（0-1之间，如果为None，使用配置值）
            k: 返回的文档数量（如果为None，使用初始化时的k值）

        Returns:
            检索到的文档列表
        """
        if keyword_weight is None:
            keyword_weight = self.hybrid_weight
        if k is None:
            k = self.k

        # 1. 语义搜索
        semantic_docs = self.vectorstore.similarity_search_with_score(query, k=k*2)

        # 2. 关键词匹配（改进版BM25）
        keyword_docs = self._keyword_search(query, k=k*2)

        # 3. 合并结果并重排序
        merged_docs = self._merge_and_rerank(
            semantic_docs,
            keyword_docs,
            keyword_weight
        )

        return merged_docs[:k]

    def _keyword_search(self, query: str, k: int) -> List[tuple]:
        """
        改进的关键词搜索

        Args:
            query: 查询文本
            k: 返回文档数

        Returns:
            (文档, 分数)元组列表
        """
        # 提取关键词（改进版：过滤停用词）
        keywords = self._extract_keywords(query)

        if not keywords:
            return []

        # 如果有文档列表，使用文档列表；否则从向量存储获取
        if self.documents:
            candidate_docs = self.documents
        else:
            candidate_docs = self.vectorstore.similarity_search(query, k=k*3)

        # 计算关键词匹配分数
        scored_docs = []
        for doc in candidate_docs:
            score = self._calculate_keyword_score(doc.page_content, keywords)
            if score > 0:
                scored_docs.append((doc, score))

        # 按分数排序
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return scored_docs[:k]

    def _extract_keywords(self, query: str) -> List[str]:
        """
        提取查询关键词（改进版：过滤停用词）

        Args:
            query: 查询文本

        Returns:
            关键词列表
        """
        # 停用词列表
        stopwords = {'的', '是', '在', '和', '与', '了', '吗', '呢', '啊', '等',
                    'the', 'is', 'in', 'and', 'of', 'to', 'a', 'for', 'on', 'at',
                    'by', 'from', 'with', 'as', 'an', 'be', 'was', 'were', 'been',
                    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                    'should', 'could', 'may', 'might', 'must', 'can'}

        # 简单分词（按空格和标点分割）
        words = re.findall(r'\w+', query.lower())

        # 过滤停用词和短词
        keywords = [w for w in words if w not in stopwords and len(w) > 1]

        return keywords

    def _calculate_keyword_score(self, text: str, keywords: List[str]) -> float:
        """
        计算关键词匹配分数（改进版：使用TF权重和对数尺度）

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
                score += math.log1p(count) * 2.0

            # 部分匹配：较低分数
            elif any(keyword in word for word in text_lower.split()):
                score += 0.5

        return score

    def _merge_and_rerank(self,
                          semantic_docs: List[tuple],
                          keyword_docs: List[tuple],
                          keyword_weight: float) -> List[Document]:
        """
        合并语义搜索和关键词搜索结果，并重排序

        Args:
            semantic_docs: 语义搜索结果 [(doc, score), ...]
            keyword_docs: 关键词搜索结果 [(doc, score), ...]
            keyword_weight: 关键词搜索的权重

        Returns:
            重排序后的文档列表
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

        semantic_weight = 1.0 - keyword_weight

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


