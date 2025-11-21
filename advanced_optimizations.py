"""
高级RAG优化示例
包含：重排序、混合检索、查询扩展等高级技术
"""

from typing import List, Dict, Any
import logging
from langchain.schema import Document

logger = logging.getLogger(__name__)


class AdvancedRetriever:
    """高级检索器，支持重排序和混合检索"""

    def __init__(self, vectorstore, k: int = 10):
        """
        初始化高级检索器

        Args:
            vectorstore: 向量存储
            k: 返回的文档数量
        """
        self.vectorstore = vectorstore
        self.k = k

    def hybrid_search(self, query: str, keyword_weight: float = 0.3) -> List[Document]:
        """
        混合检索：结合语义搜索和关键词搜索

        Args:
            query: 查询文本
            keyword_weight: 关键词搜索的权重（0-1之间）

        Returns:
            检索到的文档列表
        """
        # 1. 语义搜索
        semantic_docs = self.vectorstore.similarity_search_with_score(query, k=self.k*2)

        # 2. 简单的关键词匹配（BM25的简化版本）
        keyword_docs = self._keyword_search(query, k=self.k*2)

        # 3. 合并结果并重排序
        merged_docs = self._merge_and_rerank(
            semantic_docs,
            keyword_docs,
            keyword_weight
        )

        return merged_docs[:self.k]

    def _keyword_search(self, query: str, k: int) -> List[tuple]:
        """
        简单的关键词搜索

        Args:
            query: 查询文本
            k: 返回文档数

        Returns:
            (文档, 分数)元组列表
        """
        # 提取关键词（简化版本）
        keywords = query.split()

        # 从向量存储获取所有文档（实际应用中应该使用专门的全文检索引擎）
        all_docs = self.vectorstore.similarity_search(query, k=k*3)

        # 计算关键词匹配分数
        scored_docs = []
        for doc in all_docs:
            score = sum(1 for kw in keywords if kw in doc.page_content)
            scored_docs.append((doc, float(score)))

        # 按分数排序
        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return scored_docs[:k]

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
                return []
            max_score = max(score for _, score in docs)
            if max_score == 0:
                return [(doc, 0.0) for doc, _ in docs]
            return [(doc, score/max_score) for doc, score in docs]

        semantic_normalized = normalize_scores(semantic_docs)
        keyword_normalized = normalize_scores(keyword_docs)

        # 合并分数
        doc_scores = {}
        semantic_weight = 1.0 - keyword_weight

        for doc, score in semantic_normalized:
            doc_id = id(doc)
            doc_scores[doc_id] = {
                'doc': doc,
                'score': score * semantic_weight
            }

        for doc, score in keyword_normalized:
            doc_id = id(doc)
            if doc_id in doc_scores:
                doc_scores[doc_id]['score'] += score * keyword_weight
            else:
                doc_scores[doc_id] = {
                    'doc': doc,
                    'score': score * keyword_weight
                }

        # 按最终分数排序
        ranked = sorted(doc_scores.values(), key=lambda x: x['score'], reverse=True)

        return [item['doc'] for item in ranked]


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


class RerankerSimple:
    """简单的重排序器"""

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


def optimize_rag_pipeline_example():
    """
    RAG优化流程示例

    展示如何使用上述优化技术
    """
    logger.info("=== RAG优化示例 ===")

    # 示例：使用混合检索
    print("""
    使用方法示例：

    1. 在 rag_system.py 中集成混合检索：

    from advanced_optimizations import AdvancedRetriever, QueryExpander, RerankerSimple

    # 在 RAGSystem.setup_qa_chain 方法中
    def setup_qa_chain(self):
        # 创建高级检索器
        advanced_retriever = AdvancedRetriever(self.vectorstore, k=10)

        # 使用混合检索
        def custom_retriever(query):
            # 1. 查询扩展
            expanded_queries = QueryExpander.expand_query(query)

            # 2. 对每个扩展查询进行检索
            all_docs = []
            for exp_query in expanded_queries:
                docs = advanced_retriever.hybrid_search(exp_query)
                all_docs.extend(docs)

            # 3. 去重
            unique_docs = list({id(d): d for d in all_docs}.values())

            # 4. 重排序
            reranked_docs = RerankerSimple.rerank_by_question_similarity(
                unique_docs, query, top_k=5
            )

            return reranked_docs

        # 使用自定义检索器创建QA链
        # ... 其余代码

    2. 或者，在 pipeline.py 中修改 answer_question 方法直接使用
    """)


if __name__ == "__main__":
    optimize_rag_pipeline_example()
