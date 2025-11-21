"""
知识图谱构建器
功能：从文档中提取实体和关系，构建知识图谱并可视化
支持多语言自动检测和对应模型加载
"""

from typing import List, Dict, Any, Tuple, Optional
import logging
import networkx as nx
import spacy

try:
    from langdetect import detect
except ImportError:
    logger.warning("langdetect未安装，将使用默认语言。建议安装: pip install langdetect")
    detect = None

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class KnowledgeGraphBuilder:
    """多语言知识图谱构建器（支持中文、英文、德文等）"""

    def __init__(self):
        """
        初始化知识图谱构建器，加载多个语言的spaCy模型

        支持的语言和模型：
        - 中文: zh_core_web_sm
        - 英文: en_core_web_sm
        - 德文: de_core_news_sm
        - 法文: fr_core_news_sm
        - 西班牙文: es_core_news_sm
        """
        # 语言模型映射表
        self.language_models = {
            'zh': 'zh_core_web_sm',
            'en': 'en_core_web_sm',
            'de': 'de_core_news_sm',
            'fr': 'fr_core_news_sm',
            'es': 'es_core_news_sm'
        }

        # 加载的模型缓存
        self.nlp_models = {}

        # 尝试加载常用语言模型（中文、英文）
        for lang, model_name in [('zh', 'zh_core_web_sm'), ('en', 'en_core_web_sm')]:
            try:
                self.nlp_models[lang] = spacy.load(model_name)
                logger.info(f"已加载{lang}语言模型: {model_name}")
            except:
                logger.warning(f"{lang}模型未安装: {model_name}")

        # 如果没有任何模型，尝试加载英文模型作为默认
        if not self.nlp_models:
            try:
                self.nlp_models['en'] = spacy.load("en_core_web_sm")
                logger.info("使用英文模型作为默认")
            except:
                logger.error("⚠️ 未安装任何spaCy模型！请安装:")
                logger.error("  中文: python -m spacy download zh_core_web_sm")
                logger.error("  英文: python -m spacy download en_core_web_sm")

        # 默认使用中文模型（如果有），否则使用第一个可用模型
        self.default_lang = 'zh' if 'zh' in self.nlp_models else list(self.nlp_models.keys())[0] if self.nlp_models else None

        self.graph = nx.DiGraph()
        self.entities = set()
        self.relations = []

    def _detect_language(self, text: str) -> str:
        """
        检测文本语言

        Args:
            text: 待检测的文本

        Returns:
            语言代码（'zh', 'en', 'de'等），如果检测失败返回默认语言
        """
        if not detect:
            return self.default_lang or 'en'

        try:
            # 使用langdetect检测语言
            lang = detect(text[:500])  # 只检测前500字符

            # langdetect返回的语言代码映射
            lang_map = {
                'zh-cn': 'zh',
                'zh-tw': 'zh',
                'en': 'en',
                'de': 'de',
                'fr': 'fr',
                'es': 'es'
            }

            detected_lang = lang_map.get(lang, lang)
            logger.debug(f"检测到语言: {detected_lang}")
            return detected_lang
        except Exception as e:
            logger.debug(f"语言检测失败: {e}，使用默认语言")
            return self.default_lang or 'en'

    def _get_nlp_model(self, text: str) -> Optional[spacy.language.Language]:
        """
        根据文本语言获取对应的spaCy模型

        Args:
            text: 文本内容

        Returns:
            spaCy语言模型，如果没有可用模型返回None
        """
        # 检测语言
        lang = self._detect_language(text)

        # 如果该语言模型已加载，直接返回
        if lang in self.nlp_models:
            return self.nlp_models[lang]

        # 尝试加载该语言模型
        model_name = self.language_models.get(lang)
        if model_name:
            try:
                self.nlp_models[lang] = spacy.load(model_name)
                logger.info(f"动态加载{lang}语言模型: {model_name}")
                return self.nlp_models[lang]
            except:
                logger.warning(f"无法加载{lang}模型: {model_name}")

        # 使用默认模型
        if self.default_lang and self.default_lang in self.nlp_models:
            logger.debug(f"使用默认{self.default_lang}模型处理{lang}文本")
            return self.nlp_models[self.default_lang]

        # 如果有任何可用模型，返回第一个
        if self.nlp_models:
            fallback_lang = list(self.nlp_models.keys())[0]
            logger.debug(f"使用{fallback_lang}模型作为后备")
            return self.nlp_models[fallback_lang]

        return None
        
    def extract_entities_and_relations(self, text: str) -> Tuple[List[str], List[Tuple]]:
        """
        从文本中提取实体和关系（多语言自适应）

        Args:
            text: 输入文本

        Returns:
            (entities, relations)元组
        """
        # 动态获取适合该文本语言的spaCy模型
        nlp = self._get_nlp_model(text)
        if not nlp:
            logger.warning("没有可用的spaCy模型")
            return [], []

        # 限制文本长度（避免spaCy处理超长文本）
        doc = nlp(text[:100000])  # 限制为10万字符
        
        entities = []
        relations = []
        
        # 提取命名实体
        for ent in doc.ents:
            entities.append({
                'text': ent.text,
                'label': ent.label_,
                'start': ent.start_char,
                'end': ent.end_char
            })
            self.entities.add(ent.text)
        
        # 简单的关系抽取（基于依存关系）
        for token in doc:
            if token.dep_ in ["ROOT", "prep", "agent"]:
                for child in token.children:
                    if child.dep_ in ["pobj", "dobj", "attr"]:
                        subject = token.head.text
                        relation = token.text
                        object_ = child.text
                        
                        if subject and object_:
                            relations.append((subject, relation, object_))
                            self.relations.append((subject, relation, object_))
        
        return entities, relations
    
    def build_graph_from_documents(self, documents: Dict[str, str]):
        """从文档构建知识图谱"""
        logger.info("开始构建知识图谱...")
        
        for doc_name, content in documents.items():
            if not content:
                continue
                
            logger.info(f"处理文档: {doc_name}")
            
            # 分块处理长文本
            chunks = self._split_text(content, chunk_size=5000)
            
            for chunk in chunks:
                entities, relations = self.extract_entities_and_relations(chunk)
                
                # 添加节点
                for entity in entities:
                    self.graph.add_node(
                        entity['text'],
                        label=entity['label'],
                        doc_source=doc_name
                    )
                
                # 添加边（关系）
                for subject, relation, object_ in relations:
                    self.graph.add_edge(
                        subject, 
                        object_,
                        relation=relation,
                        doc_source=doc_name
                    )
        
        logger.info(f"知识图谱构建完成: {len(self.graph.nodes)} 个节点, {len(self.graph.edges)} 条边")
        return self.graph
    
    def _split_text(self, text: str, chunk_size: int = 5000) -> List[str]:
        """将文本分割成chunks"""
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i+chunk_size])
        return chunks
    

