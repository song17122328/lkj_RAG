"""
地理位置标注模块

功能：
1. 从文本中提取地理位置实体（省、市、区）
2. 识别地理范围（全国、省级、市级）
3. 在metadata中添加地理标签
4. 支持地域过滤检索
"""

import re
import logging
from typing import List, Dict, Any, Set, Optional, Tuple

try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    spacy = None

logger = logging.getLogger(__name__)


class GeographicalTagger:
    """地理位置标注器"""

    def __init__(self, use_spacy: bool = True):
        """
        Args:
            use_spacy: 是否使用spaCy进行NER（需要已安装spaCy和模型）
        """
        self.use_spacy = use_spacy and SPACY_AVAILABLE
        self.nlp = None

        # 尝试加载spaCy模型
        if self.use_spacy:
            try:
                # 优先使用中文模型
                try:
                    self.nlp = spacy.load("zh_core_web_sm")
                    logger.info("使用spaCy中文模型进行地理位置提取")
                except OSError:
                    # 降级到英文模型
                    try:
                        self.nlp = spacy.load("en_core_web_sm")
                        logger.info("使用spaCy英文模型进行地理位置提取")
                    except OSError:
                        logger.warning("spaCy模型未找到，将使用基于规则的方法")
                        self.nlp = None
            except Exception as e:
                logger.warning(f"spaCy初始化失败: {e}，将使用基于规则的方法")
                self.nlp = None

        # 中国省份和直辖市列表
        self.provinces = {
            # 省份
            '北京', '天津', '上海', '重庆',  # 直辖市
            '河北', '山西', '辽宁', '吉林', '黑龙江',
            '江苏', '浙江', '安徽', '福建', '江西', '山东',
            '河南', '湖北', '湖南', '广东', '海南',
            '四川', '贵州', '云南', '陕西', '甘肃', '青海',
            '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆',
            '香港', '澳门',
        }

        # 常见城市列表（部分）
        self.cities = {
            # 直辖市
            '北京', '上海', '天津', '重庆',
            # 省会和主要城市
            '广州', '深圳', '南京', '杭州', '苏州', '武汉', '成都', '西安',
            '郑州', '长沙', '哈尔滨', '沈阳', '大连', '青岛', '济南', '石家庄',
            '太原', '呼和浩特', '长春', '南昌', '合肥', '福州', '厦门',
            '南宁', '海口', '贵阳', '昆明', '拉萨', '兰州', '西宁',
            '银川', '乌鲁木齐', '宁波', '温州', '无锡', '常州', '佛山',
            '东莞', '珠海', '中山', '惠州', '汕头', '徐州', '淮安', '盐城',
            '扬州', '南通', '泰州', '镇江', '芜湖', '绍兴', '台州', '金华',
            '嘉兴', '湖州', '洛阳', '开封', '新乡', '许昌', '株洲', '湘潭',
        }

        # 省-市映射（用于识别省级范围）
        self.province_city_map = {
            '江苏': ['南京', '苏州', '无锡', '常州', '徐州', '南通', '扬州', '盐城', '淮安', '连云港', '镇江', '泰州', '宿迁'],
            '浙江': ['杭州', '宁波', '温州', '绍兴', '湖州', '嘉兴', '金华', '台州', '丽水', '舟山', '衢州'],
            '广东': ['广州', '深圳', '东莞', '佛山', '中山', '珠海', '惠州', '汕头', '江门', '湛江', '茂名', '肇庆', '梅州', '汕尾', '河源', '阳江', '清远', '韶关', '揭阳', '云浮', '潮州'],
            '山东': ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '临沂', '德州', '聊城', '滨州', '菏泽'],
            '四川': ['成都', '绵阳', '德阳', '南充', '宜宾', '自贡', '乐山', '泸州', '达州', '内江', '遂宁', '攀枝花', '眉山', '广安', '资阳', '凉山', '广元', '雅安', '巴中', '阿坝', '甘孜'],
            '河南': ['郑州', '洛阳', '开封', '南阳', '安阳', '商丘', '新乡', '平顶山', '许昌', '焦作', '周口', '信阳', '驻马店', '濮阳', '漯河', '三门峡', '鹤壁', '济源'],
            '湖北': ['武汉', '襄阳', '宜昌', '荆州', '黄冈', '孝感', '黄石', '咸宁', '随州', '荆门', '十堰', '恩施', '鄂州', '仙桃', '潜江', '天门', '神农架'],
            '湖南': ['长沙', '株洲', '湘潭', '衡阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底', '湘西'],
            '河北': ['石家庄', '唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水'],
            '福建': ['福州', '厦门', '泉州', '漳州', '莆田', '三明', '南平', '龙岩', '宁德'],
            '安徽': ['合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '六安', '亳州', '池州', '宣城'],
        }

    def extract_geographical_info(self, text: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        提取文本中的地理信息并更新metadata

        Args:
            text: 输入文本
            metadata: 原始metadata

        Returns:
            enriched_metadata: 增强后的metadata
        """
        if metadata is None:
            metadata = {}

        # 1. 提取地理实体
        provinces, cities = self._extract_locations(text)

        if not provinces and not cities:
            # 没有地理信息，直接返回
            return metadata

        # 2. 识别地理范围
        geographic_scope = self._identify_geographic_scope(provinces, cities, text)

        # 3. 更新metadata
        enriched_metadata = metadata.copy()
        enriched_metadata.update({
            'has_geographical_info': True,
            # ChromaDB只支持基本类型，将集合转为逗号分隔字符串
            'provinces': ', '.join(sorted(provinces)),
            'cities': ', '.join(sorted(cities)),
            'geographic_scope': geographic_scope,
        })

        # 4. 添加省-市关联（用于省级范围查询）
        province_relations = self._identify_province_relations(provinces, cities)
        if province_relations:
            # 将字典转为字符串格式："省1:市1,市2; 省2:市3,市4"
            relations_str = '; '.join([f"{prov}:{','.join(cities)}"
                                       for prov, cities in province_relations.items()])
            enriched_metadata['province_city_relations'] = relations_str

        logger.debug(f"提取地理信息: 省={list(provinces)}, 市={list(cities)}, 范围={geographic_scope}")

        return enriched_metadata

    def _extract_locations(self, text: str) -> Tuple[Set[str], Set[str]]:
        """
        提取地理位置实体

        Returns:
            (provinces, cities): 省份集合和城市集合
        """
        provinces = set()
        cities = set()

        # 方法1: 使用spaCy NER
        if self.nlp:
            try:
                doc = self.nlp(text[:10000])  # 限制长度，避免处理时间过长
                for ent in doc.ents:
                    if ent.label_ in ['GPE', 'LOC']:  # GPE=地缘政治实体, LOC=位置
                        location = ent.text
                        if location in self.provinces:
                            provinces.add(location)
                        elif location in self.cities:
                            cities.add(location)
            except Exception as e:
                logger.debug(f"spaCy提取失败: {e}，使用规则方法")

        # 方法2: 基于规则的提取（作为补充或备用）
        # 提取省份
        for province in self.provinces:
            if province in text:
                provinces.add(province)

        # 提取城市
        for city in self.cities:
            if city in text:
                cities.add(city)

        # 特殊处理：江苏省、浙江省等带"省"后缀的
        province_pattern = r'([\u4e00-\u9fa5]{2,4})省'
        for match in re.finditer(province_pattern, text):
            province = match.group(1)
            if province in self.provinces:
                provinces.add(province)

        # 特殊处理：南京市、杭州市等带"市"后缀的
        city_pattern = r'([\u4e00-\u9fa5]{2,4})市'
        for match in re.finditer(city_pattern, text):
            city = match.group(1)
            if city in self.cities:
                cities.add(city)

        return provinces, cities

    def _identify_geographic_scope(self, provinces: Set[str], cities: Set[str], text: str) -> str:
        """
        识别地理范围

        Returns:
            'national' | 'provincial' | 'municipal' | 'mixed'
        """
        # 检测全国范围的关键词
        national_keywords = ['全国', '国内', '中国', '全国范围', '各省', '各市']
        has_national = any(keyword in text for keyword in national_keywords)

        # 检测省级范围的关键词
        provincial_keywords = ['省内', '全省', '本省']
        has_provincial = any(keyword in text for keyword in provincial_keywords)

        if has_national or (len(provinces) >= 3 and len(cities) >= 5):
            return 'national'
        elif has_provincial or (len(provinces) == 1 and len(cities) >= 2):
            # 单一省份 + 多个城市 = 省级范围
            return 'provincial'
        elif len(cities) == 1 and not provinces:
            return 'municipal'
        elif provinces or cities:
            return 'mixed'
        else:
            return 'unknown'

    def _identify_province_relations(self, provinces: Set[str], cities: Set[str]) -> Dict[str, List[str]]:
        """
        识别省-市关联关系

        Returns:
            {省份: [城市列表]}
        """
        relations = {}

        for province in provinces:
            if province in self.province_city_map:
                # 找出文本中提到的该省份的城市
                province_cities = []
                for city in cities:
                    if city in self.province_city_map[province]:
                        province_cities.append(city)

                if province_cities:
                    relations[province] = province_cities

        # 反向推断：从城市推断省份
        for city in cities:
            for province, city_list in self.province_city_map.items():
                if city in city_list and province not in provinces:
                    # 隐含的省份
                    if province not in relations:
                        relations[province] = []
                    if city not in relations[province]:
                        relations[province].append(city)

        return relations

    def filter_by_geography(self, documents: List[Any], target_provinces: List[str] = None,
                           target_cities: List[str] = None,
                           scope: str = None) -> List[Any]:
        """
        根据地理范围过滤文档

        Args:
            documents: 文档列表
            target_provinces: 目标省份列表
            target_cities: 目标城市列表
            scope: 目标范围（'national', 'provincial', 'municipal'）

        Returns:
            过滤后的文档列表
        """
        filtered = []

        for doc in documents:
            metadata = doc.metadata if hasattr(doc, 'metadata') else {}

            # 如果没有地理信息，保留（避免过度过滤）
            if not metadata.get('has_geographical_info'):
                filtered.append(doc)
                continue

            # 检查省份匹配
            if target_provinces:
                doc_provinces = set(metadata.get('provinces', []))
                if doc_provinces & set(target_provinces):
                    filtered.append(doc)
                    continue

            # 检查城市匹配
            if target_cities:
                doc_cities = set(metadata.get('cities', []))
                if doc_cities & set(target_cities):
                    filtered.append(doc)
                    continue

            # 检查范围匹配
            if scope:
                doc_scope = metadata.get('geographic_scope')
                if doc_scope == scope or doc_scope == 'mixed':
                    filtered.append(doc)
                    continue

        logger.debug(f"地理过滤: {len(documents)} -> {len(filtered)} 个文档")
        return filtered


class GeographicalQueryAnalyzer:
    """
    地理查询分析器

    从查询中提取地理意图
    """

    def __init__(self):
        self.tagger = GeographicalTagger()

    def analyze_query(self, query: str) -> Dict[str, Any]:
        """
        分析查询中的地理信息

        Returns:
            {
                'has_geographical_intent': bool,
                'target_provinces': [...],
                'target_cities': [...],
                'scope': 'national' | 'provincial' | 'municipal'
            }
        """
        provinces, cities = self.tagger._extract_locations(query)

        # 识别范围意图
        scope = None
        if '省内' in query or '全省' in query:
            scope = 'provincial'
        elif '市内' in query or '本市' in query:
            scope = 'municipal'
        elif '全国' in query or '国内' in query:
            scope = 'national'

        return {
            'has_geographical_intent': bool(provinces or cities or scope),
            # ChromaDB只支持基本类型，将集合转为逗号分隔字符串
            'target_provinces': ', '.join(sorted(provinces)),
            'target_cities': ', '.join(sorted(cities)),
            'scope': scope
        }
