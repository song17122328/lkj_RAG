"""
表格提取与增强模块

功能：
1. 从Markdown文档中识别和提取表格
2. 将表格转换为结构化数据
3. 生成表格的自然语言描述，便于语义检索
4. 为表格数据创建专门的Document对象
"""

import re
import logging
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass

try:
    from langchain.schema import Document
except ImportError:
    @dataclass
    class Document:
        page_content: str
        metadata: Optional[Dict[str, Any]] = None

logger = logging.getLogger(__name__)


class TableExtractor:
    """Markdown表格提取器"""

    def __init__(self, min_rows: int = 2, min_cols: int = 2):
        """
        Args:
            min_rows: 最小行数（包含表头）
            min_cols: 最小列数
        """
        self.min_rows = min_rows
        self.min_cols = min_cols

    def extract_tables_from_markdown(self, markdown_text: str, source: str = "") -> List[Document]:
        """
        从Markdown文本中提取所有表格并转换为Document对象

        Args:
            markdown_text: Markdown格式的文本
            source: 文档来源（文件名）

        Returns:
            包含表格数据的Document列表
        """
        tables = []
        table_id = 0

        # 分割文本为行
        lines = markdown_text.split('\n')

        i = 0
        while i < len(lines):
            # 检测表格开始（Markdown表格以 | 开头）
            if self._is_table_row(lines[i]):
                # 提取完整表格
                table_lines, end_idx = self._extract_table_lines(lines, i)

                if len(table_lines) >= self.min_rows:
                    # 解析表格
                    parsed_table = self._parse_table(table_lines)

                    if parsed_table and len(parsed_table['headers']) >= self.min_cols:
                        # 创建表格Document
                        table_doc = self._create_table_document(
                            parsed_table,
                            source,
                            table_id
                        )
                        tables.append(table_doc)
                        table_id += 1
                        logger.info(f"提取表格 {table_id} from {source}: "
                                   f"{len(parsed_table['rows'])}行 × {len(parsed_table['headers'])}列")

                i = end_idx
            else:
                i += 1

        logger.info(f"从 {source} 中提取了 {len(tables)} 个表格")
        return tables

    def _is_table_row(self, line: str) -> bool:
        """判断是否为表格行"""
        stripped = line.strip()
        # Markdown表格行以 | 开头和结尾，并且包含至少2个 |
        return (stripped.startswith('|') and
                stripped.endswith('|') and
                stripped.count('|') >= 3)

    def _extract_table_lines(self, lines: List[str], start_idx: int) -> Tuple[List[str], int]:
        """
        提取完整的表格行

        Returns:
            (table_lines, end_idx): 表格行列表和结束索引
        """
        table_lines = []
        idx = start_idx

        while idx < len(lines) and self._is_table_row(lines[idx]):
            table_lines.append(lines[idx])
            idx += 1

        return table_lines, idx

    def _parse_table(self, table_lines: List[str]) -> Optional[Dict[str, Any]]:
        """
        解析表格行为结构化数据

        Returns:
            {
                'headers': [...],
                'rows': [[...], [...], ...]
            }
        """
        if len(table_lines) < 2:
            return None

        # 第一行是表头
        headers = self._parse_row(table_lines[0])

        # 第二行通常是分隔符（|---|---|），跳过
        separator_idx = 1
        if len(table_lines) > 1 and self._is_separator_row(table_lines[1]):
            separator_idx = 2
        else:
            separator_idx = 1

        # 剩余的是数据行
        rows = []
        for line in table_lines[separator_idx:]:
            if not self._is_separator_row(line):
                row = self._parse_row(line)
                if row:
                    rows.append(row)

        return {
            'headers': headers,
            'rows': rows
        }

    def _is_separator_row(self, line: str) -> bool:
        """判断是否为表格分隔符行（|---|---|）"""
        # 分隔符行主要包含 - 和 |
        stripped = line.strip()
        return bool(re.match(r'^\|[\s\-:|]+\|$', stripped))

    def _parse_row(self, line: str) -> List[str]:
        """解析单行表格数据"""
        # 移除首尾的 |
        stripped = line.strip()
        if stripped.startswith('|'):
            stripped = stripped[1:]
        if stripped.endswith('|'):
            stripped = stripped[:-1]

        # 分割单元格
        cells = [cell.strip() for cell in stripped.split('|')]
        return cells

    def _create_table_document(self, parsed_table: Dict[str, Any],
                               source: str, table_id: int) -> Document:
        """
        将解析后的表格转换为Document对象

        策略：
        1. page_content: 包含表格的自然语言描述
        2. metadata: 包含表格元数据和原始数据
        """
        headers = parsed_table['headers']
        rows = parsed_table['rows']

        # 生成自然语言描述
        natural_language_desc = self._generate_natural_language_description(
            headers, rows, source, table_id
        )

        # 创建metadata
        metadata = {
            'source': source,
            'content_type': 'table',
            'table_id': table_id,
            'column_count': len(headers),
            'row_count': len(rows),
            'headers': headers,
            'table_summary': self._generate_table_summary(headers, rows),
            # 存储表格数据的JSON表示（用于精确查询）
            'table_data': {
                'headers': headers,
                'rows': rows
            }
        }

        return Document(
            page_content=natural_language_desc,
            metadata=metadata
        )

    def _generate_natural_language_description(self, headers: List[str],
                                               rows: List[List[str]],
                                               source: str,
                                               table_id: int) -> str:
        """
        生成表格的自然语言描述

        策略：
        1. 表格概述
        2. 每行数据的自然语言转换
        3. 关键统计信息
        """
        descriptions = []

        # 1. 表格概述
        descriptions.append(f"【表格{table_id}】来源：{source}")
        descriptions.append(f"本表格包含 {len(rows)} 行数据，列名为：{', '.join(headers)}。")
        descriptions.append("")

        # 2. 转换每行数据为自然语言
        # 限制行数，避免chunk过大
        max_rows_to_describe = min(50, len(rows))

        for i, row in enumerate(rows[:max_rows_to_describe]):
            row_desc = self._row_to_natural_language(headers, row)
            if row_desc:
                descriptions.append(row_desc)

        if len(rows) > max_rows_to_describe:
            descriptions.append(f"... (省略{len(rows) - max_rows_to_describe}行)")

        return '\n'.join(descriptions)

    def _row_to_natural_language(self, headers: List[str], row: List[str]) -> str:
        """
        将单行数据转换为自然语言

        例如：
        headers: ['城市', '线路', '里程']
        row: ['南京', 'S7号线', '30.20']
        输出: "南京市S7号线运营里程为30.20公里。"
        """
        # 确保row和headers长度一致
        if len(row) != len(headers):
            # 补齐或截断
            if len(row) < len(headers):
                row = row + [''] * (len(headers) - len(row))
            else:
                row = row[:len(headers)]

        # 过滤掉空值
        non_empty_pairs = [(h, v) for h, v in zip(headers, row) if v.strip()]

        if not non_empty_pairs:
            return ""

        # 构建自然语言句子
        # 策略：第一个字段作为主语，其他字段作为属性
        if len(non_empty_pairs) == 0:
            return ""

        # 主语（第一列）
        subject = non_empty_pairs[0][1]

        # 属性
        attributes = []
        for header, value in non_empty_pairs[1:]:
            attributes.append(f"{header}为{value}")

        if attributes:
            return f"{subject}的{', '.join(attributes)}。"
        else:
            return f"{subject}。"

    def _generate_table_summary(self, headers: List[str], rows: List[List[str]]) -> str:
        """
        生成表格的概要描述

        用于元数据索引和快速理解表格内容
        """
        # 提取关键信息
        # 1. 主题（从表头推断）
        topic_keywords = self._extract_topic_keywords(headers)

        # 2. 数据范围（从第一列提取）
        entities = []
        if rows:
            for row in rows[:10]:  # 只看前10行
                if row:
                    entities.append(row[0])

        entities_str = ', '.join(set(entities[:5]))  # 去重，取前5个

        summary = f"包含{len(rows)}条记录的{topic_keywords}数据表，涉及：{entities_str}等。"
        return summary

    def _extract_topic_keywords(self, headers: List[str]) -> str:
        """从表头提取主题关键词"""
        # 常见的主题关键词映射
        topic_map = {
            ('城市', '线路', '里程'): '城市轨道交通运营',
            ('企业', '中标', '金额'): '企业中标',
            ('序号', '城市', '制式'): '城轨交通制式',
            ('线路', '运营', '时间'): '线路运营',
        }

        headers_tuple = tuple(headers[:3])  # 取前3个表头

        for key, topic in topic_map.items():
            if all(k in ' '.join(headers) for k in key):
                return topic

        # 默认返回表头组合
        return '+'.join(headers[:2]) if len(headers) >= 2 else '数据'


class TableAwareTextSplitter:
    """
    表格感知的文本分割器

    功能：
    1. 识别文本中的表格位置
    2. 确保表格不被分割
    3. 为非表格文本正常分割
    """

    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.table_extractor = TableExtractor()

    def split_text_with_tables(self, text: str, source: str = "") -> Tuple[List[str], List[Document]]:
        """
        分割文本，同时提取表格

        Returns:
            (text_chunks, table_documents): 文本chunks和表格Documents
        """
        # 1. 提取所有表格
        table_documents = self.table_extractor.extract_tables_from_markdown(text, source)

        # 2. 标记表格位置并移除
        text_without_tables, table_markers = self._remove_tables_with_markers(text)

        # 3. 分割非表格文本
        text_chunks = self._split_text(text_without_tables)

        logger.info(f"文本分割完成: {len(text_chunks)}个文本chunks + {len(table_documents)}个表格")

        return text_chunks, table_documents

    def _remove_tables_with_markers(self, text: str) -> Tuple[str, List[Tuple[int, int]]]:
        """
        移除文本中的表格，并用占位符标记

        Returns:
            (text_without_tables, table_markers)
        """
        lines = text.split('\n')
        result_lines = []
        table_markers = []

        i = 0
        table_count = 0
        while i < len(lines):
            if self.table_extractor._is_table_row(lines[i]):
                # 找到表格
                table_lines, end_idx = self.table_extractor._extract_table_lines(lines, i)

                # 添加占位符
                marker = f"[TABLE_{table_count}]"
                result_lines.append(marker)
                table_markers.append((i, end_idx))
                table_count += 1

                i = end_idx
            else:
                result_lines.append(lines[i])
                i += 1

        return '\n'.join(result_lines), table_markers

    def _split_text(self, text: str) -> List[str]:
        """
        简单的文本分割（基于字符数）
        """
        chunks = []
        text_length = len(text)

        start = 0
        while start < text_length:
            end = start + self.chunk_size

            # 如果不是最后一个chunk，尝试在段落边界分割
            if end < text_length:
                # 查找最近的段落边界
                boundary = text.rfind('\n\n', start, end)
                if boundary > start:
                    end = boundary
                else:
                    # 查找最近的句号
                    boundary = text.rfind('。', start, end)
                    if boundary > start:
                        end = boundary + 1

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            # 下一个chunk的起点考虑overlap
            start = max(start + 1, end - self.chunk_overlap)

        return chunks
