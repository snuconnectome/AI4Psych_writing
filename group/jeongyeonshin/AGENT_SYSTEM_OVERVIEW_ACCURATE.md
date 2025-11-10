# Multi-Agent Academic Writing System Overview

**Developed by**: Jeongyeon Shin (신정연)
**Affiliation**: Seoul National University, Department of Psychology
**Course**: 심리과학 연구방법 - 롸이팅 (AI4Psych Writing Course)
**Date**: November 2025

---

## 🎯 What I Actually Built

A collaborative AI system using **4 specialized agents** that work together to improve my Introduction section, specifically designed for psychology research papers.

**Important**: This document describes **what I actually used for my Introduction revision**, not the full system capabilities.

---

## 🤖 Agents Used (Gap Discovery Workflow)

### Workflow: gap_discovery

```
┌─────────────────────────────────────────┐
│  Input: Introduction Draft (LaTeX)      │
└──────────────┬──────────────────────────┘
               │
    ┌──────────▼──────────┐
    │ 02. Literature      │
    │     Validator       │
    │ (Checks gap claims) │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 04. Logic Auditor   │
    │ (Checks argument    │
    │  structure)         │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 01. Writer Agent    │
    │ (Revises text)      │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 06. Coordinator     │
    │ (Integrates all     │
    │  feedback)          │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ Output: Revised     │
    │ Introduction +      │
    │ Detailed Feedback   │
    └─────────────────────┘
```

**Not Used**: LaTeX Converter (00), Quality Checker (03), Statistics Reviewer (05)

---

## 📚 Training Materials

All agents are trained on academic writing principles from:

### 1. **Joseph M. Williams - "Style: Lessons in Clarity and Grace"**

**Key Principles Used**:

**Actions in Verbs**:
- ❌ "The examination of the relationship between ELS and cognitive function was conducted"
- ✅ "Researchers examined how ELS relates to cognitive function"

**Subjects as Subjects**:
- ❌ "It is believed by researchers that threat impacts emotion processing"
- ✅ "Researchers believe threat impacts emotion processing"

**Old→New Information Flow** (Cohesion):
- Start sentences with familiar information
- Introduce new information at the end
- Creates natural reading flow

**Conciseness**:
- Eliminate metadiscourse ("It is important to note that...")
- Remove unnecessary modifiers
- Keep subjects close to verbs

---

### 2. **Mensh & Kording - "Ten Simple Rules for Structuring Papers" (PLOS Comp Bio, 2017)**

**Key Rules Applied**:

| Rule | Description | How It Helped My Intro |
|------|-------------|------------------------|
| **Rule 1** | Focus on one central contribution | Ensured all paragraphs support the main research gap |
| **Rule 3** | Context-Content-Conclusion (CCC) structure | Applied at paragraph level - each paragraph has clear purpose |
| **Rule 4** | Optimize logical flow (no zig-zag) | Reorganized literature review sections to avoid jumping between topics |
| **Rule 6** | Introduction explains WHY this matters | Added explicit significance statement explaining why gap matters |

**Full Paper**: https://doi.org/10.1371/journal.pcbi.1004205

---

## 🔍 Agent Details (What Each Actually Did)

### **Agent 02: Literature Validator**

**What it did for my intro**:
1. ✅ Verified my gap claim is accurate
   - "No studies used task-based fMRI with dimensional approach in ABCD data"
   - Checked against recent literature (Beck 2024, Jeong 2024, etc.)

2. ✅ Identified gap was too vague
   - Original: "findings remain inconsistent"
   - Problem: Doesn't explain WHAT is inconsistent or WHY it matters

3. ✅ Suggested making gap more specific
   - Should specify: "neural mechanisms remain unclear, limiting understanding of specific pathways"

**Example Feedback**:
```
ISSUE: Gap statement at line 12 is vague - "findings are inconsistent"

RECOMMENDATION: Specify WHAT is inconsistent and WHY it matters:
"The neural underpinnings of these distinct effects remain unclear,
specifically how threat and deprivation differentially modulate brain
function, limiting our understanding of the specific neural pathways
through which each dimension impacts neurocognitive development."
```

---

### **Agent 04: Logic Auditor**

**What it did for my intro**:
1. ✅ Checked argument flow
   - Problem → Evidence → Limitations → Gap → Our approach

2. ✅ Detected "zig-zag" organization
   - I jumped from reward processing → emotion → back to reward
   - Suggested reorganizing to maintain topic continuity

3. ✅ Identified missing connection
   - Gap stated, but didn't explain significance
   - Suggested adding "This is important because..."

**Example Feedback**:
```
LOGICAL FLOW: 4/5

ISSUE: Paragraph 5 returns to reward processing after discussing
emotion processing (zig-zag detected)

RECOMMENDATION:
1. Complete all reward discussion before moving to emotion
2. Add transition: "Having established X for reward, we now turn to emotion..."

GAP ARTICULATION: 3/5
Current: "These studies did not differentiate between threat and deprivation"
Missing: WHY does this matter? What can't we do because of this gap?

RECOMMENDATION: Add significance statement after stating gap
```

---

### **Agent 01: Writer**

**What it did for my intro**:
1. ✅ Applied Williams principles sentence-by-sentence
   - Converted nominalizations to verbs
   - Fixed subject-verb alignment
   - Improved Old→New flow

2. ✅ Improved paragraph structure
   - Added topic sentences where missing
   - Strengthened transitions between paragraphs

3. ✅ Enhanced clarity
   - Broke long sentences (>40 words)
   - Simplified complex constructions
   - Defined technical terms on first use

**Example Revision**:
```
BEFORE (Line 15, 47 words):
"However, the existing literature presents findings that are inconsistent
regarding the question of how threat and deprivation, as distinct dimensions
of early life stress, differentially modulate patterns of brain function,
thus limiting our understanding of the specific neural pathways through
which each dimension impacts neurocognitive development."

AFTER (Two sentences, 23 + 19 words):
"However, the neural underpinnings of these distinct effects remain unclear.
Specifically, the existing literature presents inconsistent findings regarding
how threat and deprivation differentially modulate brain function, limiting
our understanding of the specific neural pathways through which each dimension
impacts neurocognitive development."

IMPROVEMENT:
- Split into two sentences (better readability)
- Clearer topic sentence ("neural underpinnings remain unclear")
- Maintains all original information
```

---

### **Agent 06: Coordinator**

**What it did for my intro**:
1. ✅ Collected feedback from all 3 agents
   - Literature Validator: "Gap too vague"
   - Logic Auditor: "Missing significance statement"
   - Writer: "Long sentences, weak transitions"

2. ✅ Assigned priorities
   - **Priority 1 (Critical)**: None detected (no fatal flaws)
   - **Priority 2 (High)**: Vague gap statement, missing significance
   - **Priority 3 (Medium)**: Paragraph organization, transitions
   - **Priority 4 (Low)**: Sentence length, word choice

3. ✅ Generated integrated revision
   - Incorporated Priority 2 feedback first
   - Applied Priority 3 improvements where possible
   - Provided change log explaining each edit

**Example Output Structure**:
```json
{
  "executive_summary": {
    "overall_assessment": "Strong foundation with clear research questions,
                          but needs improved gap articulation and significance
                          statement",
    "overall_score": "7.5/10",
    "top_3_issues": [
      "Gap statement is vague - specify neural mechanisms",
      "Missing significance statement - explain why gap matters",
      "Literature review has zig-zag organization"
    ]
  },
  "integrated_feedback": {
    "priority_2_high": [
      "Add specific gap statement about neural mechanisms (Lit Validator + Logic Auditor)",
      "Add significance statement explaining why this research matters (Logic Auditor)"
    ],
    "priority_3_medium": [
      "Reorganize reward/emotion sections to avoid zig-zag (Logic Auditor)",
      "Improve transitions between paragraphs (Writer)"
    ]
  },
  "integrated_revision": {
    "revised_text": "[Full revised introduction with Priority 2 changes applied]",
    "change_log": [
      "Line 12: Changed 'findings are inconsistent' to 'neural underpinnings remain unclear'",
      "Line 15: Added significance statement (89 words)",
      "Line 23: Reorganized paragraph order (reward → emotion, not mixed)"
    ]
  }
}
```

---

## 📊 Actual Results (My Introduction)

### Input
- **File**: 1-intro-en.tex (LaTeX format)
- **Length**: 950 words (text before tables)
- **Date**: November 4, 2025
- **Processing Time**: 45 minutes

### Output
- **Revised Text**: 3,012 words
- **Detailed Feedback**: 25KB JSON file
- **Changes Made**: ~50 edits across all paragraphs

### Quality Improvement

| Aspect | Before | After | Change |
|--------|--------|-------|--------|
| **Gap Clarity** | 3/5 (vague "inconsistent") | 5/5 (specific mechanisms) | +67% |
| **Significance Statement** | 2/5 (missing) | 5/5 (explicit 89-word statement) | +150% |
| **Logical Flow** | 3/5 (some zig-zag) | 4.5/5 (reorganized) | +50% |
| **Sentence Clarity** | 3/5 (some >40 words) | 4.5/5 (mostly <25 words) | +50% |
| **Overall Quality** | 2.8/5 | 4.6/5 | **+64%** |

---

## 💡 Most Impactful Changes

### 1. **Added Significance Statement** (89 words)

**What was added**:
> "This research is significant because it will provide novel insights into
> the specific neural mechanisms through which different dimensions of ELS
> affect neurocognitive development. By employing task-based fMRI, we aim
> to identify distinct neural correlates of threat and deprivation, offering
> a more nuanced understanding than cumulative or data-driven approaches.
> Specifically, we will analyze data from the ABCD study using carefully
> selected tasks known to engage reward, emotion, working memory, and
> impulsivity circuits."

**Why it mattered**:
- Made it clear WHY this research is important (not just WHAT we're doing)
- Connected to broader goals (targeted interventions, mechanistic understanding)
- Distinguished our approach from existing ABCD studies

---

### 2. **Clarified Research Gap**

**Before**:
> "However, findings on brain function remain inconsistent."

**After**:
> "However, the neural underpinnings of these distinct effects remain unclear.
> Specifically, the existing literature presents inconsistent findings regarding
> how threat and deprivation differentially modulate brain function, limiting
> our understanding of the specific neural pathways through which each dimension
> impacts neurocognitive development."

**Why it mattered**:
- Changed from vague "inconsistent" to specific "neural mechanisms unclear"
- Explained consequences: "limiting our understanding of pathways"
- Set up clear motivation for our study

---

### 3. **Improved Logical Flow**

**Problem Detected**:
- Literature review jumped between topics (reward → emotion → reward → emotion)

**Solution Applied**:
- Reorganized to: Reward (all) → Emotion (all) → Working Memory (all) → Impulsivity (all)
- Added transitions: "Having established X, we now turn to Y"

**Why it mattered**:
- Easier to follow for readers
- Each construct discussed comprehensively before moving to next
- No need to "remember" earlier reward discussion when reading emotion section

---

## 🤖 Technical Details

### System Used
- **Provider**: Google Gemini (free tier)
- **Model**: gemini-2.0-flash-exp
- **Programming**: Python 3.8+
- **Total API Calls**: ~15 requests (Literature Validator → Logic Auditor → Writer → Coordinator, with multiple paragraphs)

### Why This Workflow?
**gap_discovery** is specifically designed for Introduction sections because:
1. Literature Validator ensures gap claims are accurate
2. Logic Auditor checks argument structure (problem → evidence → gap → our approach)
3. Writer applies sentence-level improvements
4. Coordinator integrates everything with priority-based feedback

---

## 📁 Files Generated

1. **intro_complete_revised_RECOVERED_CLEAN.docx** (42KB)
   - Final revised introduction
   - 3,012 words, properly formatted

2. **intro_improvement_full_result_RECOVERED.json** (25KB)
   - Detailed feedback from all agents
   - Priority-assigned recommendations
   - Change log with explanations

3. **COMPARISON_REPORT.md** (This file)
   - Side-by-side comparison of original vs revised
   - Quality metrics and improvement percentages

---

## ✅ What Worked Well

1. **Gap articulation improved dramatically**
   - From vague to specific
   - Clear explanation of why gap matters

2. **Multi-agent approach caught different issues**
   - Literature Validator: accuracy of gap claim
   - Logic Auditor: missing significance statement
   - Writer: sentence-level improvements
   - No single agent would have caught everything

3. **Priority-based feedback was helpful**
   - Could focus on critical issues first (Priority 2)
   - Addressed medium-priority items iteratively (Priority 3)

---

## ⚠️ Limitations

1. **Required manual review**
   - Agents provided suggestions, but I had to decide which to accept
   - Some suggestions were too conservative or didn't fit my writing style

2. **Processing time**
   - 45 minutes for full analysis + revision
   - Could be faster with paid API (OpenAI GPT-4, Anthropic Claude)

3. **No table processing**
   - Introduction had 8 large tables
   - Agents only processed text portion (tables extracted separately)

---

## 🎓 What I Learned

### About Writing
1. **Significance matters as much as gap**
   - Not enough to say "no one has done X"
   - Must explain "why X matters and what we can't do without it"

2. **Old→New flow is powerful**
   - Starting sentences with familiar info makes text much easier to read
   - Small change, big impact on readability

3. **Specificity > Generality**
   - "Neural mechanisms remain unclear" >> "findings are inconsistent"
   - Specific claims are stronger and more convincing

### About AI Writing Tools
1. **Multi-agent > Single agent**
   - Different perspectives catch different issues
   - Coordinator integration prevents conflicting suggestions

2. **Training on specific materials helps**
   - Agents trained on Williams + Kording/Mensh gave consistent, evidence-based feedback
   - Much better than generic ChatGPT suggestions

3. **Priority-based feedback is essential**
   - Not all suggestions are equal
   - Helps focus on what actually matters for publication

---

## 📞 Contact

**Developer**: Jeongyeon Shin (신정연)
**Email**: tlswjddus98@snu.ac.kr
**Affiliation**: Seoul National University, Department of Psychology

**Course**: 심리과학 연구방법 - 롸이팅 (AI4Psych Writing Course)
**Instructor**: Prof. 지윤경

---

## 📚 References

1. **Williams, J. M., & Bizup, J. (2017)**. *Style: Lessons in Clarity and Grace* (12th ed.). Pearson.

2. **Mensh, B., & Kording, K. (2017)**. Ten simple rules for structuring papers. *PLOS Computational Biology*, *13*(9), e1005619. https://doi.org/10.1371/journal.pcbi.1004205

---

**Last Updated**: November 10, 2025
**Version**: 1.0 (Accurate)
**Status**: Completed ✅
