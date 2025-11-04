# Academic Writing Multi-Agent System

**Created by**: Jeongyeon Shin
**Course**: 심리과학 연구방법 - 롸이팅 (Psychology Research Writing)
**Institution**: SNU Connectome Lab

---

## 📖 Overview

이 시스템은 학술 논문 작성을 돕는 **6개의 기능 기반 AI 에이전트**로 구성된 multi-agent 협업 시스템입니다.

### Why Multi-Agent?

단일 AI는 다음과 같은 한계가 있습니다:
- 글쓰기와 검토를 동시에 하면 자기 교정이 어려움
- 문헌 정확성과 문체를 동시에 챙기기 어려움
- 논리적 흐름과 통계적 정확성을 함께 보기 어려움

**Multi-agent 시스템은 각 에이전트가 전문 분야에 집중하여 더 정확하고 체계적인 글쓰기를 지원합니다.**

---

## 🤖 Agent Architecture

### Function-Based Design (NOT Section-Based)

각 에이전트는 **논문의 특정 섹션이 아닌 특정 기능**을 담당합니다:

```
┌─────────────────────────────────────────────────────────────┐
│                    User's Research Input                     │
│             (Abstract, Introduction, Methods, etc.)          │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
            ┌───────────────────────┐
            │  Coordinator Agent    │
            │  (Orchestrator)       │
            └───────────┬───────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Writer       │ │ Literature   │ │ Quality      │
│ Agent        │ │ Validator    │ │ Checker      │
│              │ │ Agent        │ │ Agent        │
└──────────────┘ └──────────────┘ └──────────────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Logic        │ │ Statistics   │ │ Final        │
│ Auditor      │ │ Reviewer     │ │ Polish       │
│ Agent        │ │ Agent        │ │ Agent        │
└──────────────┘ └──────────────┘ └──────────────┘
```

### 6 Agents and Their Roles

| Agent | Primary Function | Training Materials | Output |
|-------|-----------------|-------------------|---------|
| **1. Writer Agent** | Draft generation, content creation | Week 1-6 lecture notes, CCC structure | Draft text with clear structure |
| **2. Literature Validator** | Citation accuracy, gap validation | Week 3 gap discovery templates | Literature validation report |
| **3. Quality Checker** | Writing quality, clarity, concision | Duke Writing principles, Elements of Style | Quality improvement suggestions |
| **4. Logic Auditor** | Logical flow, argument coherence | Ten Simple Rules, Week 3-4 worksheets | Logic analysis report |
| **5. Statistics Reviewer** | Statistical rigor, reproducibility | Week 4 reproducibility checklist | Statistical validation report |
| **6. Coordinator Agent** | Workflow orchestration, integration | All workflow templates | Final integrated output |

---

## 📁 Folder Structure

```
group/jeongyeonshin/
├── README.md                          # This file
├── materials/                         # Professor's course materials (8 PDFs)
│   ├── Duke_Writing_*.pdf
│   ├── Paper_writing_guide.pdf
│   ├── Ten_simple_rules_for_writing.pdf
│   └── ...
│
├── agents/                            # Agent system prompts
│   ├── 01_writer_agent.md
│   ├── 02_literature_validator.md
│   ├── 03_quality_checker.md
│   ├── 04_logic_auditor.md
│   ├── 05_statistics_reviewer.md
│   └── 06_coordinator_agent.md
│
├── orchestrator/                      # Python orchestration system
│   ├── multi_agent_orchestrator.py   # Main orchestrator
│   ├── agent_base.py                  # Base agent class
│   ├── workflow.py                    # Workflow definitions
│   └── requirements.txt               # Python dependencies
│
├── examples/                          # Usage examples
│   ├── abstract_revision_example.md
│   ├── methods_bulletproofing_example.md
│   └── full_paper_workflow_example.md
│
└── week1-6/                           # Weekly assignments
    ├── week1/
    ├── week2/
    └── ...
```

---

## 🚀 Quick Start

### 1. Installation

```bash
cd group/jeongyeonshin/orchestrator
pip install -r requirements.txt
```

### 2. Set API Keys

```bash
export OPENAI_API_KEY="your-api-key"
# or
export ANTHROPIC_API_KEY="your-api-key"
```

### 3. Run Multi-Agent System

```python
from orchestrator.multi_agent_orchestrator import MultiAgentOrchestrator

# Initialize orchestrator
orchestrator = MultiAgentOrchestrator()

# Run full workflow
result = orchestrator.run_full_workflow(
    input_text="Your abstract draft here...",
    section="abstract",
    workflow="revision"
)

print(result.final_output)
print(result.agent_reports)
```

---

## 💡 Usage Scenarios

### Scenario 1: Abstract Revision (Week 2)

```python
orchestrator.run_workflow(
    workflow="abstract_revision",
    input_text="[Your abstract]",
    focus_areas=["broad_significance", "opening_pattern"]
)
```

**Agent Pipeline**:
1. Writer Agent: Revise using Nature/Science strategies
2. Quality Checker: Apply Duke Writing principles
3. Logic Auditor: Verify CCC structure
4. Coordinator: Integrate feedback

### Scenario 2: Methods Section Bulletproofing (Week 4)

```python
orchestrator.run_workflow(
    workflow="methods_bulletproofing",
    input_text="[Your methods section]",
    focus_areas=["reproducibility", "controls"]
)
```

**Agent Pipeline**:
1. Writer Agent: Enhance clarity and detail
2. Statistics Reviewer: Check reproducibility checklist
3. Logic Auditor: Verify logical flow
4. Quality Checker: Improve readability
5. Coordinator: Integrate all feedback

### Scenario 3: Literature Review Gap Discovery (Week 3)

```python
orchestrator.run_workflow(
    workflow="gap_discovery",
    input_text="[Your literature review]",
    focus_areas=["conceptual_gap", "validation"]
)
```

**Agent Pipeline**:
1. Literature Validator: 3-stage gap validation
2. Logic Auditor: Check gap argumentation
3. Writer Agent: Strengthen gap statement
4. Coordinator: Synthesize findings

---

## 📊 Agent Details

### 1. Writer Agent

**Training Materials**:
- Week 1: Duke Writing principles (Subjects/Actions, Cohesion, Concision)
- Week 2: Nature/Science abstract strategies
- Week 3-6: Section-specific strategies
- Ten Simple Rules for Structuring Papers
- CCC (Context-Content-Conclusion) structure

**Key Capabilities**:
- Generate drafts following IMRaD structure
- Apply CCC pattern to each section
- Use parallel construction and active voice
- Optimize logical flow (no zig-zag)

**Prompt Template**: [agents/01_writer_agent.md](agents/01_writer_agent.md)

---

### 2. Literature Validator Agent

**Training Materials**:
- Week 3: Gap discovery templates
- Week 3: 3-stage validation workflow
- Week 3: False gap prevention checklist

**Key Capabilities**:
- Validate citations and claims
- Distinguish conceptual vs incremental gaps
- Run 3-stage gap validation
- Detect false gaps

**Prompt Template**: [agents/02_literature_validator.md](agents/02_literature_validator.md)

---

### 3. Quality Checker Agent

**Training Materials**:
- Duke Writing Lesson 1: Subjects and Actions
- Duke Writing Lesson 2: Cohesion and Coherence
- Duke Writing Lesson 3: Concision and Simplicity
- Elements of Style (Strunk)

**Key Capabilities**:
- Check clarity and concision
- Verify active voice usage
- Analyze old→new information flow
- Detect needless words

**Prompt Template**: [agents/03_quality_checker.md](agents/03_quality_checker.md)

---

### 4. Logic Auditor Agent

**Training Materials**:
- Ten Simple Rules (Rule 4: Logical flow)
- Week 3-4: Validation worksheets
- CCC structure requirements

**Key Capabilities**:
- Analyze argument structure
- Detect logical gaps or jumps
- Verify claim-evidence alignment
- Check paragraph-level coherence

**Prompt Template**: [agents/04_logic_auditor.md](agents/04_logic_auditor.md)

---

### 5. Statistics Reviewer Agent

**Training Materials**:
- Week 4: Reproducibility checklist
- Week 4: Top 10 rejection reasons
- Week 4: Control validation strategies

**Key Capabilities**:
- Check statistical methods appropriateness
- Verify reproducibility (6 critical elements)
- Validate control conditions
- Detect overclaiming

**Prompt Template**: [agents/05_statistics_reviewer.md](agents/05_statistics_reviewer.md)

---

### 6. Coordinator Agent

**Training Materials**:
- All workflow templates from Week 1-6
- Integration strategies

**Key Capabilities**:
- Orchestrate agent workflows
- Resolve conflicting feedback
- Prioritize revisions
- Generate final integrated output

**Prompt Template**: [agents/06_coordinator_agent.md](agents/06_coordinator_agent.md)

---

## 🔄 Workflows

### Pre-defined Workflows

1. **`abstract_revision`** (Week 2)
   - Writer → Quality → Logic → Coordinator

2. **`gap_discovery`** (Week 3)
   - Literature Validator → Logic → Writer → Coordinator

3. **`methods_bulletproofing`** (Week 4)
   - Writer → Statistics → Logic → Quality → Coordinator

4. **`results_validation`** (Week 4)
   - Statistics → Logic → Quality → Coordinator

5. **`discussion_enhancement`** (Week 5)
   - Writer → Logic → Quality → Coordinator

6. **`full_paper_review`** (Week 6)
   - All agents in sequence → Coordinator

### Custom Workflows

```python
# Define custom agent sequence
orchestrator.run_custom_workflow(
    agent_sequence=[
        ("writer", {"focus": "introduction"}),
        ("literature_validator", {"depth": "deep"}),
        ("logic_auditor", {"check_transitions": True}),
        ("coordinator", {})
    ],
    input_text="[Your text]"
)
```

---

## 📚 Educational Integration

This system integrates seamlessly with the course structure:

| Week | Course Focus | Multi-Agent Support |
|------|--------------|-------------------|
| Week 1 | Human-centered writing | Quality Checker applies Duke principles |
| Week 2 | Nature/Science abstracts | Writer Agent uses top-tier strategies |
| Week 3 | Gap discovery | Literature Validator runs 3-stage workflow |
| Week 4 | Methods/Results | Statistics Reviewer applies bulletproofing |
| Week 5 | Discussion | Writer + Logic agents collaborate |
| Week 6 | Peer review | Full multi-agent pipeline |

---

## 🎯 Design Principles

### 1. Function-Based (Not Section-Based)

Each agent can work on **any section** of the paper:
- ✅ Quality Checker can review Abstract, Methods, or Discussion
- ✅ Logic Auditor can analyze Introduction or Results
- ✅ Writer Agent can draft any IMRaD section

This is different from section-based agents (Abstract Agent, Methods Agent, etc.)

### 2. Specialist Expertise

Each agent is trained on **specific course materials** relevant to its function:
- Quality Checker = Duke Writing + Elements of Style
- Literature Validator = Week 3 gap discovery materials
- Statistics Reviewer = Week 4 reproducibility checklists

### 3. Collaborative Workflow

Agents work **in sequence** and build on each other's outputs:
```
Input → Agent 1 → Agent 2 → Agent 3 → Coordinator → Final Output
```

### 4. Transparency

All agent outputs are preserved:
- Individual agent reports
- Reasoning chains
- Conflicting feedback resolution
- Final integration rationale

---

## 🛠️ Technical Details

### Agent Implementation

All agents inherit from `AgentBase` class:

```python
class AgentBase:
    def __init__(self, name, system_prompt_path):
        self.name = name
        self.system_prompt = self.load_prompt(system_prompt_path)

    def process(self, input_text, context={}):
        # Call LLM with system prompt + input
        # Return structured output
        pass
```

### System Prompts

Each agent has a markdown file with:
- Role definition
- Training materials summary
- Task instructions
- Output format specification
- Examples

### Orchestrator

```python
class MultiAgentOrchestrator:
    def __init__(self):
        self.agents = self.load_all_agents()
        self.workflows = self.load_workflows()

    def run_workflow(self, workflow_name, input_text):
        workflow = self.workflows[workflow_name]
        context = {"input": input_text}

        for agent_name, params in workflow:
            agent = self.agents[agent_name]
            result = agent.process(context["input"], params)
            context[agent_name] = result
            context["input"] = result.output_text

        coordinator = self.agents["coordinator"]
        final_result = coordinator.integrate(context)
        return final_result
```

---

## 📝 Examples

See [examples/](examples/) folder for detailed examples:

- **`abstract_revision_example.md`**: Step-by-step abstract revision with agent outputs
- **`methods_bulletproofing_example.md`**: Methods section improvement workflow
- **`full_paper_workflow_example.md`**: Complete paper review process

---

## 🚧 Future Enhancements

- [ ] Add GUI interface for easier interaction
- [ ] Implement feedback loop for iterative revision
- [ ] Add support for multiple LLM providers (OpenAI, Anthropic, local models)
- [ ] Create web dashboard for visualizing agent interactions
- [ ] Add citation validation using external databases (PubMed, Google Scholar)
- [ ] Implement version control for tracking revision history

---

## 📖 References

### Course Materials

This system is built on materials from "심리과학 연구방법 - 롸이팅" course:
- Duke University Writing Center lessons
- Kording & Mensh (2015). Ten simple rules for structuring papers. *PLOS Computational Biology*.
- Strunk, W. *The Elements of Style*.
- Course lecture notes (Week 1-6)

### Repository

- **GitHub**: https://github.com/snuconnectome/AI4Psych_writing
- **Folder**: `group/jeongyeonshin/`

---

## 💬 Questions?

For questions or feedback:
- 📧 Email: [your email]
- 💬 GitHub Issues: https://github.com/snuconnectome/AI4Psych_writing/issues
- 🎓 Course instructor: [Professor's name]

---

**Last Updated**: 2025-01-04
**Version**: 1.0
**License**: MIT (for educational use)
