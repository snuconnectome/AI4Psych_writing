# Intro_Pipeline: Automated Academic Introduction Generator

An advanced multi-agent pipeline that automatically generates publication-ready academic research paper introductions using AI, literature search, and rigorous validation.

## Overview

**Intro_Pipeline** combines automated PubMed literature search with AI-powered writing to create well-structured, properly cited academic introductions. The system uses a 7-agent pipeline that handles everything from topic definition to final style checking.

### Key Features

- **Automated Literature Search**: PubMed API integration with optimized search queries
- **AI-Powered Writing**: Generates academic introductions with proper citations
- **Logic Validation**: Ensures coherence and relevance of every sentence
- **User Integration**: Merges user-written content with AI-generated text
- **Publication-Ready Output**: Applies 25+ academic writing rules for polished results
- **APA 7th Edition**: Automatic citation formatting

## Pipeline Architecture

The system consists of 7 sequential agents:

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| **Agent 0** | Topic Definition | Research topic (free text) | Structured topic + keywords + PubMed queries |
| **Agent 1** | Literature Search | Topic definition | 25+ papers with APA formatting |
| **Agent 2** | Introduction Writer | Papers + topic | Draft introduction (~1500 words) |
| **Agent 3** | Logic Checker | Draft introduction | Logic validation report |
| **Agent 3.5** | Logic Rewriter | Draft + validation | Improved introduction |
| **Agent 4** | User Integrator | User intro + AI intro | Merged introduction |
| **Agent 5** | Style Checker | Integrated text | Publication-ready final version |

## Installation

### Requirements

- Python 3.12+
- Jupyter Notebook
- Virtual environment (recommended)

### Dependencies

```bash
pip install aisuite google-generativeai openai requests pandas python-dotenv openpyxl
```

### API Setup

1. Create a `.env` file in the HW6 directory:

```env
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_google_gemini_key_here
```

2. Required API access:
   - **OpenAI API**: For GPT models
   - **Google Gemini API**: For generative AI with tool calling
   - **PubMed E-utilities**: Free, no key required

## Usage

### Quick Start

1. Open the notebook:
```bash
jupyter notebook Intro_Pipeline.ipynb
```

2. Run cells sequentially, providing your research topic when prompted

3. Find output files in the HW6 directory with timestamps

### Configuration Parameters

```python
# Agent 1: Literature Search
max_papers = 25              # Number of papers to retrieve
interactive_mode = False     # Manual query selection
year = "2000:2025"          # Publication year range

# Agent 3: Logic Validation
threshold = 0.6             # Relevance threshold (0.0-1.0)
                           # 0.5 = lenient, 0.6 = moderate, 0.7 = strict
```

### Example Workflow

```python
# 1. Define your research topic
topic = """
TMS를 SPC(Superior parietal cortex)에 적용하여
working memory 수행 변화 측정하는 연구
"""

# 2. Run Agent 0-5 sequentially (in notebook cells)
# Each agent automatically saves outputs with timestamps

# 3. Optional: Provide your own introduction for Agent 4
user_intro_path = "user_introduction/revised_introduction.txt"

# 4. Get final publication-ready introduction from Agent 5
```

## Output Files

All outputs are timestamped (format: `YYYYMMDD_HHMMSS`):

```
HW6/
├── agent0_topic_definition_[timestamp].txt
├── papers_search_[timestamp].json          # Complete paper metadata
├── papers_table_[timestamp].csv            # Excel-compatible table
├── agent2_introduction_draft_[timestamp].txt
├── agent3_logic_report_[timestamp].txt
├── agent3.5_logic_revised_[timestamp].txt
├── agent4_integrated_[timestamp].txt
└── agent5_final_[timestamp].txt           # Final deliverable
```

## Agent Details

### Agent 0: Topic Definition
- Converts free-form research description to structured format
- Generates 5-7 keywords and 3-5 optimized PubMed queries
- Output: Main topic, field, methods, specific focus

### Agent 1: Literature Search & APA Formatting
- Searches PubMed using advanced query syntax
- Retrieves ~25 papers with full metadata
- Formats all references in APA 7th edition
- Exports JSON (complete) and CSV (table) formats

### Agent 2: Introduction Writer
- Acts as expert academic writer
- Structures introduction in 4 sections:
  1. Background (2-3 paragraphs)
  2. Current research trends (2-3 paragraphs)
  3. Research gap (1-2 paragraphs)
  4. Study necessity (1-2 paragraphs)
- Uses proper (Author, Year) citations

### Agent 3: Logic Checker
- Validates each sentence's relevance to main topic
- Scores sentences 0-10 for logical coherence
- Identifies problematic sentences below threshold
- Provides specific improvement suggestions

### Agent 3.5: Logic-Based Rewriter
- Rewrites/deletes sentences scoring 0-4
- Enhances sentences scoring 4-6
- Preserves sentences scoring 7-10
- Output: Logically coherent introduction

### Agent 4: User-Pipeline Integrator
- Merges user-written introduction with AI version
- Adds citations to user's text
- Preserves user's voice and arguments
- Combines best elements from both sources

### Agent 5: Style Checker
- Applies 25+ academic writing rules
- Enforces formal academic English
- Ensures publication-ready quality
- Final output ready for submission

## Supporting Tools

Located in `user_introduction/`:

- **01_referencing.py**: Converts raw references to APA 7th format
- **02_translate.py**: Korean→English translation with citations
- **03_revise.py**: Academic style revision with writing rules

## Runtime

- **Total pipeline**: ~10-15 minutes
- **Per agent**: 30 seconds to 3 minutes (varies by complexity)

## Technical Details

### Custom LLM Wrapper

The notebook includes a `UnifiedLLMClient` class that:
- Provides unified interface for OpenAI and Gemini APIs
- Automatically converts Python functions to Gemini Tool format
- Handles tool calling and function execution
- Supports both streaming and non-streaming responses

### PubMed Integration

- Uses E-utilities API (ESearch + EFetch)
- Optimized query generation with Boolean operators
- Automatic retry logic for failed requests
- Metadata extraction: PMID, Title, Authors, Year, Journal, DOI

### Data Processing

- JSON for complete metadata storage
- CSV for Excel-compatible tables
- Pandas for data manipulation
- Automatic timestamp generation for versioning

## Best Practices

1. **Topic Definition**: Be specific about your research focus, methods, and field
2. **Literature Search**: Review generated queries before execution (use `interactive_mode=True`)
3. **Logic Threshold**: Start with 0.6, adjust based on results
4. **User Integration**: Provide well-structured user introduction for best results
5. **API Limits**: Monitor API usage to stay within rate limits

## Troubleshooting

### Common Issues

**"API key not found"**
- Ensure `.env` file is in the same directory as notebook
- Check API key format (no quotes needed in .env)

**"No papers found"**
- Broaden search queries or date range
- Check topic definition keywords
- Try `interactive_mode=True` to review queries

**"Logic validation too strict"**
- Lower threshold to 0.5
- Review Agent 3 report for specific issues

**"Out of tokens/rate limit"**
- Reduce `max_papers` parameter
- Add delays between API calls
- Check API plan limits

## Output Example

### Agent 5 Final Output (Publication-Ready)
```
Working memory, the cognitive system responsible for temporary storage
and manipulation of information, plays a crucial role in complex cognitive
tasks (Baddeley & Hitch, 1974). Recent advances in non-invasive brain
stimulation techniques have enabled researchers to causally investigate
the neural mechanisms underlying working memory processes...

[Continues with full introduction, proper citations, academic style]
```