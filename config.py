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
    "device": "cpu",  # "cuda" for GPU（建议使用GPU加速）
    "batch_size": 32,
    "normalize": True,
}

# ==================== 文档处理配置 ====================

# 文本分割配置
TEXT_SPLITTING = {
    "chunk_size": 1500,  # 块大小（字符数）- 增加以保留更多上下文
    "chunk_overlap": 300,  # 块重叠（字符数）- 增加以避免信息断裂
    "separators": ["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""],
    "length_function": len,
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
    "search_type": "similarity",  # "similarity", "mmr", "similarity_score_threshold"
    "k": 10,  # 返回的文档数 - 增加到10以提高召回率
    "score_threshold": 0.3,  # 相似度阈值 - 降低以包含更多候选
    "fetch_k": 30,  # MMR的初始获取数（仅用于mmr）- 增加候选池
    "lambda_mult": 0.5,  # MMR的多样性参数（仅用于mmr）
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
1. 仔细阅读上下文中的所有信息，包括表格、数据和技术细节
2. 如果上下文包含答案，请直接引用相关信息并给出准确答案
3. 对于涉及数字、日期、时间、编号、百分比等精确数据的问题，必须确保完全准确
4. 对于技术术语、标准编号、系统名称等，必须保持原文准确性
5. 如果上下文中确实没有足够信息回答问题，明确说"根据提供的上下文信息，我无法找到该问题的准确答案"
6. 不要编造、推测或使用上下文之外的信息
7. **请直接输出最终答案，不要展示思考过程、推理步骤或任何中间分析。不要使用<think>标签。**

上下文信息:
{context}

问题: {question}

请直接提供准确答案（不要包含思考过程）:""",
    
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
    "max_workers": 4,  # 并行处理的最大工作线程数
    "timeout": 30,  # 请求超时时间（秒）
}

# ==================== 文件路径配置 ====================

PATHS = {
    "output_directory": "./processed_documents",
    "cache_directory": "./.cache",
    "log_file": "./rag_system.log",
}

# ==================== 高级功能配置 ====================

ADVANCED_FEATURES = {
    "hybrid_search": True,  # 混合搜索（关键词+语义）- 推荐开启
    "hybrid_weight": 0.3,  # 关键词搜索权重（0-1）
    "reranking": True,  # 重排序 - 推荐开启
    "reranking_top_k": 20,  # 重排序前先检索的文档数
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
