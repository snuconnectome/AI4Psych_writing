# Multi-Agent Academic Writing System

**Jeongyeon's AI-Powered Writing Assistant for Psychology Research Papers**

This system uses multiple specialized AI agents to improve academic writing quality, with automatic LaTeX support and comprehensive feedback.

---

## 📚 Overview

A multi-agent orchestration system designed to improve academic papers through specialized AI agents, each focusing on different aspects of writing quality:

- **LaTeX Converter** (00): Automatically detects and converts LaTeX to plain text
- **Writer Agent** (01): Revises text using top-tier writing principles
- **Literature Validator** (02): Validates research gaps and citations
- **Quality Checker** (03): Evaluates clarity, coherence, and style
- **Logic Auditor** (04): Analyzes argument structure and logical flow
- **Statistics Reviewer** (05): Checks reproducibility and statistical rigor
- **Coordinator** (06): Integrates all feedback and produces final revision

---

## 🚀 Quick Start

### 1. Setup

```bash
# Install dependencies
cd orchestrator
pip install -r requirements.txt

# Set your API key (Gemini, OpenAI, or Anthropic)
export GEMINI_API_KEY="your-api-key-here"
```

### 2. Improve Your Introduction (LaTeX or Plain Text)

```bash
# Auto-detects LaTeX and converts!
python3 improve_latex_intro_with_tables.py
```

This automatically:
- ✅ Detects LaTeX and converts to plain text
- ✅ Improves main text with gap_discovery workflow
- ✅ Proof-reads all tables
- ✅ Generates detailed feedback and revised text

---

## 📁 Project Structure

```
.
├── README.md                           # This file
├── agents/                             # Agent system prompts (7 agents)
│   ├── 00_latex_converter_agent.md
│   ├── 01_writer_agent.md
│   ├── 02_literature_validator.md
│   ├── 03_quality_checker.md
│   ├── 04_logic_auditor.md
│   ├── 05_statistics_reviewer.md
│   └── 06_coordinator_agent.md
│
├── orchestrator/                       # Core system
│   ├── agent_base.py                   # Agent classes
│   ├── multi_agent_orchestrator.py     # Main orchestrator
│   ├── latex_detector.py               # Auto LaTeX detection
│   └── requirements.txt
│
├── improve_latex_intro_with_tables.py  # Main script
└── 1-intro-en.tex                      # Your LaTeX file
```

---

## 🔧 Key Features

### ✅ Automatic LaTeX Detection

Works with **both LaTeX and plain text** - automatically detected!

```python
# LaTeX input
latex = r"\section{Intro} ELS \citep{carr2013}..."

# Plain text input  
plain = "Introduction\n\nELS (Carr et al., 2013)..."

# Both work! System auto-detects.
result = orchestrator.run_workflow("gap_discovery", latex, context)
```

### ✅ Predefined Workflows

**gap_discovery** (Best for Introductions)
```
Literature Validator → Logic Auditor → Writer → Coordinator
```

**abstract_revision**, **methods_validation**, **results_validation**, etc.

### ✅ Comprehensive Feedback

```json
{
  "executive_summary": {...},
  "integrated_feedback": {
    "priority_1_critical": [...],  // Must fix
    "priority_2_high": [...],       // Important
    "priority_3_medium": [...],     // Recommended
    "priority_4_low": [...]         // Polish
  },
  "integrated_revision": {
    "revised_text": "...",
    "change_log": [...]
  }
}
```

---

## 🎯 Usage Examples

### Example 1: Improve Introduction

```python
from orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator

orchestrator = MultiAgentOrchestrator(provider="gemini")

result = orchestrator.run_workflow(
    workflow_name="gap_discovery",
    input_text=your_intro_text,  # LaTeX or plain text
    context={
        "section": "introduction",
        "paper_title": "Your Paper Title",
        "target_journal": "Developmental Psychology"
    }
)

revised = result['integrated_revision']['revised_text']
```

### Example 2: Use Pre-made Script

```bash
# Edit the file path in improve_latex_intro_with_tables.py
python3 improve_latex_intro_with_tables.py
```

Output files:
- `intro_revised_plain.txt` - Revised main text
- `intro_main_result.json` - Detailed feedback
- `intro_table_results.json` - Table issues
- `RECONSTRUCTION_GUIDE.md` - How to merge back

---

## 🤖 Supported LLM Providers

### Groq (Free - RECOMMENDED!) ✨
```python
orchestrator = MultiAgentOrchestrator(provider="groq")
```
✅ **Best free option!**
- Fast inference (2-3x faster than Gemini)
- Generous rate limits (30 req/min, 14,400 req/day)
- No credit card required
- Get API key: https://console.groq.com/keys

### Gemini (Free)
```python
orchestrator = MultiAgentOrchestrator(provider="gemini")
```
⚠️ Rate limits: ~15 requests/minute (may hit quota easily)

### OpenAI (Paid)
```python
orchestrator = MultiAgentOrchestrator(provider="openai", model="gpt-4")
```

### Anthropic (Paid)
```python
orchestrator = MultiAgentOrchestrator(provider="anthropic", model="claude-sonnet-4")
```

---

## ⚠️ Troubleshooting

### Gemini Quota Exceeded (429 Error)

**Solutions:**
1. Wait 1-2 minutes between runs
2. Use different model: `gemini-2.5-flash-preview-05-20`
3. Switch to OpenAI or Anthropic

### File Too Large

Split into sections or use `improve_latex_intro_with_tables.py` (auto-splits)

---

## 🎓 Tips

1. **Provide Rich Context**: Include paper title, target journal, research field
2. **Choose Right Workflow**: gap_discovery for intro, abstract_revision for abstract
3. **Review All Priorities**: Don't skip medium/low priority suggestions
4. **Iterate**: Run multiple times for best results

---

## 📞 Contact

**Author**: Jeongyeon Shin (신정연)
**Email**: tlswjddus98@snu.ac.kr  
**Affiliation**: Seoul National University, Department of Psychology

---

**Last Updated**: 2025-01-10  
**Version**: 1.0.0

Built with course materials from **심리과학 연구방법 - 롸이팅** (AI4Psych Writing Course)
