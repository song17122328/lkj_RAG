# CLAUDE.md - AI Assistant Guide for lkj_RAG

## Project Overview

**lkj_RAG** is a Retrieval-Augmented Generation (RAG) system with integrated Knowledge Graph capabilities, designed for processing and querying Chinese railway and transportation technical documents. The system combines semantic search, knowledge graph construction, and LLM-powered question answering to provide accurate, context-aware responses.

### Core Capabilities

- **Advanced Document Processing**: 5-stage pipeline with structure-aware chunking
  - **Table Extraction**: Preserves Markdown table structure with natural language conversion
  - **Numerical Enrichment**: Tags and summarizes percentages, currencies, distances, ratios
  - **Geographical Tagging**: Extracts provinces, cities, and geographic scope
- **Knowledge Graph**: Extracts entities and relationships using spaCy NLP models
- **Hybrid Retrieval**: Combines semantic search (embeddings) with BM25 keyword matching
  - **Cross-Encoder Reranking**: BAAI/bge-reranker-v2-m3 for precise relevance scoring
  - **Multi-path Retrieval**: File-guided + full-corpus strategies for balanced precision/recall
- **Vector Search**: Creates embeddings using BAAI/bge-m3 and ChromaDB similarity search
- **Multi-LLM Support**: Compatible with OpenAI, vLLM, and Ollama
- **Multilingual Support**: Optimized for Chinese/English/German mixed documents

## Repository Structure

```
lkj_RAG/
├── main.py                  # Entry point with test questions
├── pipeline.py              # Orchestrates the complete RAG workflow
├── rag_system.py            # Core RAG implementation (retrieval + QA)
├── retrieval.py             # Advanced retrieval with hybrid search & reranking
├── knowledge_graph.py       # Entity extraction and graph visualization
├── config.py                # Centralized configuration management
├── table_extractor.py       # [NEW v1.2] Table extraction & NL conversion
├── numerical_enricher.py    # [NEW v1.2] Numerical data tagging & summarization
├── geographical_tagger.py   # [NEW v1.2] Geographic entity extraction
├── .gitignore               # Excluded files and directories
├── vectorstore/             # Persisted vector database (ignored)
├── knowledge_graph.html     # Interactive graph visualization (ignored)
└── AI_database_markdown/    # Source documents (ignored)
```

## File-by-File Guide

### main.py (Entry Point)

**Purpose**: Application entry point that demonstrates the complete RAG pipeline with test questions.

**Key Features**:
- Configurable LLM backend (OpenAI vs vLLM)
- Option to use existing vectorstore or rebuild from scratch
- Includes 10 test questions about railway systems
- Outputs JSON-formatted results with retrieved contexts

**Usage Pattern**:
```python
# main.py:21-27
pipeline = CompleteRAGPipeline(
    use_openai=False,
    use_vllm=True,
    vllm_base_url="http://127.0.0.1:8910/v1"
)
```

**AI Assistant Notes**:
- When modifying test questions, maintain the technical domain focus
- The `interactive_qa()` method is commented out but available for testing
- Always check if `AI_database_markdown/` directory exists before processing

### config.py (Configuration)

**Purpose**: Central configuration hub for all system parameters.

**Key Configuration Sections**:

1. **LLM_CONFIG** (lines 10-37): Model provider settings
   - Supports: OpenAI, vLLM, Ollama, local models
   - Default: vLLM at `http://127.0.0.1:8910/v1`

2. **EMBEDDING_CONFIG** (lines 40-46): Vector embedding settings
   - Default: `paraphrase-multilingual-MiniLM-L12-v2`
   - Configurable device (CPU/CUDA)

3. **TEXT_SPLITTING** (lines 51-56): Document chunking parameters
   - chunk_size: 1000 characters
   - chunk_overlap: 200 characters
   - Separators optimized for Chinese/English text

4. **KNOWLEDGE_GRAPH** (lines 60-73): Graph construction settings
   - spaCy model selection (en_core_web_sm default)
   - Visualization options (HTML + PNG)

5. **VECTOR_STORE** (lines 77-82): ChromaDB configuration
   - Persistence directory: `./vectorstore`
   - Distance metric: cosine similarity

6. **RETRIEVAL** (lines 86-92): Search parameters
   - Top-k: 5 documents
   - Support for MMR (Maximum Marginal Relevance)

7. **PROMPTS** (lines 105-123): Template strings for LLM
   - QA template with Chinese instructions
   - Conversation history condensing

**AI Assistant Notes**:
- Always use `get_config()` to retrieve full configuration
- Use `update_config_for_chinese()` when working with Chinese documents
- Configuration is designed to be imported: `from config import LLM_CONFIG`

### pipeline.py (Orchestration)

**Purpose**: High-level pipeline that coordinates the entire RAG workflow.

**Class: CompleteRAGPipeline**

**Key Methods**:

1. **`__init__`** (lines 28-70): Initialize with LLM backend selection
   - Auto-configures based on `use_openai` and `use_vllm` flags
   - Creates `KnowledgeGraphBuilder` and `RAGSystem` instances

2. **`run_from_markdown`** (lines 152-182): Main processing pipeline
   - Accepts file paths or content dictionaries
   - Expands directories to find all `.md` files
   - Processes: Documents → Knowledge Graph → Vector Store → QA Chain

3. **`prepare_from_existing_vectorstore`** (lines 184-190): Fast startup
   - Skips document processing
   - Loads pre-built vectorstore
   - Useful for development/testing

4. **`answer_question`** (lines 192-194): Query interface
   - Returns dict with answer, source_documents, graph_context

5. **`interactive_qa`** (lines 196-241): CLI-based Q&A session
   - Special commands: 'exit', 'quit', 'graph'
   - Displays sources and graph entities

**Workflow Sequence**:
```
Markdown Files → Load → Knowledge Graph → Vector Store → QA Chain → Ready
```

**AI Assistant Notes**:
- Always check if vectorstore exists before deciding to rebuild
- The `_expand_markdown_inputs` method handles both files and directories
- Graph visualization is automatically saved to `knowledge_graph.html`

### rag_system.py (Core RAG)

**Purpose**: Implements the retrieval and generation pipeline.

**Class: RAGSystem**

**Initialization** (lines 47-177):
- **Embeddings**: Local HuggingFace or OpenAI
- **LLM**: OpenAI, vLLM, or Ollama with automatic model discovery
- **Text Splitter**: RecursiveCharacterTextSplitter with Chinese separators

**Key Methods**:

1. **`load_and_process_documents`** (lines 179-197)
   - Converts markdown to LangChain Document objects
   - Splits into chunks using configured parameters
   - Preserves source metadata

2. **`create_vector_store`** (lines 199-212)
   - Creates ChromaDB vectorstore
   - Persists to disk automatically
   - Uses configured embedding model

3. **`load_vector_store`** (lines 214-224)
   - Loads existing vectorstore from disk
   - Validates persistence directory exists

4. **`setup_qa_chain`** (lines 226-265)
   - Creates retriever with similarity search
   - Sets up RetrievalQA chain with custom prompt
   - Configures to return source documents

5. **`integrate_knowledge_graph`** (lines 267-270)
   - Links NetworkX graph to RAG system
   - Enables graph-based context enhancement

6. **`query`** (lines 272-314)
   - Main query interface
   - Returns: question, answer, source_documents, graph_context
   - Fallback to simple retrieval if no LLM available

**Private Methods**:

- **`_get_graph_context`** (lines 316-353): Extracts relevant subgraph
  - Entity matching in question
  - Neighbor expansion (max 5 neighbors)
  - Relation extraction

- **`_simple_answer_generation`** (lines 355-366): No-LLM fallback
  - Concatenates top 3 document chunks
  - Returns first 500 characters

**LLM Configuration Notes**:
- **vLLM**: Attempts to auto-detect model from `/models` endpoint (lines 122-131)
- **OpenAI**: Uses ChatOpenAI with compatible API
- **Ollama**: Requires `langchain-community` package

**AI Assistant Notes**:
- The system gracefully handles missing LLM (retrieval-only mode)
- Chinese separators in text splitter: `["。", "！", "？"]`
- Always check `self.llm` before calling QA chain methods
- Graph context is optional but enhances answer quality

### knowledge_graph.py (Graph Construction)

**Purpose**: Extracts entities and relationships from documents, builds and visualizes knowledge graphs.

**Class: KnowledgeGraphBuilder**

**Initialization** (lines 21-35):
- Attempts to load `zh_core_web_sm` (Chinese), falls back to `en_core_web_sm`
- Creates NetworkX DiGraph
- Initializes entity and relation trackers

**Key Methods**:

1. **`extract_entities_and_relations`** (lines 37-70)
   - Uses spaCy NER (Named Entity Recognition)
   - Extracts dependency-based relations
   - Targets: ROOT, prep, agent dependencies
   - Returns entities with labels and relations as triples

2. **`build_graph_from_documents`** (lines 72-106)
   - Processes documents in 5000-character chunks
   - Adds entities as nodes with metadata
   - Adds relations as directed edges
   - Preserves document source in graph attributes

3. **`visualize_graph`** (lines 115-133)
   - Creates interactive HTML using pyvis
   - Dark theme with white text
   - Node titles show entity types
   - Edge titles show relation types
   - Auto-saves to `knowledge_graph.html`

4. **`_save_static_graph`** (lines 138-162)
   - Generates PNG using matplotlib
   - Spring layout algorithm
   - Max 100 nodes (performance limit)
   - 20x15 figure size, 150 DPI

**Graph Structure**:
- **Nodes**: Entities with attributes `{label, doc_source}`
- **Edges**: Relations with attributes `{relation, doc_source}`
- **Format**: Directed graph (subject → object)

**AI Assistant Notes**:
- Text chunking (5000 chars) prevents spaCy memory issues
- Graph construction is language-agnostic (depends on spaCy model)
- Static graph generation skipped if >100 nodes
- Visualization requires browser to view HTML output

## Development Workflows

### 1. Initial Setup

```bash
# Install dependencies (recommended to create requirements.txt)
pip install langchain langchain-community chromadb
pip install sentence-transformers huggingface-hub
pip install spacy networkx matplotlib pyvis
python -m spacy download en_core_web_sm
python -m spacy download zh_core_web_sm  # For Chinese support
```

### 2. First Run (Build Vectorstore)

```bash
# Ensure AI_database_markdown/ directory exists with .md files
python main.py
# Input: N (to build new vectorstore)
```

**Expected Output**:
- `vectorstore/` directory created
- `knowledge_graph.html` interactive visualization
- `knowledge_graph.png` static image (if <100 nodes)
- JSON output with answers to test questions

### 3. Subsequent Runs (Use Existing Vectorstore)

```bash
python main.py
# Input: Y (to use existing vectorstore)
```

**Advantages**:
- Faster startup (skips document processing)
- Consistent results across runs
- Useful for testing prompt changes

### 4. Configuration Changes

**Switching LLM Backend**:

```python
# In main.py, modify:
USE_OPENAI = True   # For OpenAI
USE_VLLM = False

# Or:
USE_OPENAI = False
USE_VLLM = True     # For vLLM (default)
```

**Changing Embedding Model**:

```python
# In config.py, modify EMBEDDING_CONFIG:
EMBEDDING_CONFIG = {
    "model_name": "BAAI/bge-large-zh-v1.5",  # Better for Chinese
    "device": "cuda"  # Use GPU
}
```

**Adjusting Retrieval**:

```python
# In config.py, modify RETRIEVAL:
RETRIEVAL = {
    "k": 10,  # Retrieve more documents
    "search_type": "mmr",  # Use MMR for diversity
    "lambda_mult": 0.7  # More diversity
}
```

### 5. Adding New Features

**Adding a New Document Loader**:
1. Create method in `pipeline.py` (e.g., `_load_pdf_files`)
2. Add to `run_from_markdown` logic
3. Update `.gitignore` if needed

**Implementing Custom Retrieval**:
1. Modify `RAGSystem.setup_qa_chain` (rag_system.py:226)
2. Create custom retriever class
3. Update RETRIEVAL config with new parameters

**Enhancing Knowledge Graph**:
1. Modify `extract_entities_and_relations` (knowledge_graph.py:37)
2. Add custom relation extraction rules
3. Update visualization colors/layout

### 6. Testing Workflow

**Unit Testing**:
```python
# Create tests/test_rag_system.py
from rag_system import RAGSystem

def test_document_loading():
    rag = RAGSystem(embedding_model="local", llm_model="local")
    # Test document processing
```

**Integration Testing**:
```python
# Test full pipeline
pipeline = CompleteRAGPipeline(use_vllm=True)
result = pipeline.answer_question("Test question?")
assert result["answer"] is not None
```

## Key Conventions

### 1. Code Style

- **Language**: Chinese comments for domain-specific explanations, English for code
- **Logging**: Use `logging` module, not `print()` (except in main.py for user output)
- **Error Handling**: Graceful fallbacks (e.g., no LLM → retrieval-only mode)
- **Type Hints**: Present in function signatures (e.g., `Dict[str, str]`)

### 2. Configuration Pattern

- **Centralized**: All configs in `config.py`
- **Hierarchical**: Nested dicts for grouped settings
- **Overridable**: Function parameters override config defaults
- **Documented**: Comments explain each parameter

### 3. Data Flow

```
Markdown → Document → Chunks → Embeddings → Vectorstore
                ↓
         Knowledge Graph (parallel)
                ↓
            QA Chain (combines both)
```

### 4. Naming Conventions

- **Classes**: PascalCase (e.g., `RAGSystem`, `CompleteRAGPipeline`)
- **Functions**: snake_case (e.g., `load_and_process_documents`)
- **Private Methods**: Prefix with `_` (e.g., `_split_text`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `LLM_CONFIG`)

### 5. File Naming

- **Python Modules**: snake_case (e.g., `rag_system.py`)
- **Output Files**: Descriptive (e.g., `knowledge_graph.html`)
- **Directories**: snake_case (e.g., `AI_database_markdown/`)

### 6. Import Organization

```python
# Standard library
import os
from typing import List, Dict

# Third-party
from langchain import ...
import networkx as nx

# Local modules
from config import LLM_CONFIG
from rag_system import RAGSystem
```

### 7. Error Handling Strategy

- **File Operations**: Log warnings, continue processing
- **LLM Failures**: Fallback to retrieval-only mode
- **Missing Dependencies**: Inform user with installation instructions
- **Empty Results**: Return informative messages, not errors

## AI Assistant Guidelines

### When Working on This Codebase

1. **Always Read Configuration First**
   - Check `config.py` for parameter defaults
   - Understand which LLM backend is active
   - Note the embedding model being used

2. **Respect the Pipeline Architecture**
   - Don't bypass pipeline.py for complete workflows
   - Use existing methods before creating new ones
   - Maintain separation: main.py (UI) → pipeline.py (orchestration) → rag_system.py (logic)

3. **Handle Multilingual Content**
   - Assume documents may be Chinese or English
   - Use Unicode-safe string operations
   - Test separators work for both languages
   - Check spaCy model matches document language

4. **Preserve Metadata**
   - Always include `source` in document metadata
   - Maintain `doc_source` in graph attributes
   - Return source_documents in query results

5. **Test with Real Data**
   - Use test questions from main.py as examples
   - Verify answers are factually grounded in sources
   - Check retrieved documents are relevant

6. **Performance Considerations**
   - Large documents: Ensure chunking is active
   - Many documents: Consider batch processing
   - Graph visualization: Skip PNG if >100 nodes
   - LLM calls: Cache results when possible

7. **Logging Best Practices**
   - Use `logger.info()` for major steps
   - Use `logger.warning()` for fallbacks
   - Use `logger.error()` for critical failures
   - Include context in log messages

8. **Configuration Modifications**
   - Update `config.py`, not hardcoded values
   - Document new configuration parameters
   - Provide sensible defaults
   - Add validation where appropriate

9. **Dependency Management**
   - Check if new libraries are necessary
   - Prefer libraries already in use
   - Note version compatibility (LangChain is version-sensitive)
   - Add try/except for optional dependencies

10. **Documentation Updates**
    - Update this file when architecture changes
    - Add docstrings to new functions
    - Explain non-obvious design decisions
    - Keep comments accurate with code

### Common Tasks

#### Adding a New LLM Provider

1. Add configuration to `config.py` LLM_CONFIG
2. Implement initialization in `rag_system.py` RAGSystem.__init__
3. Update `pipeline.py` to accept new provider flag
4. Test with a simple query
5. Document in this file

#### Modifying Prompt Templates

1. Locate template in `config.py` PROMPTS section
2. Edit template string (maintain {context} and {question} placeholders)
3. Test with various question types
4. Consider Chinese/English language needs

#### Changing Vector Database

1. Update VECTOR_STORE config in `config.py`
2. Modify imports in `rag_system.py`
3. Replace Chroma methods in create_vector_store and load_vector_store
4. Update persistence logic
5. Test migration path

#### Improving Knowledge Graph

1. Options:
   - Better NER: Train custom spaCy model
   - Better relations: Use dependency parsing rules
   - Better visualization: Customize pyvis settings
2. Modify `knowledge_graph.py` methods
3. Test with documents containing clear entities/relations
4. Update visualization if needed

### Debugging Tips

1. **LLM Not Responding**
   - Check vLLM service: `curl http://127.0.0.1:8910/v1/models`
   - Verify API key if using OpenAI
   - Look for error logs in console
   - Test with `llm_model="local"` for retrieval-only

2. **Poor Retrieval Results**
   - Verify vectorstore exists: `ls -la vectorstore/`
   - Check chunk_size (config.py): Too large = less precise
   - Increase k in RETRIEVAL config
   - Try MMR search for diversity

3. **Empty Knowledge Graph**
   - Verify spaCy model installed: `python -m spacy download en_core_web_sm`
   - Check if NER finds entities in your documents
   - Ensure documents have named entities (not just generic text)
   - Review extracted entities: Print in build_graph_from_documents

4. **Memory Issues**
   - Reduce TEXT_SPLITTING chunk_size
   - Lower batch_size in EMBEDDING_CONFIG
   - Process documents in smaller batches
   - Limit knowledge graph chunk_size (currently 5000)

5. **Encoding Errors**
   - Verify file encoding: `file -i *.md`
   - Ensure UTF-8: Files should be UTF-8 encoded
   - Check locale: `echo $LANG` (should include UTF-8)

### Performance Optimization

1. **Faster Startup**
   - Use existing vectorstore (prepare_from_existing_vectorstore)
   - Cache embeddings if rebuilding frequently
   - Disable knowledge graph if not needed (set KNOWLEDGE_GRAPH["enabled"] = False)

2. **Better Retrieval Quality**
   - Use better embedding model: `BAAI/bge-large-zh-v1.5` for Chinese
   - Increase chunk_overlap for context continuity
   - Tune retrieval k based on document density
   - Enable reranking (ADVANCED_FEATURES)

3. **Faster LLM Response**
   - Use local vLLM instead of OpenAI (lower latency)
   - Reduce max_tokens in LLM_CONFIG
   - Lower temperature for deterministic outputs
   - Consider smaller, faster models for development

4. **Graph Performance**
   - Limit max_entities_per_doc (config.py:63)
   - Increase min_entity_frequency to filter noise
   - Disable static PNG for large graphs

## Technical Debt & Future Improvements

### Known Limitations

1. **Language Model Detection**: spaCy auto-detection could be improved
2. **Relation Extraction**: Current method is rule-based and simple
3. **No Reranking**: Retrieved documents are not reranked by relevance
4. **Limited Error Recovery**: Some failures cause complete stops
5. **No Hybrid Search**: Only semantic search, no keyword matching
6. **Hardcoded Paths**: Some paths could be more configurable

### Recommended Enhancements

1. **Add Requirements File**
   ```
   langchain>=0.1.0
   langchain-community>=0.1.0
   chromadb>=0.4.0
   sentence-transformers>=2.2.0
   spacy>=3.5.0
   networkx>=3.0
   pyvis>=0.3.1
   matplotlib>=3.5.0
   ```

2. **Implement Caching**
   - Cache embedding computations
   - Cache LLM responses for repeated questions
   - Use SYSTEM["cache_enabled"] from config.py

3. **Add Evaluation Metrics**
   - Retrieval precision/recall
   - Answer quality scoring
   - Graph coverage metrics

4. **Improve CLI**
   - Add argparse for command-line options
   - Progress bars for document processing
   - Better error messages

5. **Add Tests**
   - Unit tests for each module
   - Integration tests for pipeline
   - Regression tests for test questions

6. **Better Logging**
   - Structured logging (JSON format)
   - Log levels per module
   - Log file rotation

## Environment Variables

The system supports the following environment variables:

```bash
# OpenAI Configuration
export OPENAI_API_KEY="sk-..."

# Ollama Configuration
export OLLAMA_BASE_URL="http://127.0.0.1:11434"
export OLLAMA_MODEL="llama3"

# General
export LOG_LEVEL="INFO"  # DEBUG, INFO, WARNING, ERROR
```

## Git Workflow

### Ignored Files (.gitignore)

- `demo_example_provided/`: Example data
- `AI_database_markdown/`: Source documents (large, user-provided)
- `AI_database/`: Processed database
- `processed_documents/`: Intermediate files
- `__pycache__/`: Python cache
- `knowledge_graph.html`: Generated visualization
- `vectorstore/`: Vector database (should be regenerated)

### Commit Conventions

- **feat**: New feature (e.g., "feat: add Ollama support")
- **fix**: Bug fix (e.g., "fix: handle empty documents")
- **docs**: Documentation (e.g., "docs: update CLAUDE.md")
- **refactor**: Code restructuring (e.g., "refactor: simplify pipeline")
- **perf**: Performance improvement (e.g., "perf: batch embedding")
- **test**: Add tests (e.g., "test: add RAG system tests")

### Branch Strategy

- `main`: Stable, production-ready code
- `develop`: Integration branch for features
- `feature/*`: Individual feature branches
- `fix/*`: Bug fix branches

## Troubleshooting

### Issue: "AI_database_markdown目录不存在"

**Solution**: Create directory and add markdown files:
```bash
mkdir -p AI_database_markdown
# Add your .md files to this directory
```

### Issue: "请安装spaCy语言模型"

**Solution**: Install required spaCy models:
```bash
python -m spacy download en_core_web_sm
python -m spacy download zh_core_web_sm
```

### Issue: vLLM connection refused

**Solution**: Verify vLLM service is running:
```bash
# Check if vLLM is accessible
curl http://127.0.0.1:8910/v1/models

# If not running, start vLLM service
# (Refer to vLLM documentation for startup)
```

### Issue: "使用OpenAI模型需要提供API密钥"

**Solution**: Set API key:
```bash
export OPENAI_API_KEY="sk-your-key-here"
# Or modify main.py line 16
```

### Issue: Low-quality answers

**Checklist**:
1. Verify documents are in `AI_database_markdown/`
2. Check vectorstore was created successfully
3. Ensure k=5 is sufficient for your use case
4. Try increasing chunk_overlap in config.py
5. Verify LLM is properly configured and responding

## Quick Reference

### Starting the System

```python
from pipeline import CompleteRAGPipeline

# Initialize
pipeline = CompleteRAGPipeline(use_vllm=True)

# Option 1: Build from scratch
pipeline.run_from_markdown(markdown_inputs=["path/to/docs/"])

# Option 2: Use existing vectorstore
pipeline.prepare_from_existing_vectorstore()

# Query
result = pipeline.answer_question("Your question?")
print(result["answer"])
```

### Configuration Quick Changes

```python
# In config.py

# More documents in retrieval
RETRIEVAL["k"] = 10

# Smaller chunks (more precise)
TEXT_SPLITTING["chunk_size"] = 500

# Use GPU for embeddings
EMBEDDING_CONFIG["device"] = "cuda"

# Change LLM temperature
LLM_CONFIG["temperature"] = 0.3
```

### Checking System Status

```python
# Check vectorstore exists
import os
print(os.path.exists("./vectorstore"))

# Check graph statistics
pipeline.interactive_qa()  # Type 'graph' command

# Check retrieved documents
result = pipeline.answer_question("test")
print(len(result["source_documents"]))
```

## Support and Resources

- **LangChain Docs**: https://python.langchain.com/docs/
- **ChromaDB Docs**: https://docs.trychroma.com/
- **spaCy Docs**: https://spacy.io/usage
- **NetworkX Docs**: https://networkx.org/documentation/

## Version History

- **v1.2** (2025-11-22): Comprehensive RAG optimization for numerical reasoning and table understanding
  - **P0 Optimization - Document Enhancement Pipeline**:
    - **NEW: table_extractor.py** (642 lines): Markdown table extraction with natural language conversion
      - Extracts tables as structured data with {headers, rows}
      - Generates natural language descriptions ("南京的线路为S7号线, 里程为30.20")
      - Creates independent Document objects with table metadata
      - Solves: Nanjing Metro S7 ranking problem (table data lost in text conversion)
    - **NEW: numerical_enricher.py** (431 lines): Numerical data identification and tagging
      - Identifies 6 types: percentage, currency, distance, time, count, ratio
      - Adds metadata tags: `numerical_values=['8%', '40%']`, `numerical_types=['percentage']`
      - Generates numerical summaries: "百分比数据: 8%, 40%; 涉及增长率或目标数据"
      - Solves: UIC market share calculation problem (8% × (1+40%) = 11.2%)
    - **NEW: geographical_tagger.py** (445 lines): Geographic entity extraction and scope identification
      - Extracts provinces and cities using spaCy NER + rule-based matching
      - Tags geographic scope: national/provincial/municipal
      - Province-city relationship mapping for 11 major provinces
      - Solves: Geographic confusion (e.g., Beijing vs Jiangsu documents)
    - **MODIFIED: rag_system.py**: Integrated 5-stage document processing pipeline
      - Stage 1: Table extraction (separate Documents)
      - Stage 2: Markdown structure-aware splitting
      - Stage 3: Chunk splitting with overlap
      - Stage 4: Numerical & geographical enrichment
      - Stage 5: Merge all Documents
    - **config.py**: Added `DOCUMENT_ENHANCEMENT` configuration section

  - **P1 Optimization - Retrieval Depth & Quality**:
    - **Retrieval depth**: Increased k from 8→10, fetch_k from 30→50, lambda_mult from 0.7→0.6
      - Rationale: Multi-step reasoning questions need broader context coverage
    - **Hybrid search weight**: Increased from 0.3→0.4 for better BM25 keyword matching
      - Rationale: BM25 excels at exact term matching (e.g., "8%", "S7号线")
    - **Reranker upgrade**: BAAI/bge-reranker-base → BAAI/bge-reranker-v2-m3
      - Better multilingual support (Chinese/English/German)
      - Added reranker_threshold=0.3 to filter low-relevance documents
    - **Reranking candidates**: Increased reranking_top_k from 20→30
    - **MODIFIED: retrieval.py**: Implemented threshold-based filtering in `_simple_rerank()`

  - **P2 Optimization - Chunk Size & Context**:
    - **Chunk size**: Increased from 500→800 characters
      - Rationale: Reduce probability of splitting key sentences across chunks
    - **Chunk overlap**: Increased from 100→200 characters
      - Rationale: Ensure context continuity for cross-chunk information
    - **Prompt template**: Already optimized with explicit numerical reasoning instructions
      - Example: "当前8%，需增长40%，则目标为8%×(1+40%)=11.2%"
      - Table ranking guidance: "对于排名类问题，需要对数值进行比较和排序"

  - **Expected Impact**:
    - Table-based questions: 0% → ~80% accuracy
    - Numerical reasoning questions: 0% → ~70% accuracy
    - Overall accuracy: 50% → 80%+ (projected)

- **v1.1** (2025-11-22): Retrieval accuracy improvements
  - **Critical Fix**: Resolved `available_files=0` issue when loading from existing vectorstore
    - Modified `_extract_available_files()` in retrieval.py to extract filenames from vectorstore metadata when `self.documents` is empty
    - Automatically strips legacy "MinerU_" prefix from filenames for compatibility
  - **Optimization**: Improved regex-based file name extraction
    - Removed misleading entity patterns (company names, location names)
    - Enhanced standard number detection (IEEE, GB/T, ISO, SUBSET, T/CAMET)
    - Added document type keyword extraction for better file matching
  - **Configuration**: Already optimized for multi-language documents
    - Embedding model: BAAI/bge-m3 (best for Chinese/English/German混合)
    - Chunk size: 500 characters (optimized for precision)
    - Retrieval: MMR with k=5, fetch_k=15 for balanced coverage
  - **Impact**: LLM-driven file selection now functional, improved retrieval precision

- **v1.0**: Initial implementation with vLLM, OpenAI, Ollama support
  - Knowledge graph integration
  - Multi-language support
  - Interactive and batch modes

---

**Last Updated**: 2025-11-22
**Maintained By**: Project Team
**For Questions**: Review this document first, then check logs, then ask maintainers
