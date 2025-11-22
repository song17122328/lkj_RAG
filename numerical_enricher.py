"""
数值数据增强模块

功能：
1. 识别文本中的各类数值数据（百分比、货币、长度、时间等）
2. 提取数值及其上下文
3. 在Document的metadata中添加数值标记
4. 在chunk前添加数值摘要，提升检索效果
"""

import re
import logging
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class NumericalEntity:
    """数值实体"""
    value: str  # 原始值（如 "8%", "30.20公里"）
    number: float  # 数值部分
    unit: str  # 单位（如 "%", "公里", "亿元"）
    context: str  # 上下文（前后20个字符）
    entity_type: str  # 类型（percentage, currency, distance, time等）
    position: int  # 在文本中的位置


class NumericalDataEnricher:
    """数值数据增强器"""

    def __init__(self):
        # 数值模式定义
        self.patterns = {
            'percentage': [
                r'(\d+\.?\d*)\s*%',  # 8%, 8.5%
                r'(\d+\.?\d*)\s*％',  # 中文百分号
                r'百分之(\d+\.?\d*)',  # 百分之八
            ],
            'currency': [
                r'(\d+\.?\d*)\s*(元|万元|亿元|美元|欧元)',  # 金额
                r'(\d+\.?\d*)\s*(USD|EUR|CNY)',
                r'\$\s*(\d+\.?\d*)',
                r'￥\s*(\d+\.?\d*)',
            ],
            'distance': [
                r'(\d+\.?\d*)\s*(公里|km|千米|米|m)',  # 距离
                r'(\d+\.?\d*)\s*(mile|miles)',
            ],
            'time': [
                r'(\d+\.?\d*)\s*(年|月|日|天|小时|分钟|秒)',  # 时间
                r'(\d{4})[年/-](\d{1,2})[月/-](\d{1,2})',  # 日期
            ],
            'count': [
                r'(\d+\.?\d*)\s*(个|条|辆|列|座|项|次)',  # 数量
            ],
            'ratio': [
                r'(\d+\.?\d*)\s*倍',  # 倍数
                r'增长\s*(\d+\.?\d*)',  # 增长率
                r'下降\s*(\d+\.?\d*)',
                r'同比\s*(\d+\.?\d*)',
            ]
        }

        # 关键词映射（用于识别数值的语义上下文）
        self.semantic_keywords = {
            'growth': ['增长', '提升', '上涨', '增加', 'grow', 'increase'],
            'decline': ['下降', '减少', '降低', 'decrease', 'decline'],
            'market_share': ['市场份额', '占比', 'market share', 'share'],
            'target': ['目标', '需要', '达到', 'target', 'goal', 'objective'],
            'current': ['当前', '现在', '目前', 'current', 'present'],
            'ranking': ['排名', '排第', '位列', 'rank', 'ranking'],
        }

    def enrich_text(self, text: str, metadata: Optional[Dict[str, Any]] = None) -> Tuple[str, Dict[str, Any]]:
        """
        增强文本的数值信息

        Args:
            text: 原始文本
            metadata: 原始metadata

        Returns:
            (enriched_text, enriched_metadata)
        """
        if metadata is None:
            metadata = {}

        # 1. 提取所有数值实体
        numerical_entities = self._extract_numerical_entities(text)

        if not numerical_entities:
            # 没有数值，直接返回
            return text, metadata

        # 2. 生成数值摘要
        numerical_summary = self._generate_numerical_summary(numerical_entities, text)

        # 3. 更新metadata
        enriched_metadata = metadata.copy()
        enriched_metadata.update({
            'contains_numerical_data': True,
            'numerical_count': len(numerical_entities),
            'numerical_types': list(set(e.entity_type for e in numerical_entities)),
            'numerical_values': [e.value for e in numerical_entities],
            'numerical_summary': numerical_summary,
        })

        # 识别语义上下文
        semantic_context = self._identify_semantic_context(text)
        if semantic_context:
            enriched_metadata['numerical_context'] = semantic_context

        # 4. 在文本前添加摘要（可选，如果摘要足够有价值）
        if numerical_summary:
            enriched_text = f"【数值摘要】{numerical_summary}\n\n{text}"
        else:
            enriched_text = text

        logger.debug(f"提取了 {len(numerical_entities)} 个数值实体: {[e.value for e in numerical_entities]}")

        return enriched_text, enriched_metadata

    def _extract_numerical_entities(self, text: str) -> List[NumericalEntity]:
        """提取文本中的所有数值实体"""
        entities = []

        for entity_type, patterns in self.patterns.items():
            for pattern in patterns:
                for match in re.finditer(pattern, text):
                    entity = self._create_numerical_entity(
                        match, entity_type, text
                    )
                    if entity:
                        entities.append(entity)

        # 按位置排序
        entities.sort(key=lambda e: e.position)

        return entities

    def _create_numerical_entity(self, match: re.Match, entity_type: str, text: str) -> Optional[NumericalEntity]:
        """从正则匹配创建数值实体"""
        try:
            # 提取数值部分
            if match.lastindex:
                # 有分组，取第一个分组
                value_str = match.group(1)
            else:
                # 无分组，取整个匹配
                value_str = match.group(0)

            # 转换为float
            try:
                number = float(value_str.replace(',', ''))
            except ValueError:
                # 如果无法转换（例如日期），使用0
                number = 0.0

            # 提取完整匹配（包含单位）
            full_value = match.group(0)

            # 提取单位
            unit = full_value.replace(value_str, '').strip()

            # 提取上下文（前后20个字符）
            start = max(0, match.start() - 20)
            end = min(len(text), match.end() + 20)
            context = text[start:end]

            return NumericalEntity(
                value=full_value,
                number=number,
                unit=unit,
                context=context,
                entity_type=entity_type,
                position=match.start()
            )
        except Exception as e:
            logger.warning(f"创建数值实体失败: {e}")
            return None

    def _generate_numerical_summary(self, entities: List[NumericalEntity], full_text: str) -> str:
        """
        生成数值摘要

        策略：
        1. 列出所有关键数值
        2. 识别数值之间的关系（如增长关系）
        """
        if not entities:
            return ""

        # 按类型分组
        by_type = {}
        for entity in entities:
            if entity.entity_type not in by_type:
                by_type[entity.entity_type] = []
            by_type[entity.entity_type].append(entity)

        summary_parts = []

        # 百分比（最重要）
        if 'percentage' in by_type:
            percentages = [e.value for e in by_type['percentage']]
            if len(percentages) <= 3:
                summary_parts.append(f"百分比数据: {', '.join(percentages)}")
            else:
                summary_parts.append(f"包含{len(percentages)}个百分比数据")

        # 货币金额
        if 'currency' in by_type:
            currencies = [e.value for e in by_type['currency']]
            if len(currencies) <= 3:
                summary_parts.append(f"金额: {', '.join(currencies)}")
            else:
                summary_parts.append(f"包含{len(currencies)}个金额数据")

        # 距离/里程
        if 'distance' in by_type:
            distances = [e.value for e in by_type['distance']]
            if len(distances) <= 3:
                summary_parts.append(f"里程: {', '.join(distances)}")

        # 如果有增长/目标相关的上下文，特别标注
        if self._contains_growth_pattern(full_text):
            summary_parts.append("涉及增长率或目标数据")

        return '; '.join(summary_parts) if summary_parts else ""

    def _identify_semantic_context(self, text: str) -> List[str]:
        """
        识别数值的语义上下文

        Returns:
            语义标签列表，如 ['growth', 'market_share', 'target']
        """
        contexts = []

        for context_type, keywords in self.semantic_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    contexts.append(context_type)
                    break  # 每个类型只标记一次

        return contexts

    def _contains_growth_pattern(self, text: str) -> bool:
        """检测是否包含增长模式"""
        growth_patterns = [
            r'增长.*?\d+\.?\d*\s*%',
            r'需要.*?增长',
            r'目标.*?\d+\.?\d*\s*%',
            r'grow.*?by.*?\d+\.?\d*\s*%',
        ]

        for pattern in growth_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True

        return False


class EnhancedDocument:
    """
    增强的Document包装器

    提供便捷的方法来访问数值信息
    """

    def __init__(self, document):
        self.document = document
        self.metadata = document.metadata if hasattr(document, 'metadata') else {}

    def has_numerical_data(self) -> bool:
        """是否包含数值数据"""
        return self.metadata.get('contains_numerical_data', False)

    def get_numerical_values(self) -> List[str]:
        """获取所有数值"""
        return self.metadata.get('numerical_values', [])

    def get_numerical_types(self) -> List[str]:
        """获取数值类型"""
        return self.metadata.get('numerical_types', [])

    def get_numerical_summary(self) -> str:
        """获取数值摘要"""
        return self.metadata.get('numerical_summary', '')

    def has_percentage_data(self) -> bool:
        """是否包含百分比数据"""
        return 'percentage' in self.get_numerical_types()

    def has_currency_data(self) -> bool:
        """是否包含货币数据"""
        return 'currency' in self.get_numerical_types()

    def get_semantic_context(self) -> List[str]:
        """获取语义上下文"""
        return self.metadata.get('numerical_context', [])

    def is_growth_related(self) -> bool:
        """是否与增长相关"""
        return 'growth' in self.get_semantic_context()

    def is_target_related(self) -> bool:
        """是否与目标相关"""
        return 'target' in self.get_semantic_context()
