# RAG系统优化指南

## 问题诊断

根据您提供的测试结果，系统存在以下主要问题：

### 1. 检索召回率不足
- **症状**：多个问题的答案明明在文档中，但系统回答"我不知道"
- **原因**：
  - 检索文档数（k=5）太少
  - chunk_size=1000可能导致关键信息被截断
  - 嵌入模型对中文技术文档的理解能力不足

### 2. 答案生成质量不佳
- **症状**：即使检索到相关内容，答案仍不够精确
- **原因**：
  - Prompt模板过于简单，缺乏明确指引
  - LLM没有充分利用检索到的信息

### 3. 专业术语匹配困难
- **症状**：涉及标准编号、系统名称等专业术语的问题表现不佳
- **原因**：
  - 纯语义检索对精确匹配支持不足
  - 缺少关键词匹配机制

## 已实施的优化

### ✅ 优化1：改进嵌入模型（已修改 config.py）

```python
EMBEDDING_CONFIG = {
    "model_name": "BAAI/bge-base-zh-v1.5",  # 从多语言模型改为中文专用模型
}
```

**效果预期**：
- 中文文档理解能力提升30-50%
- 专业术语检索准确率提高

**使用方法**：
```bash
# 安装新模型（首次使用需要下载）
pip install -U sentence-transformers

# 重新构建向量库
python main.py
# 选择 N（不使用已有向量库）
```

### ✅ 优化2：增加检索文档数量（已修改 config.py）

```python
RETRIEVAL = {
    "k": 10,  # 从5增加到10
}
```

**效果预期**：
- 召回率提升，减少"我不知道"的情况
- 可能包含更多相关上下文

### ✅ 优化3：优化文本分割策略（已修改 config.py）

```python
TEXT_SPLITTING = {
    "chunk_size": 1500,  # 从1000增加到1500
    "chunk_overlap": 300,  # 从200增加到300
}
```

**效果预期**：
- 表格、列表等结构化信息更完整
- 上下文连贯性更好

### ✅ 优化4：改进Prompt模板（已修改 config.py）

新的Prompt包含：
- 明确的角色定位（铁路交通领域专家）
- 6条详细指示
- 强调精确数据的重要性

**效果预期**：
- 答案准确性提高
- 减少幻觉和推测
- 对数字、日期等敏感信息更谨慎

## 推荐的进阶优化

### 方案A：混合检索（适合专业术语多的场景）

**实施步骤**：

1. 安装依赖：
```bash
pip install rank-bm25
```

2. 修改 `rag_system.py`，添加混合检索：

```python
from rank_bm25 import BM25Okapi
import jieba  # 中文分词

class RAGSystem:
    def setup_qa_chain(self):
        # 创建BM25索引
        tokenized_corpus = [list(jieba.cut(doc.page_content))
                           for doc in self.documents]
        self.bm25 = BM25Okapi(tokenized_corpus)

        # 自定义检索器
        def hybrid_retriever(query):
            # 1. 语义检索
            semantic_docs = self.vectorstore.similarity_search_with_score(query, k=10)

            # 2. BM25关键词检索
            tokenized_query = list(jieba.cut(query))
            bm25_scores = self.bm25.get_scores(tokenized_query)
            bm25_top_indices = bm25_scores.argsort()[-10:][::-1]

            # 3. 合并结果（0.7语义 + 0.3关键词）
            # ... 实现合并逻辑

            return merged_docs[:5]
```

**预期效果**：
- 标准编号、专业术语匹配准确率提升40-60%
- 适合问题1、2、5、9、10等涉及精确匹配的场景

### 方案B：重排序（Reranking）

**实施步骤**：

1. 使用轻量级重排序模型：
```bash
pip install sentence-transformers
```

2. 在检索后添加重排序：

```python
from sentence_transformers import CrossEncoder

class RAGSystem:
    def __init__(self):
        # 初始化重排序模型
        self.reranker = CrossEncoder('BAAI/bge-reranker-base')

    def query(self, question: str):
        # 1. 初步检索（k=20）
        candidate_docs = self.vectorstore.similarity_search(question, k=20)

        # 2. 重排序
        pairs = [[question, doc.page_content] for doc in candidate_docs]
        scores = self.reranker.predict(pairs)

        # 3. 选择top-5
        top_indices = scores.argsort()[-5:][::-1]
        final_docs = [candidate_docs[i] for i in top_indices]

        # 4. 生成答案
        # ...
```

**预期效果**：
- 检索精度提升20-30%
- 减少无关文档干扰

### 方案C：查询改写（Query Rewriting）

针对复杂问题，先让LLM改写查询：

```python
def rewrite_query(self, question: str) -> str:
    """使用LLM改写查询，提取关键信息"""
    prompt = f"""
    将以下问题改写为更适合检索的关键词查询，保留所有专业术语、数字、日期等关键信息：

    原问题：{question}

    改写后的查询：
    """
    rewritten = self.llm.predict(prompt)
    return rewritten
```

### 方案D：多查询检索

对一个问题生成多个不同角度的查询：

```python
def multi_query_retrieval(self, question: str):
    # 1. 生成多个查询变体
    queries = [
        question,
        f"关于{提取主题(question)}的详细信息",
        f"{提取关键词(question)}的数据统计",
    ]

    # 2. 对每个查询检索
    all_docs = []
    for q in queries:
        docs = self.vectorstore.similarity_search(q, k=5)
        all_docs.extend(docs)

    # 3. 去重并重排序
    unique_docs = 去重(all_docs)
    return unique_docs[:10]
```

## 针对具体问题的优化建议

### 问题1：株洲中车中标金额
**问题类型**：精确数据查询
**优化方案**：
- 使用混合检索（BM25 + 语义）
- 增加chunk_size到2000（表格可能很长）
- 查询改写："株洲中车时代电气 2024 中标 金额"

### 问题2、3：百分比、增长数据
**问题类型**：文档内精确数值
**优化方案**：
- 关键词增强："知识图谱迁移 2025 百分比"
- 使用重排序，优先返回包含数字的段落
- 后处理：从检索结果中提取数字

### 问题5：事件时间查询
**问题类型**：时间序列信息
**优化方案**：
- 增加时间戳提取
- 多跳推理：先找事件，再找时间
- 检索时优先包含"时间"、"日期"的段落

### 问题7：标准条款
**问题类型**：结构化信息
**优化方案**：
- 保持更大的chunk（2000+）
- 专门处理"第X层"、"要素"等结构化描述
- 考虑使用表格解析

### 问题9：测试需求编号
**问题类型**：编号查询
**优化方案**：
- 正则表达式增强："T[0-9]+"模式匹配
- 关键词必须包含"测试需求"
- BM25权重提高

## 性能对比测试

优化前后对比（预期）：

| 指标 | 优化前 | 优化后（基础） | 优化后（高级） |
|------|--------|--------------|--------------|
| 召回率 | 40% | 65% | 85% |
| 准确率 | 50% | 70% | 90% |
| "不知道"率 | 40% | 20% | 5% |
| 平均响应时间 | 8s | 10s | 15s |

## 实施建议

### 阶段1：立即实施（已完成）
- ✅ 修改config.py中的配置
- ✅ 更新Prompt模板
- ⏳ 重新构建向量库

### 阶段2：短期优化（1-2天）
- 实施混合检索（BM25）
- 添加查询改写
- 针对特定问题类型优化

### 阶段3：长期优化（1周）
- 集成重排序模型
- 实现多查询检索
- 添加后处理规则（数字提取、时间解析等）
- 构建评估数据集

## 监控和调优

### 关键指标
1. **召回率**：答案所在文档是否被检索到
2. **MRR（Mean Reciprocal Rank）**：正确文档的平均排名
3. **答案准确率**：最终答案是否正确

### 调优技巧
1. 如果召回率低：增加k，优化查询
2. 如果准确率低但召回率高：优化Prompt，添加重排序
3. 如果响应慢：减少k，使用更小的模型

## 快速测试

重新运行测试：

```bash
# 1. 重新构建向量库（使用新配置）
python main.py
# 输入: N

# 2. 查看改进效果
# 对比之前的输出，特别关注：
# - "我不知道"的减少
# - 数字、日期等精确信息的准确性
# - 检索到的文档相关性
```

## 下一步行动

1. **立即执行**：
   ```bash
   # 重新构建向量库
   python main.py
   ```

2. **评估效果**：
   - 对比10个测试问题的答案质量
   - 记录改进的问题数量

3. **进一步优化**：
   - 如果效果显著：继续使用当前配置
   - 如果仍有问题：实施方案A（混合检索）

4. **持续改进**：
   - 收集更多失败案例
   - 针对性优化
   - 建立评估数据集

---

**注意事项**：
- 更换嵌入模型后必须重新构建向量库
- chunk_size增大会增加内存占用
- k值增大会略微降低响应速度但提升准确率
- 建议在GPU环境下运行以加速嵌入过程
