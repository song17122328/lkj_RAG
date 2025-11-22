"""
文档并行处理模块

功能：
1. 使用多进程并行处理Markdown文档
2. 加速表格提取、文本分割、数值/地理标注
3. 自动管理进程池和异常处理
"""

import logging
import multiprocessing as mp
from typing import Dict, List, Tuple, Optional
from functools import partial

try:
    from langchain.schema import Document
except ImportError:
    from dataclasses import dataclass

    @dataclass
    class Document:
        page_content: str
        metadata: Optional[Dict] = None

logger = logging.getLogger(__name__)


def process_single_document(
    doc_item: Tuple[str, str],
    text_splitter_config: Dict,
    markdown_splitter_config: Dict,
    use_enhancement: bool = True
) -> List[Document]:
    """
    处理单个Markdown文档（在worker进程中执行）

    Args:
        doc_item: (doc_name, content) 元组
        text_splitter_config: 文本分割配置
        markdown_splitter_config: Markdown分割配置
        use_enhancement: 是否启用增强功能

    Returns:
        处理后的Document列表
    """
    doc_name, content = doc_item

    if not content:
        return []

    # === 在worker进程中初始化所需的对象 ===
    # 注意：spaCy模型不能跨进程传递，必须在每个worker中重新加载
    from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

    # 初始化文本分割器
    text_splitter = RecursiveCharacterTextSplitter(**text_splitter_config)

    # 初始化Markdown分割器
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=markdown_splitter_config['headers_to_split_on'],
        strip_headers=markdown_splitter_config['strip_headers']
    )

    # 初始化增强模块（如果启用）
    table_documents = []
    if use_enhancement:
        try:
            from table_extractor import TableExtractor
            from numerical_enricher import NumericalDataEnricher
            from geographical_tagger import GeographicalTagger

            table_extractor = TableExtractor()
            numerical_enricher = NumericalDataEnricher()
            geographical_tagger = GeographicalTagger()
        except Exception as e:
            logger.warning(f"Worker进程中增强模块初始化失败: {e}")
            use_enhancement = False

    # === 阶段1: 表格提取 ===
    if use_enhancement:
        try:
            table_documents = table_extractor.extract_tables_from_markdown(content, doc_name)
        except Exception as e:
            logger.warning(f"表格提取失败({doc_name}): {e}")
            table_documents = []

    # === 阶段2: 文本分割（Markdown结构感知） ===
    try:
        md_header_splits = markdown_splitter.split_text(content)

        # 添加source元数据
        for split in md_header_splits:
            split.metadata["source"] = doc_name

        # === 阶段3: chunk分割 ===
        final_chunks = []
        for md_doc in md_header_splits:
            if len(md_doc.page_content) > 1000:
                sub_chunks = text_splitter.split_documents([md_doc])
                for chunk in sub_chunks:
                    chunk.metadata.update(md_doc.metadata)
                final_chunks.extend(sub_chunks)
            else:
                final_chunks.append(md_doc)

    except Exception as e:
        logger.warning(f"Markdown结构分割失败({doc_name}): {e}，降级到字符分割")
        doc = Document(
            page_content=content,
            metadata={"source": doc_name}
        )
        final_chunks = text_splitter.split_documents([doc])

    # === 阶段4: 数值和地理信息增强 ===
    if use_enhancement:
        enhanced_chunks = []
        for chunk in final_chunks:
            try:
                # 数值增强
                enriched_text, enriched_metadata = numerical_enricher.enrich_text(
                    chunk.page_content,
                    chunk.metadata
                )

                # 地理标注
                enriched_metadata = geographical_tagger.extract_geographical_info(
                    chunk.page_content,
                    enriched_metadata
                )

                enhanced_chunk = Document(
                    page_content=enriched_text,
                    metadata=enriched_metadata
                )
                enhanced_chunks.append(enhanced_chunk)

            except Exception as e:
                logger.warning(f"增强失败: {e}，保留原chunk")
                enhanced_chunks.append(chunk)

        final_chunks = enhanced_chunks

    # === 阶段5: 合并文本和表格 ===
    all_documents = final_chunks + table_documents

    logger.info(f"Worker完成 {doc_name}: {len(final_chunks)} 文本chunks + {len(table_documents)} 表格")

    return all_documents


class ParallelDocumentProcessor:
    """并行文档处理器"""

    def __init__(self,
                 text_splitter_config: Dict,
                 markdown_splitter_config: Dict,
                 n_workers: Optional[int] = None,
                 use_enhancement: bool = True):
        """
        Args:
            text_splitter_config: RecursiveCharacterTextSplitter配置
            markdown_splitter_config: MarkdownHeaderTextSplitter配置
            n_workers: 工作进程数（None=自动检测CPU核心数）
            use_enhancement: 是否启用表格提取、数值/地理增强
        """
        self.text_splitter_config = text_splitter_config
        self.markdown_splitter_config = markdown_splitter_config
        self.use_enhancement = use_enhancement

        # 自动检测CPU核心数
        if n_workers is None:
            # 留一个核心给系统，避免100%占用
            self.n_workers = max(1, mp.cpu_count() - 1)
        else:
            self.n_workers = max(1, n_workers)

        logger.info(f"并行处理器初始化: {self.n_workers} 个worker进程")

    def process_documents(self, markdown_contents: Dict[str, str]) -> List[Document]:
        """
        并行处理多个Markdown文档

        Args:
            markdown_contents: {doc_name: content} 字典

        Returns:
            所有处理后的Document列表
        """
        if not markdown_contents:
            return []

        # 将字典转为列表（便于并行处理）
        doc_items = list(markdown_contents.items())

        logger.info(f"开始并行处理 {len(doc_items)} 个文档，使用 {self.n_workers} 个进程...")

        # 创建partial函数（固定部分参数）
        process_func = partial(
            process_single_document,
            text_splitter_config=self.text_splitter_config,
            markdown_splitter_config=self.markdown_splitter_config,
            use_enhancement=self.use_enhancement
        )

        # 使用进程池并行处理
        all_documents = []
        try:
            # 使用 'spawn' 启动方式，避免CUDA/spaCy的fork问题
            ctx = mp.get_context('spawn')
            with ctx.Pool(processes=self.n_workers) as pool:
                # map会按顺序返回结果
                results = pool.map(process_func, doc_items)

                # 合并所有结果
                for doc_documents in results:
                    all_documents.extend(doc_documents)

        except Exception as e:
            logger.error(f"并行处理失败: {e}，降级到串行处理")
            # 降级到串行处理
            for doc_item in doc_items:
                try:
                    doc_documents = process_func(doc_item)
                    all_documents.extend(doc_documents)
                except Exception as doc_e:
                    logger.error(f"处理文档失败 {doc_item[0]}: {doc_e}")
                    continue

        logger.info(f"并行处理完成，共 {len(all_documents)} 个chunks")

        return all_documents
