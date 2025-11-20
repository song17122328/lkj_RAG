"""
知识图谱构建器
功能：从文档中提取实体和关系，构建知识图谱并可视化
"""

from typing import List, Dict, Any, Tuple
import logging
import networkx as nx
import matplotlib.pyplot as plt
import spacy
from pyvis.network import Network

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class KnowledgeGraphBuilder:
    """知识图谱构建器"""
    
    def __init__(self):
        # 加载spaCy模型用于NER和关系抽取
        try:
            self.nlp = spacy.load("zh_core_web_sm")
        except:
            logger.warning("中文模型未安装，使用英文模型")
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except:
                logger.error("请安装spaCy语言模型: python -m spacy download en_core_web_sm")
                self.nlp = None
        
        self.graph = nx.DiGraph()
        self.entities = set()
        self.relations = []
        
    def extract_entities_and_relations(self, text: str) -> Tuple[List[str], List[Tuple]]:
        """从文本中提取实体和关系"""
        if not self.nlp:
            return [], []
            
        doc = self.nlp(text[:1000000])  # 限制文本长度
        
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
    
    def visualize_graph(self, output_path: str = "knowledge_graph.html"):
        """可视化知识图谱"""
        if len(self.graph.nodes) == 0:
            logger.warning("图谱为空，无法可视化")
            return
            
        # 创建交互式网络图
        net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
        
        # 添加节点和边
        for node, attrs in self.graph.nodes(data=True):
            net.add_node(node, label=node, title=f"Type: {attrs.get('label', 'Unknown')}")
        
        for edge in self.graph.edges(data=True):
            net.add_edge(edge[0], edge[1], title=edge[2].get('relation', ''))
        
        # 保存HTML文件
        net.save_graph(output_path)
        logger.info(f"知识图谱可视化已保存: {output_path}")
        
        # 同时生成静态图片
        self._save_static_graph()
    
    def _save_static_graph(self, output_path: str = "knowledge_graph.png"):
        """保存静态图片版本的知识图谱"""
        if len(self.graph.nodes) > 100:
            logger.warning("节点过多，跳过静态图生成")
            return
            
        plt.figure(figsize=(20, 15))
        pos = nx.spring_layout(self.graph, k=2, iterations=50)
        
        # 绘制节点和边
        nx.draw_networkx_nodes(self.graph, pos, node_size=500, node_color='lightblue')
        nx.draw_networkx_labels(self.graph, pos, font_size=8)
        nx.draw_networkx_edges(self.graph, pos, edge_color='gray', arrows=True, arrowsize=20)
        
        # 绘制边标签
        edge_labels = nx.get_edge_attributes(self.graph, 'relation')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=6)
        
        plt.title("Knowledge Graph")
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        logger.info(f"静态知识图谱已保存: {output_path}")

