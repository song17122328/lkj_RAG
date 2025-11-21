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
        """使用LLM智能提取文件名（强化版）"""
        if not self.llm:
            return []

        try:
            # 使用更严格的prompt，要求只输出文件名
            prompt = f"""仅输出问题中提到的文件/文档/报告/标准的名称。
一行一个名称，不要编号，不要解释，不要总结。
如果没有提到任何文件，输出"无"。

问题：{query}

输出："""

            # 调用LLM
            try:
                if hasattr(self.llm, 'invoke'):
                    response = self.llm.invoke(prompt)
                    llm_output = response.content if hasattr(response, 'content') else str(response)
                else:
                    llm_output = self.llm(prompt)
            except:
                return []

            # 清理输出：移除思考标签和代码块
            llm_output = re.sub(r'<think>.*?</think>', '', llm_output, flags=re.DOTALL | re.IGNORECASE)
            llm_output = re.sub(r'</?think>', '', llm_output, flags=re.IGNORECASE)
            llm_output = llm_output.replace('```', '').strip()

            # 严格过滤：识别并排除句子特征
            file_names = []
            thinking_keywords = ['总结', '思路', '我', '需要', '可能', '应该', '首先', '接下来', '最后',
                                '确定', '找到', '整理', '分析', '因此', '所以', '然后', '包括']

            for line in llm_output.split('\n'):
                line = re.sub(r'^[\d\.\-\*\s]+', '', line).strip()  # 移除序号

                # 跳过空行和无意义词
                if not line or line in ['无', '没有', 'None', '输出：']:
                    continue

                # 严格过滤句子特征
                # 1. 包含冒号且后面有字（"包括："这种）
                if '：' in line and len(line) > line.index('：') + 1:
                    continue

                # 2. 包含多个逗号或句号（完整句子特征）
                if line.count('，') >= 2 or line.count('。') >= 1:
                    continue

                # 3. 包含思考关键词
                if any(kw in line for kw in thinking_keywords):
                    continue

                # 4. 以"的"结尾但没有其他文件特征（"我的思路"）
                if line.endswith('的') and len(line) < 10:
                    continue

                # 5. 过长（超过50字符）
                if len(line) > 50:
                    continue

                file_names.append(line)

            logger.info(f"LLM提取: {file_names}")
            return file_names[:3]  # 最多3个，避免噪音

        except Exception as e:
            logger.warning(f"LLM提取失败: {e}")
            return []

    def _extract_file_names_regex(self, query: str) -> List[str]:
        """使用正则提取文件名（增强版 - 包含组织名称）"""
        file_names = []

        # 1. 标准编号（最重要）
        for pattern in [r'(IEEE\s*[\d.]+)', r'(GB/T\s*\d+)', r'(ISO\s*\d+)', r'(IEC\s*\d+)', r'(SUBSET[-\s]*\d+)']:
            file_names.extend(re.findall(pattern, query, re.IGNORECASE))

        # 2. 书名号内容
        file_names.extend(re.findall(r'《([^》]{3,50})》', query))

        # 3. 关键组织/机构名称（新增）
        org_patterns = [
            r'(UIC)',  # 国际铁路联盟
            r'(欧洲铁路局)',
            r'(ERA)',
            r'(株洲中车[\u4e00-\u9fa5]{2,20}公司)',  # 株洲中车相关公司
            r'(中车[\u4e00-\u9fa5]{2,20})',  # 中车系列
            r'([^\s，。]{2,8}地铁)',  # XX地铁
            r'([^\s，。]{2,6}车站)',  # XX车站
        ]
        for pattern in org_patterns:
            matches = re.findall(pattern, query, re.IGNORECASE)
            file_names.extend(matches)

        # 4. "在...报告"模式
        file_names.extend(re.findall(r'在(.{3,25}?)(?:报告|文档|文件)(?:里|中)', query))
        file_names.extend(re.findall(r'根据(.{3,25}?)(?:报告|文档|文件)', query))

        # 5. 年份_英文名或年份-年份
        file_names.extend(re.findall(r'(\d{4}[_-][A-Za-z][\w\-\s]{5,35})', query))
        file_names.extend(re.findall(r'(\d{4}[-–—]\d{4})', query))  # 2025-2027

        # 清理并去重
        cleaned = []
        seen = set()
        for name in file_names:
            name = name.strip()
            if len(name) >= 2 and name.lower() not in seen:
                cleaned.append(name)
                seen.add(name.lower())

        return cleaned

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

    def _apply_alias_mapping(self, name: str) -> List[str]:
        """应用别名映射，返回可能的匹配名称列表"""
        # 常见组织/标准的中英文别名映射
        alias_map = {
            'uic': ['uic', '国际铁路联盟', 'union internationale', 'international union'],
            '欧洲铁路局': ['era', 'european railway agency', 'european union agency', 'spd', 'single programming'],
            '株洲中车时代电气': ['中车时代', 'crrc', '时代电气', 'zhuzhou'],
            '南京地铁': ['南京', 'nanjing', 'metro'],
            'ieee': ['ieee', '电气电子工程师学会'],
            'subset': ['subset', 'ertms', 'etcs'],
            'gb/t': ['gbt', 'gb', '国标', '国家标准'],
            'cbtc': ['cbtc', '基于通信的列车控制', 'communication based train control'],
            'manresa': ['manresa', '曼雷萨'],
            'ato': ['ato', '列车自动运行', 'automatic train operation'],
        }

        name_lower = name.lower()
        results = [name]  # 始终包含原始名称

        # 查找匹配的别名组
        for key, aliases in alias_map.items():
            if key in name_lower or any(alias in name_lower for alias in aliases):
                results.extend(aliases)
                break

        return list(set(results))  # 去重

    def _fuzzy_match(self, name: str, source: str) -> bool:
        """模糊匹配文件名和source路径（增强版 - 支持别名）"""
        from difflib import SequenceMatcher
        import os

        name_lower = name.lower()
        source_lower = source.lower()
        source_file = os.path.basename(source_lower)

        # 应用别名映射
        possible_names = self._apply_alias_mapping(name)

        for test_name in possible_names:
            test_name_lower = test_name.lower()

            # 1. 直接包含（全路径或文件名）
            if test_name_lower in source_lower or test_name_lower in source_file:
                return True

            # 2. 反向包含（文件名中的一部分在提取的名称中）
            if len(test_name_lower) >= 3:
                # 分割成token进行匹配
                test_tokens = re.findall(r'[\w]+', test_name_lower)
                source_tokens = re.findall(r'[\w]+', source_file)

                for token in test_tokens:
                    if len(token) >= 3 and any(token in st for st in source_tokens):
                        return True

        # 3. 分词匹配 - 提取关键词
        stop_words = {'的', '报告', '文件', '文档', '标准', '年', '号线', 'document', 'report', 'file', 'the', 'a', 'an'}
        name_words = set(re.findall(r'[\w]+', name_lower)) - stop_words
        source_words = set(re.findall(r'[\w]+', source_file)) - stop_words

        # 如果提取的名称关键词在文件名中（至少1个长关键词或2个短关键词）
        if name_words and source_words:
            matched_words = name_words & source_words
            long_matches = [w for w in matched_words if len(w) >= 4]
            if long_matches or len(matched_words) >= 2:
                return True

        # 4. 移除特殊字符后匹配
        clean_name = re.sub(r'[\s_\-—年]+', '', name_lower)
        clean_source = re.sub(r'[\s_\-—]+', '', source_file)
        if len(clean_name) >= 4 and clean_name in clean_source:
            return True

        # 5. 序列相似度匹配（使用difflib）
        if len(name) >= 5 and len(source_file) >= 5:
            threshold = 0.5 if len(clean_name) >= 10 else 0.6
            ratio = SequenceMatcher(None, clean_name, clean_source).ratio()
            if ratio >= threshold:
                return True

        return False

    def _boost_file_name_matches(self, query: str, docs: List[Document]) -> List[Document]:
        """根据文件名匹配提升文档优先级（简化版）"""
        if not docs:
            return docs

        extracted_names = self._extract_file_names(query)
        if not extracted_names:
            print("  [文件名提取] 未提取到文件名")
            return docs

        # 显示提取的文件名
        print(f"\n{'='*60}")
        print(f"[文件名提取] 提取到 {len(extracted_names)} 个:")
        for i, name in enumerate(extracted_names, 1):
            print(f"  {i}. {name[:45] if len(name) > 45 else name}")

        # 匹配文档
        import os
        all_sources = {doc.metadata.get('source', '') for doc in docs if doc.metadata.get('source')}
        matched_sources = set()

        # 调试：显示候选文件（仅显示前5个）
        if logger.isEnabledFor(logging.DEBUG):
            print(f"\n[调试] 候选文件（共{len(all_sources)}个，显示前5个）:")
            for i, source in enumerate(list(all_sources)[:5], 1):
                print(f"  {i}. {os.path.basename(source)[:50]}")

        print(f"\n[文件验证] 匹配结果:")
        for name in extracted_names:
            matches = []
            for source in all_sources:
                if self._fuzzy_match(name, source):
                    matched_sources.add(source)
                    matches.append(os.path.basename(source))

            if matches:
                # 只显示第一个匹配，如果有多个则显示数量
                first_match = matches[0][:35]
                if len(matches) > 1:
                    print(f"  ✓ '{name[:30]}...' -> {first_match} (+{len(matches)-1}个)")
                else:
                    print(f"  ✓ '{name[:30]}...' -> {first_match}")
            else:
                print(f"  ✗ '{name[:30]}...'")

        # 文档排序
        matched_docs = [d for d in docs if d.metadata.get('source') in matched_sources]
        unmatched_docs = [d for d in docs if d.metadata.get('source') not in matched_sources]

        print(f"\n[匹配] {len(matched_docs)}/{len(docs)} 个文档")
        print(f"{'='*60}\n")

        return (matched_docs + unmatched_docs) if matched_docs else docs

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

        # 添加同义词（这里简化处理，实际应使用词库）
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
    """重排序器，基于关键词重叠"""

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
        # 简单的相似度计算：基于关键词重叠（Jaccard相似度）
        question_words = set(question.lower().split())

        scored_docs = []
        for doc in documents:
            doc_words = set(doc.page_content.lower().split())
            intersection = len(question_words & doc_words)
            union = len(question_words | doc_words)
            similarity = intersection / union if union > 0 else 0
            scored_docs.append((doc, similarity))

        # 排序并返回
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in scored_docs[:top_k]]


