# Week 2 Materials Integration Prompt
## Consolidating Scattered Files into Classroom-Ready Teaching Materials

---

## Context

You are an expert instructional designer with 15+ years of experience designing graduate-level seminar materials for psychology programs at research universities (Stanford, MIT, Cambridge). You specialize in:
- **Live teaching optimization**: Materials that instructors can follow minute-by-minute without switching files
- **Cognitive load management**: Embedding resources at point of use to reduce instructor mental burden
- **Bilingual education**: Korean graduate students writing for English-language international journals
- **AI-enhanced pedagogy**: Integrating AI tools strategically into traditional teaching

## Problem Statement

The Week 2 course materials for "심리과학 연구방법-롸이팅" are currently scattered across 5+ separate files:
1. `lesson_slides_15min.md` (12KB) - Marp slides for lecture, currently has placeholder examples
2. `lecture_notes.md` (22KB) - Instructor guide, missing workshop details
3. `peer_feedback_session_plan.md` (115KB) - Comprehensive peer review session design
4. `selected_papers.md` (18KB) - 3 Nature/Science abstract pairs for analysis
5. `abstracts_usage_guide.md` (19KB) - Minute-by-minute timing for abstract usage
6. `practice.md` (4KB) - Old generic template (to be replaced)

**Current problem**: An instructor cannot teach the 90-minute class using only the main files. They must constantly switch between 5+ documents, losing their place, missing timing cues, and experiencing cognitive overload.

**Desired outcome**: TWO comprehensive, self-contained files that an instructor can use to teach the entire 90-minute class without opening any other documents.

---

## Task

Integrate all materials into two classroom-ready files following expert instructional design principles:

### File 1: `lesson_slides_15min.md` (TARGET: 15-20KB)
**Purpose**: Marp presentation projected for students during 15-minute lecture
**Audience**: Students (visual reference during lecture)
**Updates needed**:
- Replace placeholder examples with real Pair B abstract (AI Persuasiveness)
- Add quantitative results examples (64.4%, 81.2% increase, 95% CI)
- Add broad significance examples (governance, platform design)
- Maintain Marp formatting (---, h1, h2, code blocks, tables)
- Keep visual and concise (slides for projection, not reading)

### File 2: `lecture_notes.md` (TARGET: 60-80KB)
**Purpose**: Comprehensive instructor's teaching guide for entire 90-minute class
**Audience**: Instructor (step-by-step execution guide)
**Complete restructuring needed**:
- Part I: Overview (course context, learning objectives, 90-min structure)
- Part II: Lecture Materials (0-15 min) with teaching scripts
- Part III: Workshop Materials (15-85 min) with minute-by-minute timeline
  - Exemplar Calibration (15-35 min) - Pair A, C abstracts EMBEDDED
  - Peer Review Round 1 (35-60 min) - Rubric & Protocol EMBEDDED
  - AI Revision (60-75 min) - Prompt templates EMBEDDED
  - Validation Round 2 (75-85 min) - Quick feedback format
- Part IV: Wrap-up (85-90 min) & Assignment
- Part V: Appendices (pre-class prep, troubleshooting, Notion setup)

---

## Source Materials to Integrate

### Priority 1: MUST INTEGRATE (Core teaching materials)

**From `peer_feedback_session_plan.md`**:
- Section 2: 70-Minute Workshop Timeline (minutes 0-70) → lecture_notes.md Part III
- Section 3: Peer Review Rubric (5 dimensions, 1-5 scale) → lecture_notes.md embedded at minute 28
- Section 4: Editor Protocol Template → lecture_notes.md embedded at minute 30
- Section 7: AI Integration Strategy (5 prompt templates) → lecture_notes.md at minute 60
- Section 8: Instructor Facilitation Scripts → lecture_notes.md at each transition point

**From `selected_papers.md`**:
- Pair A: Memory & Temporal Context (Lines 15-69) → lecture_notes.md at minute 15
- Pair B: AI Persuasiveness (Lines 70-131) → lesson_slides AND lecture_notes
- Pair C: Sleep & Memory Consolidation (Lines 133-187) → lecture_notes.md at minute 23

**From `abstracts_usage_guide.md`**:
- Slide modification suggestions (Lines 44-155) → lesson_slides_15min.md updates
- Minute-by-minute instructor actions (Lines 158-300) → lecture_notes.md Part II-III
- Socratic question templates → lecture_notes.md embedded scripts

### Priority 2: REFERENCE (Context only, don't duplicate)

**From `practice.md`**:
- OLD template, DO NOT integrate
- Use only for understanding original intent
- New materials replace this entirely

---

## Integration Principles

### 1. CHRONOLOGICAL FLOW
- Materials appear in order of actual classroom use
- Minute markers throughout: "Minutes 15-17:", "Minutes 28-30:"
- No need to jump around document during class
- Example: Rubric appears at minute 28 (when instructor needs it), not in appendix

### 2. EMBEDDED RESOURCES
- Abstract texts embedded at point of use, not referenced
- Rubrics and protocols in bordered boxes where used
- Scripts in quotation format: "Say: 'Today you'll experience...'"
- No cross-references like "see section 5.3" - everything self-contained

### 3. INSTRUCTOR-FRIENDLY FORMATTING
- Clear section headers with time markers
- Boxed critical materials (rubric, protocol, abstracts)
- Action verbs: "Project", "Distribute", "Circulate", "Monitor"
- Transition scripts between activities
- Quick reference tables for materials needed

### 4. BILINGUAL SUPPORT
- Korean instructions for instructor actions
- Bilingual student-facing materials (rubric, protocol)
- Korean cultural considerations embedded where relevant
- English examples with Korean explanations

### 5. AI INTEGRATION
- AI prompt templates at exact usage point (minute 60)
- Guidance on evaluating AI output
- Examples of good/bad AI responses
- NOT generic AI concepts (students already learned from 윤경생)

---

## Detailed Integration Specifications

### TASK 1: Update `lesson_slides_15min.md`

**Slide 13-14 Update** (Lines 91-136 in current file):
```markdown
CURRENT:
### ❌ 일반 저널 Opening
Spatial memory in rodents has been extensively studied...

### ✅ Nature Opening (Problem-Driven)
Despite decades of research, the molecular mechanisms...
```

**NEW (from abstracts_usage_guide.md Lines 44-90)**:
```markdown
## Opening 차이: Real Example from Nature Human Behaviour (2025)

### ❌ 일반 저널 Opening (가상 예시)
Large language models like GPT-4 are becoming increasingly popular.
Previous research has investigated AI persuasion capabilities.

### ✅ Nature Human Behaviour Opening (Salvi et al., 2025)
Early work has found that large language models (LLMs) can generate
persuasive content. However, evidence on whether they can also personalize
arguments to individual attributes remains limited, despite being crucial
for assessing misuse.

**강점**:
- Problem-driven 패턴: AI 오용 위험성
- "Despite being crucial" → 중요성 즉시 명확
- Broad impact: AI governance, platform design
- No brain imaging: 순수 행동 실험 (N=900)으로도 Nature급 가능
```

**Slide 18-19 Update** (Lines 336-386):
- Add Pair B quantitative results: "64.4%", "81.2% relative increase", "95% CI"
- Show contrast between vague ("significant effects") and specific (Pair B numbers)

**Slide 20 Update** (Lines 280-333):
- Add Pair B broad significance: "implications for governance and design of online platforms"
- Explain how this extends beyond AI researchers to policymakers, ethicists, platform designers

**Format preservation**:
- Keep Marp YAML header (lines 1-29)
- Maintain `---` slide separators
- Keep existing style formatting
- Preserve table structures and code blocks

---

### TASK 2: Restructure `lecture_notes.md`

**Current structure** (22KB):
```
# Week 2: AI 활용 I - 초록 작성
- 개요
- 학습 목표
- Abstract Autopsy Project (40분 버전 - OLD)
- AI Writing Workshop (30분 버전 - OLD)
- 과제
```

**NEW structure** (60-80KB):

```markdown
# Week 2: Nature/Science급 초록 작성 - 완전 강의안
## 90분 수업 전체 가이드 (학생 초록 피드백 통합 버전)

---

## PART I: COURSE OVERVIEW (5 pages)

### 1.1 수업 컨텍스트
- 심리과학 연구방법-롸이팅 Week 2
- Target: 석사/박사 대학원생 6-12명
- 전제: 학생들이 자신의 초록 초안을 가지고 옴
- 전제: 윤경생 박사님 강의에서 AI 기초 이미 학습

### 1.2 학습 목표
1. 4가지 Opening 패턴 식별 (Problem/Gap/Opportunity/Challenge)
2. Broad significance framing 평가
3. 정량적 결과 vs 모호한 표현 구분
4. 탑티어 저널 편집자 기준으로 피드백 제공
5. AI로 피드백 반영 및 초록 개선

### 1.3 전체 구조 (90분)
| 시간 | 활동 | 주요 자료 |
|------|------|----------|
| 0-15분 | 강의 (Opening + Significance) | lesson_slides_15min.md |
| 15-35분 | Exemplar Calibration | Pair A, C 초록 |
| 35-60분 | Peer Review Round 1 | 5-dimension Rubric, Editor Protocol |
| 60-75분 | AI-Enhanced Revision | 5 prompt templates |
| 75-85분 | Peer Review Round 2 | Validation checklist |
| 85-90분 | Wrap-up & Assignment | 참고자료 링크 |

---

## PART II: LECTURE MATERIALS (0-15분)

### 2.1 사전 준비
**수업 2일 전**:
- [ ] lesson_slides_15min.md를 Marp로 PDF 생성
- [ ] Notion Week 2 page에 학생 초록 제출 요청 (48시간 전)
- [ ] Pair B 초록 슬라이드에 임베드 확인

**수업 당일**:
- [ ] 프로젝터 연결 확인
- [ ] Notion 접속 테스트
- [ ] 타이머 준비 (스마트폰 또는 컴퓨터)

### 2.2 Minute-by-Minute Teaching Guide

#### **Minutes 0-2: Opening & Orientation**

**[강의자 행동]**:
- 출석 확인
- Notion 초록 제출 확인 ("모두 제출했나요?")
- 오늘 수업 구조 간단 소개

**[Script]**:
> "오늘은 여러분이 가져온 초록을 Nature/Science 편집자의 기준으로 평가하고 개선하는 시간입니다.
> 15분 강의 → 70분 워크샵 → 5분 정리 순서로 진행합니다."

**[Slide]**: Title slide (lesson_slides_15min.md Slide 1)

---

#### **Minutes 2-5: 학습 목표 제시**

**[강의자 행동]**:
- Slide 2-3 투사 (학습 목표)
- 강조: "AI 개념 설명 없음, 실전 전략만"

**[Script]**:
> "윤경생 박사님 강의에서 이미 프롬프트 엔지니어링을 배웠으므로, 오늘은 개념 설명 없이
> '어떻게 탑 5% 초록을 쓸 것인가'에만 집중합니다."

**[Slide]**: Slides 2-3 (학습 목표, AI 개념 생략 안내)

---

#### **Minutes 5-7: Opening 패턴 소개 (Pair B 사용)**

**[강의자 행동]**:
- Slide 13-14 투사 (Pair B 초록 포함)
- Problem-driven 패턴 강조

**[Script]**:
> "이것은 실제 Nature Human Behaviour 2025년 논문입니다.
> GPT-4가 인간보다 설득력 있다는 연구 - 여러분이 ChatGPT 쓰시죠? 바로 그 GPT-4입니다.
> 주목: 'Despite being crucial for assessing misuse' - 왜 중요한지 즉시 명확합니다."

**[Slide]**: Slide 13-14 (NEW - Pair B 초록 포함)

**[Teaching Tip]**:
- 학생들이 "순수 행동 실험도 Nature급 가능"을 인식하도록 강조
- N=900, 64.4%, 81.2% increase 등 정량적 결과 지적

---

#### **Minutes 7-10: Broad Significance 설명 (Pair B 사용)**

**[강의자 행동]**:
- Slide 20 투사 (Pair B broad significance)
- Cross-disciplinary impact 강조

**[Script]**:
> "이 논문은 '우리가 AI 설득을 연구했다'가 아니라
> 'platform governance와 design에 영향을 미친다'고 말합니다.
> 이것이 독자층을 AI 연구자에서 정책 입안자, 윤리학자, 플랫폼 디자이너까지 확장시킵니다."

**[Slide]**: Slide 20 (NEW - Pair B broad significance)

---

#### **Minutes 10-12: 정량적 결과 표현 (Pair B 사용)**

**[강의자 행동]**:
- Slide 18-19 투사 (Pair B quantitative results)
- 5가지 정량 지표 강조

**[Script]**:
> "Nature는 '유의미했다'가 아니라 '얼마나 강했는가'를 요구합니다.
> 이 논문: 64.4% of the time, 81.2% relative increase, 95% CI, P<0.01, N=900
> 5가지 정량 지표를 한 문장에 집약했습니다."

**[Slide]**: Slide 18-19 (NEW - Pair B quantitative)

---

#### **Minutes 12-15: 4가지 Opening 패턴 요약**

**[강의자 행동]**:
- Slides 21-26 빠르게 진행 (Problem/Gap/Opportunity/Challenge)
- 각 패턴 1개 예시씩만

**[Script]**:
> "4가지 패턴을 빠르게 정리하고, 이제 실제 Nature 초록을 직접 분석해봅시다."

**[Transition to Workshop]**:
> "강의는 여기까지. 이제 70분 워크샵 시작합니다.
> 첫 20분은 Nature 초록 2개를 분석하며 평가 기준을 도출하겠습니다."

---

## PART III: WORKSHOP MATERIALS (15-85분)

### 3.1 Exemplar Calibration (15-35분)

#### **Minutes 15-17: Pair A 초록 제시 및 Silent Reading**

**[강의자 행동]**:
1. 화면에 Pair A 초록 투사
2. 학생들에게 3분 개별 분석 시간 부여
3. 타이머 시작

**[투사 자료]**:

---
**📗 Pair A: Memory & Temporal Context (Gap-driven)**

**Journal**: Nature Communications, Volume 14(1):4350 (July 2023)
**Authors**: Zou, F., Wanjia, G., Allen, E.J., et al.
**DOI**: 10.1038/s41467-023-40100-8
**Citations**: 45+ (as of 2024)

**Abstract**:
> Converging, cross-species evidence indicates that memory for time is supported by hippocampal area CA1 and entorhinal cortex. **However, limited evidence characterizes how these regions preserve temporal memories over long timescales (e.g., months).** At long timescales, memoranda may be encountered in multiple temporal contexts, potentially creating interference. Here, using 7T fMRI, we measured CA1 and entorhinal activity patterns as human participants viewed thousands of natural scene images distributed, and repeated, across many months. We show that memory for an image's original temporal context was predicted by the degree to which CA1/entorhinal activity patterns from the first encounter with an image were re-expressed during re-encounters occurring minutes to months later. Critically, temporal memory signals were dissociable from predictors of recognition confidence, which were carried by distinct medial temporal lobe expressions. These findings suggest that CA1 and entorhinal cortex preserve temporal memories across long timescales by coding for and reinstating temporal context information.

---

**[Script]**:
> "이 Nature Communications 초록을 읽으면서:
> 1. Opening sentence - 어떤 패턴? (Problem/Gap/Opportunity/Challenge)
> 2. Broad significance - 누구에게 중요한가?
> 3. Quantitative results - 구체적 숫자가 있는가?
> 3분 드리겠습니다. 표시하면서 읽으세요."

**[Teaching Tip]**:
- 조용히 순회하며 학생들이 표시하는지 확인
- 너무 빨리 읽는 학생: "천천히, 각 문장 의미 파악하며"
- 표시 안 하는 학생: "Opening sentence부터 동그라미 치세요"

---

#### **Minutes 17-25: Whole-Class Discussion - Pattern Discovery**

**[강의자 행동]**:
Socratic method로 학생들이 패턴 발견하도록 유도

**[Socratic Questions]**:

**Q1 (17:00-19:00): Opening Pattern 분석**
> Q: "첫 문장을 보세요. 어떻게 시작하나요?"
> (학생 답변 기다림) → "Converging evidence indicates..."
>
> Q: "그 다음은?"
> (학생 답변 기다림) → "**However, limited evidence**..."
>
> **확인**: "맞습니다! 이것이 **Gap-driven opening**입니다.
> 기존 연구는 있지만 (cross-species evidence),
> '장기 기억 (months)'에 대한 증거가 부족하다는 gap을 명시했습니다."

**Q2 (19:00-21:00): Broad Significance 분석**
> Q: "'Long timescales (months)'가 왜 중요한가요?"
> (학생 답변 기다림) → "실험실은 수 분~수 일, 실생활은 수개월~수 년"
>
> Q: "Temporal context memory가 왜 중요한가요?"
> (학생 답변 유도) → "Alzheimer's 환자들이 '언제' 기억했는지 혼란"
>
> **확인**: "이 논문은 기초과학 (hippocampus)을 실생활 (months) 및
> 임상 응용 (Alzheimer's)으로 확장시켰습니다."

**Q3 (21:00-23:00): Quantitative Results 분석**
> Q: "구체적인 숫자나 측정값이 있나요?"
> (학생 답변) → "7T fMRI, thousands of images, minutes to months"
>
> **확인**: "정확한 측정 도구와 시간 범위를 명시했습니다."

**[화이트보드 작성]**: 학생 답변을 받으며 기록
```
Nature/Science 초록의 3가지 특징 (Pair A에서 발견):
1. Opening: Gap-driven ("However, limited evidence...")
2. Broad Significance: Long timescales (months) → 실생활, Alzheimer's
3. Quantitative: 7T fMRI, thousands, minutes to months
```

---

#### **Minutes 23-25: Pair C Opening 소개 (Opportunity-driven)**

**[강의자 행동]**:
- 화면에 Pair C opening만 투사 (시간 절약)
- Opportunity-driven 패턴 간략 소개

**[투사 자료]**:

---
**🟢 Pair C: Sleep & Memory Consolidation (Opportunity-driven)**

**Journal**: Nature Neuroscience, Volume 26(6):1100-1110 (June 2023)
**DOI**: 10.1038/s41593-023-01324-5

**Opening (발췌)**:
> Memory consolidation during sleep is thought to depend on the coordinated interplay between cortical slow waves, thalamocortical sleep spindles and hippocampal ripples, **but direct evidence is lacking**. **Here, we implemented real-time closed-loop deep brain stimulation** in human prefrontal cortex during sleep and tested its effects...

---

**[Script]**:
> "또 다른 패턴을 봅시다. 이 Nature Neuroscience 초록은 어떤 패턴인가요?"
> (학생 답변 유도) → "Here, we implemented... → **Opportunity-driven!**"
>
> "Gap은 있었지만 (direct evidence lacking), 이 논문은
> '새로운 기술 (closed-loop stimulation)'으로 해결했다는 **기회**를 강조합니다."

**[화이트보드 추가]**:
```
Opening 패턴:
- Pair A: Gap-driven (However, limited evidence...)
- Pair B: Problem-driven (crucial for assessing misuse) - 강의에서 봄
- Pair C: Opportunity-driven (Here, we implemented...)
- (Challenge-driven은 시간 관계상 생략, 슬라이드 참고)
```

---

#### **Minutes 25-35: Checklist Derivation & Rubric Introduction**

**[강의자 행동]**:
1. 화이트보드에 "Nature/Science Checklist" 공동 작성 (25-28분)
2. 5-Dimension Rubric 배포 및 설명 (28-30분)
3. Editor Protocol 시연 (30-35분)

**[Minutes 25-28: Checklist 도출]**

**[Script]**:
> "우리가 발견한 것을 정리해봅시다. Nature/Science 초록의 핵심 요소는?"
> (학생들과 함께 도출)

**[화이트보드 최종]**:
```
✅ Nature/Science 초록 Checklist (5가지):
1. Opening Pattern: Problem/Gap/Opportunity/Challenge 중 하나 명확?
2. Broad Significance: 좁은 전공 넘어 누구에게 중요한가?
3. Quantitative Results: 구체적 숫자, %, effect size 있는가?
4. Explicit Novelty: "First", "novel", "unprecedented" 명시?
5. Logical Structure: 문제 → 방법 → 결과 → 의미 논리적 흐름?
```

**[Minutes 28-30: 5-Dimension Rubric 배포]**

**[강의자 행동]**:
- Notion page 링크 공유 또는 인쇄본 배포
- 각 dimension 1-5 점수 설명

**[5-DIMENSION RUBRIC - EMBEDDED]**

---

### **📊 Nature/Science 초록 평가 Rubric (5 Dimensions)**

각 항목을 1-5점으로 평가합니다:
- **5 = Exceptional**: Nature/Science 출판 준비 완료
- **4 = Strong**: 탑티어 저널 수준에 근접
- **3 = Adequate**: 일반 저널 수준, 탑티어에는 부족
- **2 = Needs Improvement**: 상당한 개선 필요
- **1 = Major Revision**: Desk reject 수준, 근본적 재작성 필요

---

#### **Dimension 1: Opening Pattern (4가지 패턴 중 하나 명확히 사용)**

| Score | Descriptor | Example |
|-------|------------|---------|
| **5** | 4가지 패턴 중 하나를 완벽하게 사용; "왜 중요한가" 즉시 이해 | "Despite decades of research, 60% of depression patients fail to achieve remission—limiting personalized treatment." (Problem-driven) |
| **4** | 패턴 사용 명확; 중요성이 드러나지만 더 강력할 수 있음 | "Depression treatment failure rates remain high, requiring new approaches." |
| **3** | 패턴 부분적; 중요성 불명확; 재독 필요 | "Depression is a significant public health concern with various treatment options available." |
| **2** | 방법론 또는 배경 리뷰로 시작; "왜 중요한가" 생략 | "Previous studies have investigated depression using various methodologies..." |
| **1** | 패턴 없음; 일반적 진술 | "Depression affects many people worldwide." |

**Korean Translation**:
- **5 = 탁월**: 4가지 패턴 중 하나를 완벽하게 사용; 독자가 즉시 "왜 중요한가"를 이해
- **4 = 강함**: 패턴 사용 명확하지만 더 compelling할 수 있음
- **3 = 적절**: 패턴 부분적, 중요성 불명확
- **2 = 개선 필요**: Opening이 문제/gap/opportunity를 제시하지 않음
- **1 = 대대적 수정**: 일반적 배경 설명만, 패턴 없음

---

#### **Dimension 2: Broad Significance (좁은 전공을 넘어선 영향)**

| Score | Descriptor | Example |
|-------|------------|---------|
| **5** | Cross-disciplinary + societal impact 명확; Nature 넓은 독자층 대상 | "Understanding memory stabilization is fundamental to treating neurodegenerative diseases and enhancing learning—this study reveals a previously unknown mechanism." |
| **4** | Significance 제시되지만 더 넓은 연결 가능 | "This mechanism may have implications for Alzheimer's disease." |
| **3** | 학문적 기여만 강조; 좁은 전문가 대상 | "This advances our understanding of hippocampal function in rodents." |
| **2** | Significance 문장 있지만 generic; 구체성 부족 | "These findings contribute to the literature on memory processes." |
| **1** | Significance 언급 없음; "우리가 연구했다"로만 끝남 | "We investigated memory consolidation in mice." |

**Korean Translation**:
- **5 = 탁월**: 여러 분야 + 사회적 영향 명확 (치료, 정책, 교육 등)
- **4 = 강함**: Significance 있지만 더 넓은 연결 가능
- **3 = 적절**: 학문적 기여만, 좁은 전문가만 관심
- **2 = 개선 필요**: Generic significance ("기여한다")
- **1 = 대대적 수정**: Significance 언급 없음

---

#### **Dimension 3: Quantitative Results (구체적 숫자 vs 모호한 표현)**

| Score | Descriptor | Example |
|-------|------------|---------|
| **5** | Specific %, fold change, effect size + baseline 비교 | "Performance improved 340%, exceeding predictions twofold (Cohen's d=1.8, 95% CI: 3.1-5.3)." |
| **4** | 정량 지표 있지만 일부 누락 (effect size 또는 CI 없음) | "64.4% of the time, 81.2% relative increase, P<0.01, N=900." |
| **3** | 일부 숫자 있지만 주로 모호 | "Significant improvement (p<0.05) with N=89 participants." |
| **2** | 대부분 vague; 숫자 1-2개만 | "Significant effects were observed (p<0.05)." |
| **1** | 완전히 모호; 숫자 없음 | "The method shows promising results." |

**Korean Translation**:
- **5 = 탁월**: %, fold, effect size, CI 모두 제시
- **4 = 강함**: 정량 지표 여러 개 있지만 일부 누락
- **3 = 적절**: 일부 숫자 있지만 "significant" 같은 모호한 표현 혼재
- **2 = 개선 필요**: 대부분 모호, p-value만
- **1 = 대대적 수정**: 숫자 없음

---

#### **Dimension 4: Explicit Novelty ("무엇이 새로운가" 명시)**

| Score | Descriptor | Example |
|-------|------------|---------|
| **5** | "First", "unprecedented", "novel mechanism" 명시적 진술 | "This is the first demonstration that X causes Y..." |
| **4** | Novelty 강하게 implied되지만 명시적 아님 | "This previously unknown mechanism reveals..." |
| **3** | Novelty 약하게 suggested | "Our results extend previous findings by..." |
| **2** | Novelty 불명확; "기여한다" 수준 | "This contributes to understanding of X." |
| **1** | Novelty 언급 없음 | "We investigated X and found Y." |

**Korean Translation**:
- **5 = 탁월**: "First", "Unprecedented", "Novel" 명시적 사용
- **4 = 강함**: Novelty 강하게 implied
- **3 = 적절**: Novelty 약하게 suggested ("extend")
- **2 = 개선 필요**: Generic contribution 진술
- **1 = 대대적 수정**: Novelty 언급 없음

---

#### **Dimension 5: Logical Structure (논리적 흐름)**

| Score | Descriptor | Criteria |
|-------|------------|----------|
| **5** | Perfect IMRaD flow; 각 문장이 다음으로 자연스럽게 연결 | Clear: Background → Problem → Method → Results → Significance |
| **4** | 구조 명확하지만 minor transitions 부족 | Mostly clear, 1-2 jumps 있음 |
| **3** | Basic structure 있지만 order 문제 또는 sections unbalanced | Results before methods, 또는 background too long |
| **2** | 구조 혼란; 재배열 필요 | Hard to follow, elements out of order |
| **1** | 구조 없음; 논리적 흐름 부재 | Random information, no clear progression |

**Korean Translation**:
- **5 = 탁월**: 완벽한 논리적 흐름 (배경→문제→방법→결과→의의)
- **4 = 강함**: 구조 명확, minor transition 문제만
- **3 = 적절**: Basic 구조 있지만 순서 또는 비중 문제
- **2 = 개선 필요**: 구조 혼란, 재배열 필요
- **1 = 대대적 수정**: 논리적 흐름 없음

---

**[Script]**:
> "이 rubric으로 여러분의 초록을 평가할 것입니다.
> 5점 = Nature 출판 준비 완료, 1-2점 = Desk reject.
> 냉정하게 평가하세요. 저도 제 초록이 처음엔 3점 받았습니다."

---

**[Minutes 30-35: Editor Protocol 시연]**

**[강의자 행동]**:
- 가상의 나쁜 초록 예시 투사
- Editor Protocol 4-part 시연

**[EDITOR PROTOCOL TEMPLATE - EMBEDDED]**

---

### **📝 Top-Tier Journal Editor Protocol**

4가지 파트로 구성된 구조화된 피드백:

---

#### **Part 1: Editorial Decision (Simulated)**

**Desk Reject or Send to Review?**
- [ ] **Send to Review** (Score ≥3 on all dimensions OR score 5 on multiple dimensions)
- [ ] **Desk Reject** (Score 1 on any dimension OR scores ≤2 on 3+ dimensions)

**1-Sentence Justification**:
_State the single factor that most influenced your decision._

**Example (Desk Reject)**:
> Desk reject due to narrow significance that appeals only to rodent spatial memory specialists, not Nature's cross-disciplinary readership.

**Example (Send to Review)**:
> Send to review - strong opening (Problem-driven, 5/5) and broad significance (cross-disciplinary impact, 4/5) outweigh minor weaknesses in quantitative results presentation (3/5).

---

#### **Part 2: Strongest Element**

**Which dimension (of 5) is closest to publication-ready?**

Write the dimension number (1-5) and explain why in 1-2 sentences.

**Example**:
> **Dimension 1 (Opening Pattern): 5/5**
> The Problem-driven opening immediately establishes why this matters ("60% of patients fail to achieve remission"), creating urgency and broad relevance from the first sentence.

---

#### **Part 3: Fatal Flaw**

**Which dimension (of 5) would cause rejection if not fixed?**

Write the dimension number (1-5) and explain the critical problem in 1-2 sentences.

**Example**:
> **Dimension 2 (Broad Significance): 1/5**
> The abstract only discusses rodent hippocampal mechanisms with no connection to human diseases, clinical applications, or theoretical frameworks—limiting appeal to narrow neuroscience subspecialty.

---

#### **Part 4: One Concrete Revision**

**Provide a specific sentence-level rewrite, NOT vague advice.**

**❌ BAD FEEDBACK (Too Vague)**:
> "Improve the significance statement to make it more impactful and accessible to general readers."

**✅ GOOD FEEDBACK (Concrete Revision)**:

**Current Sentence**:
> "This study advances our understanding of hippocampal function in rodents."

**Suggested Revision**:
> "Understanding how memories are stabilized is fundamental to treating Alzheimer's disease and age-related cognitive decline—this study reveals a previously unknown mechanism in the hippocampus that could be targeted therapeutically, with implications for 50 million dementia patients worldwide."

**Why Better**:
- Connects to clinical problem (Alzheimer's, dementia)
- Specifies therapeutic potential
- Quantifies impact (50 million patients)
- Cross-disciplinary appeal (neuroscience + medicine)

---

**Korean Translation** (Part 4 example):

**현재 문장**:
> "이 연구는 설치류의 해마 기능에 대한 이해를 증진시킨다."

**제안 수정**:
> "기억이 어떻게 안정화되는지 이해하는 것은 알츠하이머병과 노화 관련 인지 저하를 치료하는 데 필수적이다—본 연구는 해마에서 이전에 알려지지 않은 메커니즘을 밝혀내어 치료 표적이 될 수 있으며, 전 세계 5천만 치매 환자에게 영향을 미칠 수 있다."

---

**[가상 나쁜 초록 시연]**:

**[투사]**:
```
Example Abstract (Bad):

Stress is a significant problem affecting many college students.
Previous research has investigated the relationship between stress
and cognitive performance using various methodologies. We conducted
a study with 89 college students to examine stress effects on
cognitive flexibility. Participants completed the Wisconsin Card
Sorting Test (WCST) and reported stress levels. Our results showed
significant effects of stress on WCST performance (p<0.05).
Regression analysis revealed associations between stress and
cognitive flexibility measures. These findings contribute to the
literature on stress and cognition, with implications for
understanding mental health in college populations.
```

**[Script - Editor Protocol 시연]**:
> "이 초록을 Editor Protocol로 평가해봅시다."
>
> **Part 1: Desk Reject?** → YES
> **Justification**: Narrow significance (only college mental health researchers would care)
>
> **Part 2: Strongest Element?** → Dimension 5 (Structure): 3/5
> Basic IMRaD flow is clear, nothing else is strong.
>
> **Part 3: Fatal Flaw?** → Dimension 2 (Broad Significance): 1/5
> Only appeals to college mental health researchers, no broader impact.
>
> **Part 4: Concrete Revision**:
>
> **Current**: "These findings contribute to the literature on stress and cognition,
> with implications for understanding mental health in college populations."
>
> **Revision**: "Stress affects 60% of college students yet we lack understanding
> of which cognitive processes are most vulnerable—critical for designing effective
> interventions. This study reveals that chronic stress selectively impairs
> cognitive flexibility (34% reduction, Cohen's d=1.2), not working memory—
> challenging the 'global deficit' model and suggesting targeted cognitive training
> can reduce stress-related dropout affecting 30% of undergraduates annually."

**[Transition to Peer Review]**:
> "이제 여러분의 초록을 이 방식으로 평가할 차례입니다. 조별로 모여서
> Editor Protocol을 사용하여 서로의 초록을 평가해주세요."

---

### 3.2 Peer Review Round 1 (35-60분)

#### **Minutes 35-37: Small Group Setup**

**[강의자 행동]**:
1. 조 배정 공지 (Notion에 미리 작성해둔 것)
2. 각 조 Notion 워크스페이스 확인
3. 타이머 및 procedure 설명

**[Small Group Assignments]** (사전 준비):
- 3-4명/조
- 연구 주제 다양성 고려
- 영어 실력 균형 (한 조에 고수만 또는 초보만 몰리지 않도록)

**[Script]**:
> "조 배정은 Notion에 올렸습니다. 각자 조로 이동하고
> Notion '내 초록 워크스페이스'를 여세요.
>
> Procedure: 각 author 7분
> - Author가 초록 읽기: 2분
> - Reviewers가 Editor Protocol 작성: 4분
> - 간단 토론: 1분
>
> 저는 순회하며 도와드리겠습니다. 시작!"

**[Teaching Tip]**:
- Timer를 7분마다 울리도록 설정
- "Next author's turn!" 알림

---

#### **Minutes 37-60: Circulating & Monitoring**

**[강의자 행동]**:
각 조를 순회하며 모니터링

**[Monitor For - 체크리스트]**:
- [ ] Vague feedback ("improve clarity") → "어떤 문장을 어떻게 고칠 건가요?"
- [ ] Overly harsh tone → "건설적으로: 문제 + 해결책"
- [ ] Off-task discussion → "Protocol에 집중하세요"
- [ ] Author defensiveness → "이것은 Nature 편집자 시뮬레이션. 탑티어는 엄격합니다."
- [ ] Reviewers struggling → "Fatal flaw이 뭔가요? 어떤 dimension이 가장 약한가요?"

**[Interventions - When to Step In]**:

**Scenario 1: Vague Feedback**
> 학생: "Significance를 더 broad하게 만드세요."
>
> **Intervention**: "좋은 지적입니다. 구체적으로 어떤 문장을 어떻게 고치면 될까요?
> Part 4에 exact rewrite를 써주세요."

**Scenario 2: Overly Harsh**
> 학생: "이건 완전 엉망이에요. 처음부터 다시 써야 해요."
>
> **Intervention**: "Desk reject일 수 있지만, 가장 큰 문제 1개를 집중적으로
> 고치면 개선될 수 있습니다. Fatal flaw이 뭔가요?"

**Scenario 3: Author Defensive**
> Author: "하지만 제 연구는 정말 중요한데..."
>
> **Intervention**: "여러분의 연구는 모두 중요합니다. 하지만 Nature 편집자는
> 1년에 1만 편을 받고 850편만 출판합니다. 초록에서 importance를 명확히
> 전달해야 합니다. 피드백을 활용해서 개선합시다."

**Scenario 4: Time Management**
> 한 author에게 10분 이상 소요
>
> **Intervention**: "시간 관계상 다음 author로 넘어가야 합니다.
> Reviewer들은 Notion에 마저 작성하고, 다음 author 시작하세요."

**[Time Calls]**:
- 42분: "조 1, 2번째 author로!"
- 49분: "조 3, 3번째 author로!"
- 56분: "조 4, 마지막 author로!"
- 60분: "Peer Review Round 1 종료! 이제 AI로 개선해봅시다."

---

### 3.3 AI-Enhanced Revision (60-75분)

#### **Minutes 60-62: AI Revision 소개 및 Prompt Templates 제공**

**[강의자 행동]**:
1. Notion에 5개 AI Prompt Templates 링크 공유
2. 효과적인 prompting 원칙 설명

**[Script]**:
> "이제 받은 피드백을 바탕으로 AI로 초록을 개선해봅시다.
> 중요: AI에게 막연히 '초록 개선해줘'가 아니라,
> '이 구체적인 피드백을 반영해서 이 부분을 고쳐줘'라고 해야 합니다.
>
> Notion에 5가지 prompt template이 있습니다. 상황에 맞게 선택하세요."

**[5 AI PROMPT TEMPLATES - EMBEDDED]**

---

### **🤖 AI Revision Prompt Templates**

각 상황별로 적합한 template 선택:

---

#### **Template 1: Addressing Fatal Flaw - Broad Significance**

**상황**: Dimension 2 (Broad Significance) 점수가 1-2점, "너무 narrow"라는 피드백

```
I received peer feedback that my abstract has narrow significance
that appeals only to [subspecialty] researchers.

My current significance statement is: "[paste current sentence]"

The problem: [paste reviewer's fatal flaw description]

Task: Rewrite this significance statement to:
1. Connect my [subspecialty] finding to cross-disciplinary concerns
   (clinical/policy/computational/educational)
2. Specify the broader impact (e.g., disease prevalence, societal cost,
   theoretical implications)
3. Maintain scientific accuracy - do not fabricate claims not supported
   by my research

My research context: [1-2 sentences describing actual findings]

Output: Provide 3 alternative rewritten sentences, each taking a
different angle (clinical, computational, societal).
```

**Korean Version**:
```
동료 피드백에서 제 초록의 significance가 [세부 전공] 연구자들에게만
호소력이 있다는 지적을 받았습니다.

현재 significance 문장: "[현재 문장 붙여넣기]"

문제점: [리뷰어의 fatal flaw 설명 붙여넣기]

과제: 이 significance 문장을 다음과 같이 재작성해주세요:
1. 내 [세부 전공] 발견을 cross-disciplinary 관심사(임상/정책/계산/교육)와 연결
2. 더 넓은 영향 구체화 (질병 유병률, 사회적 비용, 이론적 함의 등)
3. 과학적 정확성 유지 - 내 연구가 뒷받침하지 않는 주장 날조 금지

내 연구 맥락: [실제 발견 1-2문장 설명]

출력: 3가지 대안 문장 제공, 각각 다른 각도(임상, 계산, 사회적)에서 접근
```

---

#### **Template 2: Adding Quantitative Results**

**상황**: Dimension 3 (Quantitative Results) 점수가 1-3점, "too vague" 피드백

```
I received feedback that my results presentation is too vague and lacks
specific numbers.

My current results section: "[paste current results sentences]"

My actual data:
- Sample size: N = [number]
- Key finding: [e.g., "Group A performed better than Group B"]
- Statistical test: [e.g., "t-test, p<0.05"]
- Effect size: [if available, e.g., "Cohen's d=1.2"]
- Percentage/fold change: [if available]

Task: Rewrite my results section to:
1. Include specific numbers (%, fold change, effect size)
2. Compare to baseline or control
3. Provide confidence intervals if available
4. Maintain conciseness (2-3 sentences maximum)

Output: 2 versions - one moderate specificity, one high specificity
(like Nature style).
```

**Korean Version**:
```
결과 제시가 너무 모호하고 구체적 숫자가 부족하다는 피드백을 받았습니다.

현재 결과 섹션: "[현재 결과 문장 붙여넣기]"

실제 데이터:
- 표본 크기: N = [숫자]
- 핵심 발견: [예: "A 그룹이 B 그룹보다 나았다"]
- 통계 검정: [예: "t-test, p<0.05"]
- Effect size: [있으면, 예: "Cohen's d=1.2"]
- 백분율/배수 변화: [있으면]

과제: 결과 섹션을 다음과 같이 재작성:
1. 구체적 숫자 포함 (%, 배수 변화, effect size)
2. Baseline 또는 control과 비교
3. 신뢰구간 제공 (가능하면)
4. 간결함 유지 (최대 2-3문장)

출력: 2가지 버전 - 중간 구체성, 높은 구체성 (Nature 스타일)
```

---

#### **Template 3: Strengthening Opening Pattern**

**상황**: Dimension 1 (Opening Pattern) 점수가 1-3점, "unclear pattern" 피드백

```
I received feedback that my opening doesn't follow a clear pattern
(Problem/Gap/Opportunity/Challenge-driven).

My current opening: "[paste first 2-3 sentences]"

My research addresses: [e.g., "Memory consolidation in Alzheimer's disease"]

Task: Rewrite my opening using EACH of the 4 patterns:

1. **Problem-driven**: Start with "Despite extensive research, [problem]
   remains unsolved..."
2. **Gap-driven**: Start with "While [known fact], we lack understanding
   of [gap]..."
3. **Opportunity-driven**: Start with "Recent advances in [technology/method]
   enable unprecedented investigation of..."
4. **Challenge-driven**: Start with "[phenomenon] poses a fundamental
   challenge to our understanding of..."

Requirements:
- Make the "why this matters" clear in the first sentence
- Connect to broader scientific/societal concerns
- Maximum 2 sentences per version

Output: All 4 versions so I can compare and choose.
```

**Korean Version**:
```
Opening이 명확한 패턴을 따르지 않는다는 피드백을 받았습니다.

현재 opening: "[처음 2-3문장 붙여넣기]"

내 연구가 다루는 것: [예: "알츠하이머병에서의 기억 공고화"]

과제: 4가지 패턴을 각각 사용하여 opening 재작성:

1. **Problem-driven**: "광범위한 연구에도 불구하고 [문제]는 여전히
   미해결이다..." 로 시작
2. **Gap-driven**: "[알려진 사실]이 확립되었지만, 우리는 [빈틈]에 대한
   이해가 부족하다..." 로 시작
3. **Opportunity-driven**: "[기술/방법]의 최근 발전이 [주제]에 대한
   전례 없는 조사를 가능하게 한다..." 로 시작
4. **Challenge-driven**: "[현상]은 [주제]에 대한 우리의 이해에 근본적
   도전을 제기한다..." 로 시작

요구사항:
- "왜 중요한가"를 첫 문장에서 명확히
- 더 넓은 과학적/사회적 관심사와 연결
- 각 버전 최대 2문장

출력: 비교하고 선택할 수 있도록 4가지 버전 모두 제공
```

---

#### **Template 4: AI Self-Critique (Before Submitting to Peers)**

**상황**: 자신의 초록이 desk-reject될지 스스로 점검하고 싶을 때

```
You are a Nature journal editor. Evaluate this abstract using the
5 common rejection reasons:

[Paste your abstract]

Evaluate on these 5 dimensions (1-10 scale, 1=severe weakness, 10=excellent):

1. **Unclear novelty**: Is what's new explicitly stated? Score and explain.
2. **Narrow scope**: Would only subspecialists care? Score and explain.
3. **Weak evidence**: Do claims exceed evidence? Score and explain.
4. **Poor structure**: Is logical flow broken? Score and explain.
5. **Overselling**: Are there exaggerated claims? Score and explain.

For each dimension:
- Score (1-10)
- Specific problem (quote the problematic sentence)
- Concrete improvement suggestion

Finally: Would you desk-reject this? Yes/No and why in 1 sentence.
```

**Korean Version**:
```
당신은 Nature 저널 편집자입니다. 다음 초록을 5가지 흔한 거부 사유로 평가하세요:

[초록 붙여넣기]

5가지 항목 평가 (1-10 척도, 1=심각한 약점, 10=탁월):

1. **Novelty 불명확**: 무엇이 새로운지 명시되었는가? 점수 및 설명.
2. **Scope 좁음**: 세부 전문가만 관심 가질 내용인가? 점수 및 설명.
3. **증거 약함**: 주장이 증거를 초과하는가? 점수 및 설명.
4. **구조 부실**: 논리적 흐름이 끊겼는가? 점수 및 설명.
5. **과장**: 과장된 표현이 있는가? 점수 및 설명.

각 항목마다:
- 점수 (1-10)
- 구체적 문제 (문제가 되는 문장 인용)
- 구체적 개선 제안

마지막: 이 초록을 desk-reject하겠는가? Yes/No 및 이유 1문장.
```

---

#### **Template 5: Combining Peer Feedback with AI**

**상황**: 여러 peer reviewer의 피드백을 종합하여 한 번에 반영하고 싶을 때

```
I received feedback from 3 peer reviewers on my abstract. Help me
synthesize and address their comments.

**My original abstract**:
[Paste abstract]

**Reviewer 1 feedback**:
- Fatal flaw: [paste]
- Suggested revision: [paste]

**Reviewer 2 feedback**:
- Fatal flaw: [paste]
- Suggested revision: [paste]

**Reviewer 3 feedback** (if applicable):
- Fatal flaw: [paste]
- Suggested revision: [paste]

Task:
1. Identify the most common criticism (what dimension had lowest scores?)
2. Rewrite my abstract addressing the TOP 2 most critical issues
3. Maintain my original research accuracy - don't fabricate data
4. Keep to 250-300 words

Output:
- Revised abstract
- Change log (what specifically was changed and why)
```

**Korean Version**:
```
3명의 peer reviewer로부터 초록 피드백을 받았습니다. 코멘트를 종합하고
반영하는 것을 도와주세요.

**원본 초록**:
[초록 붙여넣기]

**Reviewer 1 피드백**:
- Fatal flaw: [붙여넣기]
- 제안 수정: [붙여넣기]

**Reviewer 2 피드백**:
- Fatal flaw: [붙여넣기]
- 제안 수정: [붙여넣기]

**Reviewer 3 피드백** (해당시):
- Fatal flaw: [붙여넣기]
- 제안 수정: [붙여넣기]

과제:
1. 가장 공통된 비판 파악 (어떤 dimension 점수가 가장 낮았나?)
2. 가장 중요한 2가지 이슈를 반영하여 초록 재작성
3. 원래 연구 정확성 유지 - 데이터 날조 금지
4. 250-300 단어 유지

출력:
- 수정된 초록
- 변경 로그 (구체적으로 무엇을 왜 바꿨는지)
```

---

**[Teaching Tip - AI Usage Guidelines]**:
> "AI는 빠르게 다양한 버전을 생성하는 도구입니다.
> 하지만 최종 판단은 여러분이 해야 합니다.
>
> **AI가 도움 되는 것**:
> - 다양한 phrasing 옵션
> - Significance 확장 아이디어
> - 정량적 결과 presentation
>
> **AI가 못 하는 것**:
> - 데이터 날조
> - 연구의 핵심 메시지 파악
> - 과학적 정확성 검증
>
> AI 출력을 받으면:
> 1. 과학적으로 정확한가?
> 2. Peer 피드백을 실제로 반영했는가?
> 3. 내 연구의 핵심이 여전히 명확한가?
>
> 이 3가지를 확인하고 accept/reject 하세요."

---

#### **Minutes 62-75: Individual AI Revision Work**

**[강의자 행동]**:
- 조용히 순회하며 학생 모니터링
- 질문에 답변
- 좋은 AI 출력 발견 시 나중에 공유하겠다고 표시

**[Monitor For]**:
- [ ] AI 출력을 무비판적으로 수용 → "이게 정말 피드백을 반영했나요?"
- [ ] 너무 많은 버전 생성 → "Best 2개만 선택해서 비교하세요"
- [ ] Prompt 작성 어려워하는 학생 → "Template 1번부터 시작해보세요"
- [ ] AI가 데이터 날조 → "이 숫자는 여러분 실제 데이터가 아니죠? 삭제하세요"

**[Good Examples to Share Later]**:
- Pair B 스타일 opening으로 변환한 학생
- Broad significance를 clinical impact으로 확장한 학생
- 정량적 결과를 % + CI + effect size로 강화한 학생

**[Intervention Scripts]**:

**Scenario 1: Uncritical AI Acceptance**
> 학생: "AI가 이렇게 고쳐줬는데 어때요?"
>
> **Intervention**: "좋네요. 그런데 peer feedback에서 지적한 fatal flaw이
> 뭐였죠? 이 AI 출력이 그것을 실제로 고쳤나요? 비교해봅시다."

**Scenario 2: Too Many Versions**
> 학생: "AI에게 5번 물어봤는데 다 달라서 뭘 선택할지 모르겠어요."
>
> **Intervention**: "좋은 시도입니다. 이제 Best 2개를 골라서 rubric으로
> 채점해보세요. 어느 게 5-dimension에서 점수가 높은가요?"

**Scenario 3: Struggling with Prompting**
> 학생: "AI가 제대로 이해를 못 해요."
>
> **Intervention**: "Template을 사용했나요? Template 1번 - Broad Significance -
> 여기에 여러분의 구체적 문장과 피드백을 붙여넣으면 더 정확한 출력이 나옵니다."

---

### 3.4 Validation Round 2 (75-85분)

#### **Minutes 75-77: Round 2 Setup**

**[강의자 행동]**:
1. 각 조로 돌아가라고 지시
2. Round 2 procedure 설명

**[Script]**:
> "AI로 개선한 버전을 조원들에게 보여줄 시간입니다.
> Round 1보다 짧습니다 - 각 author 2분:
> - Revised abstract 읽기: 1분
> - Peers가 Quick Feedback: 1분
>
> Quick Feedback 질문:
> 1. Fatal flaw이 해결되었나? (Yes/No)
> 2. 가장 개선된 dimension은? (1-5 중)
> 3. 여전히 약한 부분은? (간단히)
>
> 시작!"

---

#### **Minutes 77-85: Quick Validation**

**[강의자 행동]**:
- 타이머 2분마다 울림
- 순회하며 모니터링
- 눈에 띄게 개선된 초록 표시 (85분에 공유 예정)

**[Monitor For]**:
- [ ] 실제로 개선되었는지 확인
- [ ] Peers가 긍정적 feedback만 하는지 (여전히 문제 있으면 지적해야)
- [ ] Time management (2분 엄수)

**[Interventions]**:

**Scenario: Unconstructive Positivity**
> 학생들: "완벽해요! 다 좋아졌어요!"
>
> **Intervention**: "좋습니다. 그럼 5-dimension 중 어떤 게 가장 개선되었나요?
> 그리고 여전히 3점 이하인 dimension이 있나요? 냉정하게 평가하세요."

**[Collect Good Examples]**:
- 눈에 띄게 broad significance가 개선된 경우
- Opening pattern이 명확해진 경우
- Quantitative results가 추가된 경우

→ 85분 wrap-up에서 공유 예정

---

## PART IV: WRAP-UP & ASSIGNMENT (85-90분)

### 4.1 Good Examples Sharing (85-88분)

**[강의자 행동]**:
1. 2-3명의 학생 초록 개선 사례 공유 (학생 동의 받고)
2. Before/After 비교
3. 어떤 AI prompt가 효과적이었는지 공유

**[Script]**:
> "몇 분의 개선 사례를 공유하겠습니다. [학생 A], 동의하시나요?
>
> **Before**: '이 연구는 스트레스가 인지에 미치는 영향을 조사했다.'
> **After**: '스트레스는 60% 대학생에게 영향을 미치지만 어떤 인지 과정이
> 가장 취약한지 불명확하다—이 연구는 인지 유연성이 선택적으로 손상된다는
> 것을 밝혀내어 (34% 감소, d=1.2), 표적 개입이 필요함을 시사한다.'
>
> 개선점:
> - Opening: Problem-driven 패턴 추가 (60% prevalence)
> - Broad Significance: 개입 전략과 연결
> - Quantitative: 34%, Cohen's d=1.2 추가
>
> 사용한 AI prompt: Template 1 (Broad Significance) + Template 2 (Quantitative)
>
> 축하합니다! [학생 A]의 초록은 이제 4점대입니다."

**[2-3 examples 반복]**

---

### 4.2 과제 안내 (88-90분)

**[강의자 행동]**:
- Notion 과제 페이지 링크 공유
- 제출 기한 및 형식 안내

**[과제 내용]**:

---

### **📝 Week 2 과제 (다음 주까지 제출)**

**제출처**: Notion "Week 2 과제 제출" 페이지

---

#### **Part A: Nature/Science급 초록 (250-300 words)**

**필수 포함 요소**:
- ✅ 4가지 Opening 패턴 중 하나 명확히 사용 (어떤 패턴인지 표시)
- ✅ Broad significance framing (누구에게 왜 중요한지)
- ✅ 정량적 결과 제시 (%, fold change, effect size, CI 등)
- ✅ Novelty 명시적 강조 ("first", "unprecedented", "novel")
- ✅ 5-dimension rubric 자가 평가표 첨부 (각 dimension 점수 및 이유)

**제출 형식**:
- Final abstract (영어)
- 5-dimension self-assessment table

---

#### **Part B: AI 활용 과정 문서 (500-700 words, 한글 OK)**

**필수 포함 요소**:
1. **사용한 프롬프트 레시피** (최소 3개)
   - 어떤 template 사용했는지
   - Input (peer feedback)
   - AI 출력
   - 왜 이 출력을 선택했는지 또는 거부했는지

2. **AI 출력 평가 과정**
   - 어떤 기준으로 good/bad 판단했는지
   - 과학적 정확성 검증 방법
   - Final version 선택 이유

3. **AI 활용의 장단점 성찰**
   - AI가 도움 된 부분
   - AI가 부족했던 부분
   - 향후 AI 활용 전략

---

#### **Part C: Peer Feedback 반영 문서 (300-400 words, 한글 OK)**

**필수 포함 요소**:
1. **받은 피드백 요약**
   - 3명 reviewer의 주요 피드백
   - 가장 공통된 fatal flaw

2. **피드백 반영 과정**
   - 어떤 피드백을 accept했는지
   - 어떤 피드백을 reject했는지 (이유와 함께)
   - Before/After 비교

3. **동료 학습 인사이트**
   - 다른 학생 초록에서 배운 점
   - 가장 인상적이었던 opening/significance 사례

---

**제출 기한**: 다음 주 월요일 23:59까지

**참고자료**:
- 오늘 분석한 3개 Nature/Science 초록 (Notion 링크)
- 5-dimension rubric
- Editor Protocol
- 5 AI prompt templates

---

**[Script]**:
> "다음 주까지 3가지 제출:
> Part A - 개선된 초록 + 자가평가
> Part B - AI 활용 과정
> Part C - Peer feedback 반영
>
> 오늘 분석한 Pair A, B, C 초록을 참고하세요.
> 질문 있으신 분? 없으면 수고하셨습니다!"

---

## PART V: APPENDICES

### Appendix A: Pre-Class Preparation Checklist

**2주 전**:
- [ ] Notion Week 2 page 생성 및 Template Button 설정
- [ ] 학생 명단 확인 (6-12명)
- [ ] Small group assignments 작성 (3-4명/조, 연구 주제 다양성 고려)

**1주 전**:
- [ ] 학생들에게 초록 제출 요청 이메일 (Notion 링크 포함)
- [ ] lesson_slides_15min.md를 Marp로 PDF 생성 테스트
- [ ] Pair A, B, C 초록 슬라이드 최종 확인

**2일 전**:
- [ ] 학생 초록 제출 확인 (48-hour deadline)
- [ ] 미제출자 독려
- [ ] 5-dimension rubric 인쇄 (조당 1부)
- [ ] Editor Protocol 인쇄 (조당 1부)

**당일 아침**:
- [ ] 프로젝터 연결 확인
- [ ] Notion 접속 테스트
- [ ] 타이머 앱 설정 (7분, 2분 알람)
- [ ] 화이트보드 마커 확인

---

### Appendix B: Small Group Assignment Strategy

**Goal**: 각 조가 다양한 연구 주제와 영어 실력을 가지도록

**Assignment Criteria**:
1. **Research Topic Diversity**: 한 조에 같은 주제 2명 이상 금지
   - Example: 조 1 = 우울증 + AI persuasion + 기억 공고화
   - Avoid: 조 1 = 우울증 + 우울증 + 우울증

2. **English Proficiency Balance**: 고수 1-2명 + 중수 1-2명 / 조
   - 사전 설문 또는 이전 수업 작문으로 파악
   - Avoid: 고수만 모인 조 vs 초보만 모인 조

3. **Personality Balance** (선택적):
   - Outspoken 학생 + Quiet 학생 균형
   - 한 조에 dominant personality 2명 이상 금지

**Pre-Class Survey** (Notion Form):
> 1. 연구 주제를 한 문장으로: _______
> 2. 영어 작문 자신감 (1-5): _______
> 3. 선호하는 peer feedback 스타일: [ ] 직접적 [ ] 완곡한

**Manual Adjustment**:
- 알고리즘 배정 후 instructor가 최종 조정
- 친한 친구끼리 같은 조 피하기 (professional feedback 유도)

---

### Appendix C: Troubleshooting Guide

#### **Problem 1: 학생이 초록을 가져오지 않음**

**Prevention**:
- 2일 전 deadline with reminder email
- "초록 없이 오면 예시 초록으로 연습" 사전 고지

**If It Happens**:
- 해당 학생은 exemplar 초록 (Pair A, B, C) 중 하나를 분석하도록
- Peer review는 참여하되 자신의 초록은 skip
- 과제에서 감점

---

#### **Problem 2: Peer feedback이 너무 vague**

**Examples**:
- "더 명확하게 쓰세요"
- "Significance를 넓히세요"
- "좋아요"

**Instructor Intervention**:
> "Part 4 - Concrete Revision을 보세요. 어떤 문장을 어떻게 고칠 건가요?
> Before/After를 써주세요. Author가 copy-paste할 수 있도록."

---

#### **Problem 3: Peer feedback이 너무 harsh**

**Examples**:
- "이건 완전 엉망이에요"
- "처음부터 다시 쓰세요"
- "이게 대학원생 글이에요?"

**Instructor Intervention**:
> "건설적 피드백의 원칙: 문제 + 해결책.
> '엉망'이 아니라 '이 dimension이 약하고, 이렇게 고치면 좋겠다'로 표현하세요."

---

#### **Problem 4: AI가 데이터를 날조함**

**Example**:
> AI: "Our results showed 78% improvement (95% CI: 65-91%, p<0.001)..."
> (학생의 실제 데이터가 아님)

**Instructor Intervention**:
> "AI가 그럴듯한 숫자를 만들었지만 여러분 실제 데이터가 아니죠?
> 이것은 data fabrication입니다. 절대 사용하면 안 됩니다.
> AI에게 여러분의 실제 숫자를 명시적으로 제공하고 '이 숫자만 사용하라'고 지시하세요."

---

#### **Problem 5: 시간이 부족함 (70분에 다 못 끝냄)**

**Adjustment Options**:

**Option A: Skip Validation Round 2**
- Minutes 60-85를 AI Revision에만 사용 (25분)
- Validation은 Notion에서 비동기로 (과제의 일부)

**Option B: Shorten Exemplar Calibration**
- Minutes 15-25로 단축 (35분 → 25분)
- Pair C 생략, Pair A만 집중 분석
- 10분을 Peer Review Round 1에 추가

**Option C: Extend to 100 minutes**
- 강의 10-15분 단축
- Workshop 80-85분으로 확장

---

#### **Problem 6: 학생이 AI 의존도가 너무 높음**

**Red Flags**:
- AI 출력을 무조건 수용
- 자신의 판단 없이 AI에게 모든 결정 맡김
- "AI가 이렇게 하래요"

**Instructor Intervention**:
> "AI는 도구입니다. 최종 판단은 여러분이 해야 합니다.
> 이 AI 출력을 왜 선택했나요? 5-dimension rubric으로 채점해봤나요?
> 과학적으로 정확한가요? 비판적으로 평가하세요."

**Teaching Moment**:
> "탑티어 저널 편집자가 AI 생성 여부를 판별할 수 있습니다.
> Generic AI phrasing은 오히려 desk-reject 이유가 됩니다.
> 여러분의 research voice가 나와야 합니다."

---

#### **Problem 7: Cultural barriers (한국 학생 특성)**

**Issue 1: 직접적 feedback 회피**
- 한국 문화: 직접 비판 uncomfortable
- 결과: "좋아요", "잘 썼어요" 만 반복

**Solution**:
> "이것은 Nature editor 시뮬레이션입니다. Professional feedback은
> 친구에게 상처 주는 것이 아니라 논문을 개선하는 것입니다.
> Editor Protocol을 따르세요 - 이것이 구조화된 피드백입니다."

**Issue 2: Bold claims 회피**
- 한국 학생: "조심스럽게 제안한다", "작은 기여를 한다"
- Nature: "First", "Unprecedented", "Fundamental"

**Solution**:
> "한국 학술 문화와 Nature 문화는 다릅니다.
> Nature에서는 bold claim + solid evidence가 기대됩니다.
> 이것은 arrogance가 아니라 clarity입니다.
> 이 수업에서는 Nature 스타일로 연습하세요."

---

### Appendix D: Notion Workspace Setup Guide

**Database 1: Student Submissions**
- Properties: Name, 학생, Week, Section, Status, Peer Score, Peer Feedback
- View: Table, Board by Status

**Database 2: AI Recipe Library**
- Properties: Recipe Name, Week, Category, Success Rate, Submitted By
- View: Gallery by Week

**Week 2 Page Structure**:
```
📚 Week 2: Nature/Science급 초록 작성

├─ 📖 강의 자료
│  ├─ 15-min Slides (Marp PDF)
│  ├─ 4가지 Opening Patterns 요약
│  └─ Broad Significance 전략
│
├─ 💡 Exemplar 초록 3개
│  ├─ Pair A: Memory & Temporal Context (Gap-driven)
│  ├─ Pair B: AI Persuasiveness (Problem-driven)
│  └─ Pair C: Sleep & Memory (Opportunity-driven)
│
├─ 📊 평가 도구
│  ├─ 5-Dimension Rubric (bilingual)
│  └─ Editor Protocol Template
│
├─ 🤖 AI Prompt Templates
│  ├─ Template 1: Broad Significance
│  ├─ Template 2: Quantitative Results
│  ├─ Template 3: Opening Pattern
│  ├─ Template 4: Self-Critique
│  └─ Template 5: Combining Feedback
│
├─ 👥 Small Groups (조 배정)
│  ├─ 조 1: [학생 A, B, C]
│  ├─ 조 2: [학생 D, E, F]
│  └─ ...
│
├─ 🧪 Student Workspaces (Template Button)
│  └─ "내 Peer Review 워크스페이스 만들기" 버튼
│
└─ 📝 과제 제출
   └─ Linked Database: Student Submissions (Week = "Week 2")
```

---

**Last Updated**: 2025-01-02
**Document Purpose**: Complete classroom-ready teaching guide for Week 2
**Target Audience**: Instructor teaching 90-minute graduate seminar
**Dependencies**: lesson_slides_15min.md (Marp slides), Notion workspace
```
