"""
RAG系统配置文件
可根据需求调整各项参数
"""
from pathlib import Path

# ==================== 模型配置 ====================

# LLM模型选择
LLM_CONFIG = {
    "provider": "vllm",  # "openai", "local", "huggingface", "vllm", "ollama"
    "model_name": "gpt-3.5-turbo",  # OpenAI模型名称（vLLM会使用实际部署的模型）
    "temperature": 0.0,  # 生成温度（0-1）
    "max_tokens": 2048,  # 最大生成token数
    "api_key": None,  # OpenAI API密钥（或设置环境变量OPENAI_API_KEY）
    # vLLM配置
    "vllm": {
        "base_url": "http://127.0.0.1:8910/v1",  # vLLM服务地址
        "model": "DeepSeek-R1-Distill-Qwen-14B",  # 模型名称（如果为None，将从服务自动获取）
        "api_key": "EMPTY",  # vLLM通常不需要真实的API key，但需要提供
        "max_tokens": 2048,  # 最大生成token数
        "temperature": 0.0,  # 温度参数
    },
    # Ollama配置
    "ollama": {
        "base_url": "http://127.0.0.1:11434",  # Ollama服务地址
        "model": "llama3",  # Ollama模型名称
        "streaming": False,  # 是否流式输出
    },
    # OpenAI配置
    "openai": {
        "api_key": None,  # OpenAI API密钥（或设置环境变量OPENAI_API_KEY）
        "model": "gpt-3.5-turbo",  # OpenAI模型名称
        "temperature": 0.0,  # 生成温度（0-1）
        "max_tokens": 2000,  # 最大生成token数
    },
}

# 嵌入模型配置
EMBEDDING_CONFIG = {
    "provider": "local",  # "openai", "local"
    # 多语言模型推荐（支持中文+英文+德文等100+语言）：
    "model_name": "BAAI/bge-m3",  # 推荐：BGE多语言模型，效果最佳
    # "model_name": "intfloat/multilingual-e5-large",  # 备选：E5多语言大模型
    # "model_name": "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",  # 备选：MPNet多语言
    # "model_name": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",  # 原模型（较小）
    # 纯中文模型（仅当文档全为中文时使用）：
    # "model_name": "BAAI/bge-base-zh-v1.5",  # 中文专用
    "device": "cuda",  # 强烈建议使用 GPU 加速（bge-m3需要GPU以发挥最佳性能）
    "batch_size": 32,
    "normalize": True,
}

# ==================== 文档处理配置 ====================

# 文本分割配置
TEXT_SPLITTING = {
    "chunk_size": 800,  # 块大小（字符数）- P2优化：增加到800以减少关键句子被分割的概率
    "chunk_overlap": 200,  # 块重叠（字符数）- P2优化：增加到200确保上下文连续性
    "separators": ["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""],
    "length_function": len,
}

# 文档增强配置（表格提取、数值标注、地理标注）
DOCUMENT_ENHANCEMENT = {
    "enabled": True,  # 是否启用文档增强功能

    # 表格提取配置
    "table_extraction": {
        "enabled": True,  # 是否提取表格
        "min_rows": 2,  # 最小行数（包含表头）
        "min_cols": 2,  # 最小列数
        "max_rows_to_describe": 50,  # 最多描述的行数（避免chunk过大）
    },

    # 数值数据增强配置
    "numerical_enrichment": {
        "enabled": True,  # 是否标注数值数据
        "extract_types": [  # 提取的数值类型
            "percentage",  # 百分比
            "currency",  # 货币
            "distance",  # 距离/里程
            "time",  # 时间
            "count",  # 数量
            "ratio",  # 比率/倍数
        ],
        "add_summary": True,  # 是否在chunk前添加数值摘要
    },

    # 地理信息标注配置
    "geographical_tagging": {
        "enabled": True,  # 是否标注地理信息
        "use_spacy": True,  # 是否使用spaCy NER（需要已安装spaCy）
        "extract_provinces": True,  # 提取省份信息
        "extract_cities": True,  # 提取城市信息
        "identify_scope": True,  # 识别地理范围（国家/省级/市级）
    },
}

# ==================== 知识图谱配置 ====================

KNOWLEDGE_GRAPH = {
    "enabled": True,  # 是否启用知识图谱
    "spacy_model": "en_core_web_sm",  # spaCy语言模型
    "max_entities_per_doc": 100,  # 每个文档最大实体数
    "min_entity_frequency": 2,  # 最小实体频率
    "relation_extraction": True,  # 是否提取关系
    "visualization": {
        "enabled": True,
        "interactive": True,  # 生成交互式HTML
        "static": True,  # 生成静态图片
        "max_nodes_static": 100,  # 静态图最大节点数
        "layout": "spring",  # 图布局算法
    }
}

# ==================== 向量数据库配置 ====================

VECTOR_STORE = {
    "type": "chroma",  # "chroma", "faiss", "milvus"
    "persist_directory": "./vectorstore",
    "collection_name": "rag_documents",
    "distance_metric": "cosine",  # "cosine", "l2", "ip"
}

# ==================== 检索配置 ====================

RETRIEVAL = {
    "search_type": "mmr",  # 使用 MMR (Maximum Marginal Relevance) 平衡相关性和多样性
    "k": 10,  # 返回的文档数 - P1优化：增加到10个以提升数值推理问题的召回率
    "score_threshold": 0.5,  # 相似度阈值 - 提高到0.5，只保留高相关文档
    "fetch_k": 50,  # MMR的初始获取数 - P1优化：增加到50个候选，显著提高召回率
    "lambda_mult": 0.6,  # MMR的相关性参数 - P1优化：降至0.6更注重多样性，召回不同角度的信息
}

# ==================== 问答链配置 ====================

QA_CHAIN = {
    "chain_type": "stuff",  # "stuff", "map_reduce", "refine", "map_rerank"
    "return_source_documents": True,
    "verbose": False,
    "max_tokens_limit": 4000,  # 上下文最大token限制
}

# ==================== 提示词模板 ====================

PROMPTS = {
    "qa_template": """你是一个专业的铁路交通领域技术助手。请基于以下上下文信息回答问题。

**重要指示：**
1. **信息提取**：仔细阅读上下文中的所有信息，包括表格、数据、图表描述和技术细节
2. **数值推理**：
   - 对于涉及计算的问题（如百分比、增长率、排名等），必须进行数学推理
   - 从多个上下文片段中综合信息（例如：当前值在A段，目标值在B段）
   - 明确展示计算过程，例如："当前8%，需增长40%，则目标为8%×(1+40%)=11.2%"
3. **表格/图表理解**：
   - 如果上下文包含表格或图表的文本描述，仔细提取其中的数据
   - 对于排名类问题，需要对数值进行比较和排序
4. **精确性要求**：
   - 数字、日期、时间、编号、百分比等必须完全准确，不得近似
   - 技术术语、标准编号、系统名称等必须保持原文准确性
5. **多步推理**：如果问题需要多步骤推理，请逐步分析并给出最终答案
6. **诚实原则**：
   - 如果上下文中确实没有足够信息，明确说"根据提供的上下文信息，我无法找到该问题的准确答案"
   - 不要编造、推测或使用上下文之外的信息

上下文信息:
{context}

问题: {question}

请提供准确答案（如需计算请展示关键步骤）:""",
    
    "condense_template": """根据以下对话历史和后续问题，将后续问题重新表述为独立的问题。

对话历史:
{chat_history}

后续问题: {question}

独立问题:""",
}

# ==================== 系统配置 ====================

SYSTEM = {
    "log_level": "INFO",  # "DEBUG", "INFO", "WARNING", "ERROR"
    "cache_enabled": True,  # 是否启用缓存
    "cache_ttl": 3600,  # 缓存过期时间（秒）
    "max_workers": 4,  # 并行处理的最大工作进程数
    "timeout": 30,  # 请求超时时间（秒）
    "enable_parallel_processing": True,  # 是否启用多进程并行处理（文档加载和表格提取）
}

# ==================== 文件路径配置 ====================

PATHS = {
    "output_directory": "./processed_documents",
    "cache_directory": "./.cache",
    "log_file": "./rag_system.log",
}

# ==================== 高级功能配置 ====================

ADVANCED_FEATURES = {
    "hybrid_search": True,  # 混合搜索（BM25关键词+语义）- 推荐开启
    "hybrid_weight": 0.4,  # 关键词搜索权重（0-1）- P1优化：增加到0.4，BM25对精确词汇（如"8%"、"S7号线"）效果更好
    "reranking": True,  # Cross-Encoder重排序 - 强烈推荐开启
    "reranking_top_k": 30,  # 重排序前先检索的文档数 - P1优化：增加到30个候选
    "reranker_model": "BAAI/bge-reranker-v2-m3",  # P1优化：升级到v2多语言模型，更精准
    "reranker_threshold": 0.3,  # P1优化：新增重排序阈值，过滤低分文档（0.3表示保留相关性>30%的文档）
    "multipath_retrieval": True,  # 多路检索（文件引导+全库） - 强烈推荐开启以提升召回率
    "query_expansion": False,  # 查询扩展（可能增加延迟）
    "feedback_loop": False,  # 反馈循环
    "multi_modal": False,  # 多模态支持
}

# ==================== 导出配置函数 ====================

def get_config():
    """获取完整配置"""
    return {
        "llm": LLM_CONFIG,
        "embedding": EMBEDDING_CONFIG,
        "text_splitting": TEXT_SPLITTING,
        "knowledge_graph": KNOWLEDGE_GRAPH,
        "vector_store": VECTOR_STORE,
        "retrieval": RETRIEVAL,
        "qa_chain": QA_CHAIN,
        "prompts": PROMPTS,
        "system": SYSTEM,
        "paths": PATHS,
        "advanced": ADVANCED_FEATURES,
    }

def update_config_for_production():
    """更新配置为生产环境设置"""
    global LLM_CONFIG, EMBEDDING_CONFIG, SYSTEM
    
    # 使用更强大的模型
    LLM_CONFIG["model_name"] = "gpt-4"
    LLM_CONFIG["temperature"] = 0.0
    
    # 使用GPU
    EMBEDDING_CONFIG["device"] = "cuda"
    
    # 提高系统性能
    SYSTEM["max_workers"] = 8
    SYSTEM["cache_enabled"] = True
    
    print("✅ 配置已更新为生产环境")

def update_config_for_chinese():
    """更新配置为中文处理"""
    global KNOWLEDGE_GRAPH, EMBEDDING_CONFIG
    
    # 使用中文spaCy模型
    KNOWLEDGE_GRAPH["spacy_model"] = "zh_core_web_sm"
    
    # 使用中文嵌入模型
    EMBEDDING_CONFIG["model_name"] = "BAAI/bge-large-zh-v1.5"
    
    print("✅ 配置已更新为中文处理")

if __name__ == "__main__":
    # 打印当前配置
    import json
    config = get_config()
    print(json.dumps(config, indent=2, ensure_ascii=False))
