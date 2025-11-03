# Week 4: AI 활용 III - Methods/Results Bulletproofing 전략

---

## 🎯 학습 목표

**"리뷰어의 methodological/statistical 공격을 방어할 수 있는 Methods/Results 작성"**

1. 🚨 탑티어 저널의 Methods/Results 거부 사유 Top 10 파악
2. 🛡️ Reproducibility, Control, Statistical Rigor 체크리스트 실행
3. ⚠️ Overclaiming 방지 및 Transparent Reporting 전략
4. 🔍 AI를 활용한 Self-Critique 및 Preemptive Defense
5. 📊 Effect Size + Significance 통합 보고

> Image suggestion: A fortress-like shield protecting a research paper from incoming reviewer arrows labeled "Reproducibility?", "Controls?", "Power?", "Overclaiming?". The shield has checkmarks on sections labeled "Methods" and "Results". Modern, professional illustration with blue/green tones for defense/protection theme.

---

## ⚠️ 전제: CoT는 이미 배웠습니다

**윤경생 박사님 강의에서 학습한 내용:**
- Chain-of-Thought (CoT) 프롬프팅 기법
- 단계별 추론 유도 방법
- AI의 사고 과정 드러내기

**본 강의에서는:**
- ❌ CoT **기법** 설명 (이미 아는 내용)
- ✅ CoT를 **Bulletproofing 목표**에 전략적 활용
- ✅ "어떻게 리뷰어의 공격을 방어하는가?"

> Image suggestion: A two-panel comparison. Left panel: "윤경생 강의 - CoT 기법" showing a tree diagram of step-by-step reasoning. Right panel: "Week 4 - CoT 전략적 활용" showing the same reasoning applied to finding vulnerabilities in a Methods section. Arrow connecting them labeled "Apply to Defense". Clean infographic style.

---

## 📚 수업 전 과제 확인

**필수 과제: Methods & Results 섹션 초안**

✅ **Methods** (800-1000 words):
- Participants, Materials, Procedure, Analysis
- Week 3의 gap을 해결하는 방법론

✅ **Results** (600-800 words):
- 주요 결과 + 최소 1개 Figure/Table
- 통계량 포함

**완벽하지 않아도 OK!**
→ 오늘 AI로 bulletproofing 할 예정

> Image suggestion: A checklist on a desk with items "Methods draft ✓", "Results draft ✓", "Figure/Table ✓". A friendly robot assistant (representing AI) standing next to the desk with a magnifying glass, ready to help inspect. Warm, encouraging colors.

---

# Part 1: 탑티어 저널의 거부 사유 (Top 10)

---

## 🚨 Methods 섹션 거부 사유 (Top 5)

| # | 거부 사유 | 리뷰어의 지적 | 발생 빈도 |
|---|---------|------------|---------|
| 1 | **Insufficient detail** | "다른 연구자가 재현 불가능" | ⭐⭐⭐⭐⭐ |
| 2 | **Inadequate controls** | "대안 설명을 배제하지 못함" | ⭐⭐⭐⭐ |
| 3 | **Sample size/power issues** | "통계적 검정력 부족" | ⭐⭐⭐⭐ |
| 4 | **Inappropriate statistics** | "분석이 데이터 구조에 안 맞음" | ⭐⭐⭐ |
| 5 | **Validation gaps** | "측정 도구 타당성 입증 부족" | ⭐⭐⭐ |

**핵심**: 리뷰어는 "내가 이 연구를 재현할 수 있는가?"를 묻는다

> Image suggestion: A rejected manuscript with red stamps showing the 5 rejection reasons. Each reason has a specific example callout (e.g., "Where's the N?", "What about confounds?", "Power analysis?"). Dramatic but professional style with red warning colors.

---

## 🚨 Results 섹션 거부 사유 (Top 5)

| # | 거부 사유 | 리뷰어의 지적 | 발생 빈도 |
|---|---------|------------|---------|
| 1 | **Overclaiming** | "데이터가 뒷받침 안 함" | ⭐⭐⭐⭐⭐ |
| 2 | **Cherry-picking** | "선택적 보고 의심" | ⭐⭐⭐⭐ |
| 3 | **Statistical issues** | "다중 비교 보정 누락" | ⭐⭐⭐⭐ |
| 4 | **Unclear presentation** | "핵심 결과가 불명확" | ⭐⭐⭐ |
| 5 | **Weak effect sizes** | "실질적 의미 미약" | ⭐⭐⭐ |

**핵심**: 리뷰어는 "주장이 데이터를 넘어서지 않는가?"를 묻는다

> Image suggestion: A balance scale. Left side: "Your Claims" (heavy, overloaded). Right side: "Your Data" (light, insufficient). The scale tips dangerously showing mismatch. Text overlay: "Claim-Evidence Mismatch = Rejection". Clean vector illustration.

---

## 🔍 실습 1: Rejection Reason 진단 (10분)

**Bad Methods 예시 (심리학 연구):**

```
"Participants were recruited online and completed a
questionnaire measuring anxiety. We analyzed the
data using ANOVA and found significant results."
```

**질문**: 위 Methods에서 찾을 수 있는 5가지 문제는?

1. 재현성: _________________
2. 통제: _________________
3. 샘플/검정력: _________________
4. 통계 적절성: _________________
5. 타당성: _________________

> Image suggestion: A detective (representing a reviewer) examining the bad Methods text with a magnifying glass, circling problematic parts. Speech bubbles with questions: "Which platform?", "What questionnaire?", "How many participants?", "What type of ANOVA?". Mystery/investigation theme.

---

## ✅ 진단 결과: AI vs Human

**AI 프롬프트:**
```
"다음 Methods 섹션을 Nature 리뷰어 관점에서 평가해줘:
[Methods text]

다음 5가지 측면에서 약점을 지적:
1. Reproducibility (재현성)
2. Controls (통제)
3. Sample size/power (샘플/검정력)
4. Statistical appropriateness (통계 적절성)
5. Validation (타당성)

각 약점에 대해:
- 구체적 문제점
- 리뷰어가 제기할 질문
- 개선 방안"
```

**AI의 진단과 여러분의 진단을 비교해보세요!**

> Image suggestion: Split screen comparison. Left: Human reviewer with sticky notes listing problems. Right: AI assistant with the same problems but with additional "Improvement suggestions" layer. Both pointing to the same Methods text in the middle. Collaborative theme.

---

# Part 2: Methods Bulletproofing 전략

---

## 🛡️ Reproducibility Checklist (재현성 체크)

**"다른 연구자가 정확히 재현할 수 있는가?"**

### 필수 포함 6가지 요소

- [ ] **Participants/Subjects**: 모집 방법, inclusion/exclusion criteria, demographics (N, M age, SD, gender)
- [ ] **Materials**: 자극/도구의 구체적 설명, 출처, 버전, 신뢰도/타당도
- [ ] **Procedure**: Step-by-step protocol, 각 단계의 타이밍/순서, 지시문
- [ ] **Parameters**: 모든 변수의 정확한 값, 범위, 단위, randomization 방법
- [ ] **Software/Equipment**: 이름, 버전, manufacturer, 설정값
- [ ] **Data processing**: Raw data → analyzed data 변환 과정, exclusion criteria

> Image suggestion: A six-part checklist board with each element represented by an icon (people for Participants, tools for Materials, flowchart for Procedure, sliders for Parameters, computer for Software, funnel for Data processing). Each with a large checkbox. Professional, organized layout.

---

## ❌ Before: 재현 불가능

```
"Participants completed a task measuring attention.
We used a standard protocol and analyzed the data
using appropriate statistical methods."
```

**문제점:**
- 어떤 task? 어떤 protocol?
- Participants 몇 명? 어떻게 모집?
- 어떤 statistical methods?

> Image suggestion: A confused researcher at a computer trying to replicate the study, surrounded by question marks and confused expressions. Speech bubble: "How do I replicate this??" Frustrated/confused theme with gray, muted colors.

---

## ✅ After: 재현 가능

```
"**Participants**: 60 undergraduate students (M age = 20.3,
SD = 1.8; 32 female) recruited via university participant
pool. Inclusion: normal/corrected vision, no ADHD diagnosis.

**Materials**: Sustained Attention to Response Test (SART;
Robertson et al., 1997). Stimuli: single digits 0-9 presented
for 250ms, ISI = 900ms. 225 trials (25 targets: digit '3').

**Procedure**: Participants pressed spacebar for non-targets,
withheld for targets. Presented using PsychoPy 3.2.4 on
24-inch monitor (60Hz, 60cm viewing distance).

**Analysis**: Mixed-effects logistic regression (lme4 package
in R 4.1.0) predicting error rates, with random intercepts
for participants."
```

**모든 6가지 요소 포함 ✓**

> Image suggestion: The same researcher now confidently replicating the study with all parameters clearly displayed on multiple monitors showing "60 participants", "SART task specs", "PsychoPy settings", etc. Successful, confident theme with green checkmarks.

---

## 🤖 AI 프롬프트: Reproducibility Audit

```
"다음 Methods 섹션을 읽고, 다른 연구자가 재현하려 할 때
막힐 수 있는 지점 10가지를 찾아줘:
[Methods text]

각 지점에 대해:
1. 무엇이 불명확한가?
2. 어떤 정보가 추가로 필요한가?
3. 구체적으로 어떻게 기술해야 하는가?
   (Before → After 예시 포함)"
```

**AI가 찾아주는 것:**
- 빠진 parameter 값
- 모호한 procedure 설명
- 누락된 software 버전
- 불명확한 exclusion criteria

> Image suggestion: AI robot with a clipboard conducting an audit of a Methods section document. The robot is highlighting 10 specific areas with magnifying glass icons, each connected to a "Fix" suggestion callout. Systematic, thorough inspection theme.

---

## 🛡️ Control Strategy Validation (통제 전략 검증)

**"대안 설명을 충분히 배제했는가?"**

### 4가지 Control 유형

| Control 유형 | 목적 | 예시 (심리학) |
|------------|-----|-------------|
| **Positive controls** | 기대 효과 확인 | Known effective manipulation이 작동하는지 |
| **Negative controls** | 무효과 확인 | Sham stimulation에서 효과 없음 |
| **Confound controls** | 혼재 변수 통제 | Task difficulty, arousal 통제 |
| **Validation controls** | 측정 타당성 | Manipulation check, attention check |

**리뷰어의 질문: "내가 생각한 다른 설명은 배제했나?"**

> Image suggestion: Four-quadrant diagram showing the 4 control types. Each quadrant has an icon (thumbs up for Positive, thumbs down for Negative, balance scales for Confound, checkmark for Validation) and a concrete psychology research example. Clear, educational layout.

---

## 🔍 Alternative Explanations 찾기

**예시 연구:**
- **Manipulation**: Positive mood induction (watching comedy clips)
- **Measurement**: Creative problem solving performance
- **Expected result**: Positive mood → better creativity

**Alternative explanations (AI가 생성):**
1. **Arousal** (not mood): 코미디가 각성만 높인 것
2. **Task engagement**: 재미있어서 더 집중한 것
3. **Demand characteristics**: 실험자 기대 파악한 것
4. **Time-on-task**: 코미디 시청 중 break 효과
5. **Baseline differences**: 두 그룹이 원래 달랐음

**각각을 어떻게 배제할 것인가?**

> Image suggestion: A central research finding surrounded by 5 alternative explanation bubbles, each trying to "attack" the main finding. Each alternative has a shield icon showing the control strategy that blocks it. Defense/protection metaphor.

---

## 🤖 AI 프롬프트: Alternative Explanation Generator

```
"내 연구 디자인:
- Manipulation: [설명]
- Measurement: [설명]
- Expected result: [설명]

다음을 생성해줘:
1. Alternative explanations (내 조작 외에 결과를 설명할 수 있는 요인 5가지)
2. 각 alternative를 배제하기 위한 control 조건
3. 리뷰어가 지적할 가능성이 높은 confound 3가지
4. 각 confound를 다루는 방법

그리고 현재 내 Methods에서:
- 충분히 다뤄진 alternative는?
- 추가해야 할 control은?"
```

> Image suggestion: AI as a "devil's advocate" character, raising hand with thought bubbles showing alternative explanations. Below each explanation, a researcher is shown implementing a control strategy. Adversarial but collaborative theme.

---

## 🛡️ Power & Sample Size Justification

**"샘플 사이즈가 충분한가?"**

### ❌ 약한 정당화 (거부 위험)

- "Previous studies used similar N" → 관례만 따름
- "We recruited as many as possible" → 계획 없음
- "N=30 is standard" → 근거 없음

### ✅ 강한 정당화 (통과 가능)

**A priori power analysis:**
```
"Based on pilot study (N=20), we expected medium effect
(Cohen's d = 0.5). Using G*Power with α=.05, power=.80,
we determined N=64 per group.

Sensitivity analysis: With final N=68 per group, we can
detect effects ≥ d=0.48 with 80% power."
```

**포함 요소:**
- 예상 effect size + 근거 (pilot/previous work)
- α, power (1-β) 명시
- 사용 소프트웨어 (G*Power)
- Sensitivity analysis (실제 달성 가능한 MDE)

> Image suggestion: Two paths diverging. Left path (red): "Weak justification" leading to a rejection letter. Right path (green): "Strong justification" with G*Power screenshot, pilot data, and effect size calculation leading to acceptance. Clear contrast in outcomes.

---

## 🤖 AI 프롬프트: Power Analysis Reviewer

```
"내 연구 계획:
- Expected effect size: d = [value] (근거: [pilot/previous work])
- Sample size: N = [value]
- Alpha: 0.05
- Planned comparisons: [number]

리뷰어 관점에서 평가해줘:
1. Expected effect size가 현실적인가? (너무 크거나 작지 않은가?)
2. Multiple comparison 보정을 고려하면 power가 충분한가?
3. 샘플 사이즈 정당화에서 보강할 점은?
4. Sensitivity analysis 결과를 어떻게 제시해야 하는가?

그리고:
- 리뷰어가 제기할 가능성 높은 질문 3가지
- 각 질문에 대한 방어 전략"
```

> Image suggestion: AI wearing a reviewer's hat examining a power analysis document with a critical eye. Magnifying glass over "Effect size justification" and "Sensitivity analysis" sections. Speech bubbles with potential reviewer questions and suggested defenses.

---

# Part 3: Results Bulletproofing 전략

---

## ⚠️ Overclaiming Prevention (과장 주장 방지)

**"주장이 데이터를 넘어서지 않는가?"**

### 흔한 Overclaiming 패턴

| Claim | Data | Problem | Conservative Alternative |
|-------|------|---------|--------------------------|
| "X **causes** Y" | Correlation X-Y | Correlation ≠ Causation | "X is **associated with** Y" |
| "X is **necessary** for Y" | Y↓ when X removed | Sufficiency not tested | "X **contributes to** Y" |
| "Works **in general**" | Tested in one condition | No generalization | "Works **in [condition]**" |
| "This **proves** Z" | Consistent with Z | Alternatives not ruled out | "**Consistent with** Z" |

**핵심**: 데이터가 뒷받침하는 범위 내에서만 주장

> Image suggestion: A tightrope walker (representing a claim) balancing on a rope labeled "Data support". Below are safety nets labeled with conservative language ("associated", "contributes", "consistent with"). Above are clouds labeled with overclaiming words ("causes", "proves", "always") shown as unreachable. Risk vs safety theme.

---

## ❌ Before: Overclaiming

**Bad Results 문장 (심리학 연구):**

```
"These results **prove** that mindfulness meditation
**causes** improved attention in all populations. Our
findings **demonstrate** that meditation is **necessary**
for attentional enhancement and **guarantees** cognitive
benefits for everyone who practices it."
```

**문제점:**
- Correlation을 causation으로 주장
- Limited sample을 "all populations"로 일반화
- "Necessary"와 "guarantees"는 데이터 초과

**Overclaiming Risk Score: 9/10** 🚨

> Image suggestion: A red warning sign with the overclaimed statement, with specific words highlighted in red ("prove", "causes", "all", "necessary", "guarantees"). Each highlighted word has a strikethrough. Alarm bells ringing around it.

---

## ✅ After: Conservative Claim

**Good Results 문장:**

```
"These results **suggest** that mindfulness meditation is
**associated with** improved attention **in our sample of
young adults**. Our findings are **consistent with** the
hypothesis that meditation **contributes to** attentional
enhancement, though **additional research is needed** to
determine the **generalizability** and **necessary conditions**
for this effect."
```

**개선점:**
- "Prove" → "Suggest"
- "Causes" → "Associated with"
- "All populations" → "In our sample"
- "Necessary" → "Contributes to"
- 한계 인정 + generalizability 언급

**Overclaiming Risk Score: 2/10** ✅

> Image suggestion: The same statement rewritten in green with conservative language highlighted. Each change is annotated with why it's better (e.g., "suggest" = acknowledges uncertainty). Checkmarks next to each improvement. Positive, safe theme.

---

## 🤖 AI 프롬프트: Claim Checker

```
"다음 Results 문장들을 분석해줘:
[Results text with claims]

각 문장에 대해:
1. Claim type (causal/correlational/mechanistic/general)
2. Evidence level (direct/indirect/suggestive)
3. Overclaiming risk (1-10)
4. Conservative alternative phrasing

그리고:
- 가장 위험한 overclaim 3개 지적
- 각각을 데이터에 맞게 수정하는 방법"
```

**AI가 체크하는 것:**
- Causal language (causes, leads to, produces)
- Generalization (all, always, everyone)
- Certainty (proves, demonstrates, shows definitively)

> Image suggestion: AI as a "claim inspector" with a checklist, examining Results statements under a magnifying glass. Each statement gets a risk score (1-10) and alternative phrasing suggestions appear in green bubbles. Quality control theme.

---

## 📊 Statistical Rigor Verification (통계적 엄밀성)

**"통계 분석이 방어 가능한가?"**

### Critical Checkpoints

- [ ] **Assumption testing**: Normality, homogeneity, independence 확인 + 위배 시 대안
- [ ] **Multiple comparisons**: Bonferroni/FDR/permutation 보정 명시
- [ ] **Effect sizes**: p-value만이 아닌 effect size + CI 보고
- [ ] **Outlier handling**: 처리 방법 + 영향 평가 (with vs without)
- [ ] **Missing data**: 처리 방법 + sensitivity analysis
- [ ] **Robustness checks**: Alternative analysis로 결과 확인

**리뷰어는 "통계적 허점"을 찾는다!**

> Image suggestion: A fortress wall with 6 defensive towers, each labeled with one checkpoint. Each tower has a shield with a checkmark. Arrows labeled "Reviewer attacks" bouncing off the well-defended fortress. Strong defense metaphor.

---

## ❌ Before: 통계적 허점

```
"Group A performed better than Group B (p < 0.05)."
```

**문제점:**
- Descriptive stats 없음 (M, SD)
- Effect size 없음 (얼마나 차이?)
- CI 없음 (불확실성?)
- Multiple comparison 고려 안 됨
- Assumptions 체크 안 됨

**리뷰어 반응:** "이것만으로는 부족합니다" ❌

> Image suggestion: A sparse, minimal Results statement with a reviewer pointing to all the missing elements with red circles. Each missing element has a question mark: "Where's the M/SD?", "Effect size?", "CI?", "Assumptions?". Incomplete/inadequate theme.

---

## ✅ After: 통계적으로 견고함

```
"**Assumption testing**: Shapiro-Wilk tests confirmed normality
for both groups (ps > .05). Levene's test showed homogeneity
of variance (p = .42).

**Primary analysis**: Group A (M = 85.3, SD = 12.1) significantly
outperformed Group B (M = 72.4, SD = 10.8), t(98) = 5.43,
p < .001, Cohen's d = 1.12, 95% CI [0.71, 1.53].

**Robustness check**: Non-parametric Mann-Whitney U test
confirmed the same pattern (U = 1847, p < .001).

**Multiple comparison note**: Bonferroni-corrected threshold
(α = .025 for 2 planned comparisons) maintained significance."
```

**모든 checkpoints 충족 ✓**

> Image suggestion: A complete, well-formatted Results paragraph with all elements clearly labeled and highlighted: "Assumptions ✓", "Descriptive stats ✓", "Effect size ✓", "CI ✓", "Robustness ✓", "Multiple comparison ✓". Full, comprehensive defense. Green checkmarks everywhere.

---

## 🤖 AI 프롬프트: Statistical Review

```
"내 Results 섹션:
- Analysis: [통계 분석 방법]
- Comparisons: [비교 횟수]
- Reported stats: [제시한 통계량]

리뷰어가 통계적으로 문제 삼을 수 있는 부분:
1. Assumption violations (어떤 가정이 문제?)
2. Multiple comparison issues (보정이 충분한가?)
3. P-hacking risks (의심받을 수 있는 분석 선택은?)
4. Missing robustness checks (어떤 추가 분석 필요?)

각 문제에 대해:
- 구체적 지적 내용
- 방어 전략
- 추가할 분석/보고 내용"
```

> Image suggestion: AI wearing a "Statistical Reviewer" badge, examining a Results section with a checklist of the 4 problem areas. For each identified problem, the AI provides specific defense strategies shown as shields blocking reviewer attacks.

---

## 🔍 Transparent Reporting (투명한 보고)

**"모든 결과를 투명하게 보고했는가?"**

### Selective Reporting 위험 신호

❌ **위험한 행동:**
- Hypothesis에 맞지 않는 결과 누락
- 일부 조건/측정치만 보고
- Failed manipulation checks 언급 없음
- Exploratory를 confirmatory처럼 보고

✅ **안전한 행동:**
- 모든 planned comparison 보고 (유의/비유의 모두)
- Primary outcome measures 전부
- Supplementary에 나머지 결과
- Exploratory 명확히 표시

**리뷰어는 "무엇을 숨겼나?"를 의심한다**

> Image suggestion: An iceberg metaphor. Above water (Main Results): visible findings. Below water (Supplementary): all other results, manipulation checks, robustness checks, excluded data. A transparent glass iceberg showing everything clearly. Transparency theme.

---

## 🤖 AI 프롬프트: Transparency Checker

```
"내 연구 계획:
- Hypotheses: [list]
- Planned comparisons: [list]
- Measured variables: [list]

현재 Results 섹션:
[Results text]

투명성 평가:
1. Planned 대비 보고된 비율 (%)
2. 누락된 결과가 있는가? 어떤 것?
3. Exploratory vs Confirmatory 구분이 명확한가?
4. Selective reporting 의심받을 수 있는 부분은?

개선 방안:
- Main에 추가할 결과
- Supplementary로 옮길 결과
- 투명성 강화를 위한 문구 제안"
```

**AI가 체크:** 계획 vs 보고 일치율

> Image suggestion: AI comparing two documents side-by-side. Left: "Planned analyses" checklist. Right: "Reported results" section. AI highlighting discrepancies with yellow markers and suggesting additions. Audit/verification theme.

---

# Part 4: Advanced Bulletproofing 전략

---

## 🎯 Preemptive Reviewer Response

**"리뷰어가 물어볼 질문을 미리 예측하고 답변"**

### AI로 Anticipated Questions 생성

```
"내 Methods/Results:
[전체 텍스트]

Nature/Science 리뷰어가 제기할 가능성이 높은 질문 10가지를 생성해줘.
각 질문에 대해:
1. 질문 유형 (reproducibility/controls/statistics/interpretation)
2. 심각도 (critical/major/minor)
3. 현재 Methods/Results에서 답변이 있는가?
4. 없다면, Methods/Results에 추가할 내용
5. Rebuttal letter에서 답변할 내용

우선순위 순으로 정렬해줘."
```

> Image suggestion: A chess game metaphor. Researcher (white pieces) anticipating reviewer's (black pieces) moves several steps ahead. Each anticipated question is a chess move, with prepared defenses shown as countermoves. Strategic planning theme.

---

## 📝 예측 질문 예시 (심리학 연구)

**AI가 생성한 Critical Questions:**

1. **Q**: "How did you ensure participants were actually paying attention during the 30-minute task?"
   - **Type**: Validation
   - **Severity**: Critical
   - **Current answer?**: ❌ No
   - **Add to Methods**: Attention check trials (10% of total)
   - **Add to Results**: Exclusion based on attention check failure (<80%)

2. **Q**: "Did you control for baseline differences in anxiety between groups?"
   - **Type**: Controls
   - **Severity**: Critical
   - **Current answer?**: ❌ No
   - **Add to Methods**: Pre-test anxiety measure (BAI)
   - **Add to Results**: ANCOVA with baseline as covariate

**Preemptive Defense**: Methods/Results에 미리 답변 삽입!

> Image suggestion: A two-column layout. Left: "Reviewer Questions" with speech bubbles containing critical questions. Right: "Preemptive Defenses" showing how each question is addressed in the Methods/Results text. Arrows connecting questions to their defenses. Proactive defense theme.

---

## 🔄 Methods/Results Cross-Validation

**"Methods에서 약속한 것을 Results에서 전부 다뤘는가?"**

### 흔한 불일치

❌ **Methods에 있지만 Results에 없음:**
- "We measured anxiety using BAI" → Results에 BAI 결과 없음
- "Control condition included" → Results에 control 결과 없음
- "Outliers >3SD removed" → Results에 excluded N 보고 없음

❌ **Results에 있지만 Methods에 설명 없음:**
- Exploratory correlation 분석 결과
- Post-hoc comparison
- Additional robustness check

**리뷰어는 이런 불일치를 즉시 발견!**

> Image suggestion: Two documents (Methods and Results) side-by-side with arrows connecting related elements. Some arrows are green (matched), some are red (mismatched - mentioned in one but not the other). A reviewer with a red pen circling the mismatches. Consistency check theme.

---

## 🤖 AI 프롬프트: Consistency Checker

```
"내 Methods 섹션:
[Methods text]

내 Results 섹션:
[Results text]

일관성 체크:
1. Methods에 있지만 Results에 없는 분석/측정/조건
2. Results에 있지만 Methods에 설명 없는 분석
3. 용어 불일치 (같은 것을 다르게 지칭)
4. 숫자 불일치 (N, df 등)

각 불일치에 대해:
- 문제 유형
- 수정 방법 (Methods 추가 vs Results 추가 vs 삭제)"
```

**AI가 찾아주는 불일치를 해결!**

> Image suggestion: AI as a "quality controller" with two clipboards (Methods and Results), checking items off and connecting matching elements with green lines. Red X marks on mismatches. Below, a list of "Fixes needed" with specific actions. Quality assurance theme.

---

## 📊 Effect Size + Significance 통합 보고

**"통계적으로 유의 + 실질적으로 의미 있는가?"**

### ❌ P-value만으로는 부족

```
"p < 0.05이므로 유의하다"
```

**문제:** 실질적 크기를 알 수 없음

### ✅ 완전한 보고 (권장 템플릿)

```
"Group A (M = 85.3, SD = 12.1) significantly outperformed
Group B (M = 72.4, SD = 10.8), t(98) = 5.43, p < .001,
Cohen's d = 1.12, 95% CI [0.71, 1.53]."
```

**포함 요소:**
- Descriptive stats (M, SD)
- Inferential stats (t, df, p)
- Effect size (Cohen's d)
- Confidence interval (95% CI)

> Image suggestion: A layered pyramid. Bottom layer: "Descriptive stats (M, SD)". Second layer: "Inferential stats (t, p)". Third layer: "Effect size (d)". Top layer: "Confidence Interval (CI)". Text: "Complete Statistical Reporting Pyramid". All layers needed for solid foundation.

---

## 🎯 Practical Significance 평가

**"통계적 유의 ≠ 실질적 의미"**

### 예시: 통계적으로는 유의하지만...

```
"Meditation group improved by 2 points on 100-point
attention scale, t(198) = 2.15, p = .03, d = 0.15"
```

**문제:**
- p < .05 (통계적 유의) ✓
- 하지만 Cohen's d = 0.15 (very small effect)
- 2-point 차이가 실제로 의미 있는가?

### AI 프롬프트로 평가

```
"내 주요 발견:
- Effect size: Cohen's d = 0.15
- Comparison: Meditation (M=52) vs Control (M=50) on 100-point scale

이 effect size가 실질적으로 의미 있는가?
- 해당 분야에서 어느 정도 크기?
- Minimum clinically/practically important difference는?
- 리뷰어가 '실질적 의미 없다'고 지적할 위험?"
```

> Image suggestion: A scale showing "Statistical Significance" on one side (large, heavy) and "Practical Significance" on the other side (small, light). The scale tips heavily showing imbalance. Text overlay: "Both needed for strong claims". Balance/imbalance metaphor.

---

## 📈 Figure/Table Optimization

**"결과를 가장 명확하게 보여주는가?"**

### Common Figure Mistakes

1. ❌ **No error bars**: 변동성 표시 없음
2. ❌ **Misleading Y-axis**: 범위 조작으로 효과 과장
3. ❌ **Too much info**: 한 figure에 너무 많은 내용
4. ❌ **No raw data**: Bar/line만 있고 개별 데이터 없음
5. ❌ **Inconsistent formatting**: Figure들 간 스타일 불일치

### ✅ Good Figure 체크리스트

- [ ] Error bars/CI 표시
- [ ] Y-axis 범위 적절 (0부터 시작 or 정당한 이유)
- [ ] Individual data points 표시 (if N < 100)
- [ ] Clear labels, legends
- [ ] Consistent style across figures

> Image suggestion: Two bar charts side-by-side. Left (bad): No error bars, Y-axis starts at 60 (exaggerating small difference), cluttered. Right (good): Error bars, Y-axis from 0, individual points overlaid, clean design. Clear contrast with annotations pointing out differences.

---

## 🤖 AI 프롬프트: Figure Critique

```
"내 figure 설명:
- Type: [bar/line/scatter 등]
- X-axis: [변수]
- Y-axis: [측정치, 범위]
- Error representation: [SEM/SD/CI/none]
- Sample size: N = [value]

리뷰어 관점에서 비판:
1. Y-axis 범위가 적절한가? (효과를 과장/축소하지 않는가?)
2. Error bars가 충분한가? (SEM vs SD vs CI 중 무엇이 적절?)
3. 개별 데이터 포인트를 보여줘야 하는가?
4. 이 figure 없이 text/table로 충분한가?
5. 여러 panel로 나눠야 하는가?

개선 제안 (구체적으로):"
```

> Image suggestion: AI as an "art critic" examining a Figure with a critical eye, holding a red pen. Speech bubbles with common criticisms ("Why no error bars?", "Y-axis suspicious", "Too cluttered"). Below, a revised "improved" version of the same figure with all issues fixed. Before/after contrast.

---

# Part 5: Peer Review & Workshop

---

## 👥 Structured Peer Review Protocol

**각 학생이 2명의 동료 Methods/Results를 평가**

### Methods 평가 (3개 항목)

1. **Reproducibility** (1-5점): ___
   - 내가 이 연구를 재현하려 할 때 막힐 부분:
   - 추가로 필요한 정보:

2. **Controls** (1-5점): ___
   - Alternative explanations이 충분히 배제됐는가?
   - 내가 리뷰어라면 추가할 control:

3. **Statistical Justification** (1-5점): ___
   - Sample size 정당화가 설득력 있는가?
   - 분석 방법이 데이터 구조에 적합한가?

> Image suggestion: A peer review template document with the 3 Methods evaluation criteria shown as a form. Each criterion has a 1-5 star rating system and text boxes for comments. Professional peer review process theme.

---

## 👥 Structured Peer Review Protocol (계속)

### Results 평가 (3개 항목)

4. **Claim-Evidence Match** (1-5점): ___
   - Overclaiming 위험이 있는 문장 (있다면 지적):
   - 보수적으로 수정할 방법:

5. **Statistical Rigor** (1-5점): ___
   - 빠진 통계량/검정:
   - Multiple comparison 처리 적절한가?

6. **Transparency** (1-5점): ___
   - 선택적 보고 의심 부분:
   - 추가로 보고해야 할 결과:

### 종합 평가

- 가장 큰 약점 1가지:
- 개선 우선순위 top 3:
- Nature/Science 제출 준비도 (1-10):

> Image suggestion: Continuation of the peer review template showing the 3 Results evaluation criteria with the same 1-5 star rating system. At the bottom, a summary section with "Overall Readiness" gauge showing 1-10 scale. Complete evaluation form theme.

---

## 🏋️ Workshop 실습 구조 (75분)

### Phase 1: Bulletproofing Audit (30분)

**Activity 1** (15분): **Methods Reproducibility Check**
- AI로 재현성 취약점 10가지 도출
- 각 취약점 개선 방법 논의
- 6가지 필수 요소 충족 체크

**Activity 2** (15분): **Results Claim Checker**
- Overclaiming 위험 문장 식별 (AI 활용)
- Effect size + practical significance 평가
- Conservative alternative phrasing 작성

> Image suggestion: A workshop timeline showing Phase 1 as the first 30 minutes. Two parallel tracks: "Methods track" (15min) and "Results track" (15min). Each track shows key activities with icons (magnifying glass for audit, checkboxes for requirements). Active, energetic theme.

---

## 🏋️ Workshop 실습 구조 (계속)

### Phase 2: Statistical Rigor (25분)

**Activity 3** (15분): **Power Analysis Review**
- AI로 sample size 정당화 강화
- Multiple comparison 보정 체크
- Sensitivity analysis 추가

**Activity 4** (10min): **Transparency Audit**
- Selective reporting 위험 평가
- 추가 보고 필요 항목 리스트
- Exploratory vs Confirmatory 구분

> Image suggestion: Workshop timeline Phase 2 (25 minutes). Two sequential activities shown as connected boxes. Icons: calculator/graph for Power Analysis, checklist for Transparency. Statistical/analytical theme.

---

## 🏋️ Workshop 실습 구조 (계속)

### Phase 3: Peer Review (25분)

**Activity 5**: **Structured Peer Review**
- 2명 동료 평가 (template 사용)
- 6가지 평가 항목별 점수 + 피드백
- 리뷰어 질문 예측 및 방어 전략 논의

### Phase 4: 최종 개선 + 공유 (10분)

**Activity 6**: **AI로 피드백 통합**
- 받은 피드백을 AI에 입력
- 개선안 생성 (7분)
- 가장 효과적이었던 bulletproofing 전략 공유 (3분)

**총 Workshop: 90분 (강의 15분 + 실습 75분)**

> Image suggestion: Complete workshop timeline showing all 4 phases in sequence. Phase 3 (peer review) shows two people exchanging documents with feedback arrows. Phase 4 shows AI helping to integrate all feedback into final improved version. Collaborative conclusion theme.

---

## 📝 과제: "My Methods/Results - Bulletproofed"

### 제출물 (총 5개 섹션)

**1. Methods 섹션 완성** (800-1000 words)
- Reproducibility checklist 6가지 모두 충족
- Control strategy 정당화
- Statistical power/sample size 근거

**2. Results 섹션 완성** (600-800 words)
- 모든 주요 결과 (effect size + CI + p)
- Figure/Table 최소 1개
- Overclaiming 없는 conservative claims

**3. Bulletproofing Documentation** (800 words)
- AI를 활용한 self-critique 결과
- 예상 리뷰어 질문 5개 + 방어 전략

> Image suggestion: A checklist showing the 5 assignment sections with word counts and key requirements. Each section has icons (document for Methods/Results, shield for Bulletproofing, AI icon for AI usage, people for Peer Review). Organized assignment structure.

---

## 📝 과제: "My Methods/Results - Bulletproofed" (계속)

**4. AI 활용 과정** (500 words)
- 사용한 프롬프트 레시피 **5개 이상**
- 각 레시피의 효과 및 한계
- AI의 한계 및 인간 판단이 필요했던 지점

**5. Peer Review 반영** (300 words)
- 받은 피드백 요약 (6가지 평가 항목별)
- 각 피드백을 어떻게 반영했는지

### 평가 기준

- **Reproducibility & Rigor** (40%): 재현성, control, 통계 정당화
- **Transparent Reporting** (25%): 완전 보고, overclaiming 방지
- **Reviewer-Ready** (20%): 예상 질문 대응, preemptive defense
- **AI 활용 & Peer Review** (15%): 효과적 프롬프트, 피드백 반영

> Image suggestion: A grading rubric pie chart showing the 4 evaluation categories with percentages (40%, 25%, 20%, 15%). Each slice has an icon representing the category. Clear, professional assessment criteria visualization.

---

## 🎯 핵심 메시지

### Bulletproof Methods/Results = 5가지 요소

```
Reproducibility (6가지 요소 충족)
         +
Control (alternative explanation 배제)
         +
Statistical Rigor (power, assumptions, effect size)
         +
Transparent Reporting (모든 결과, no overclaiming)
         +
Preemptive Defense (예상 질문에 미리 답변)
         =
Nature/Science 리뷰어가 공격할 틈 없는 Methods/Results
```

**CoT의 역할:**
> "윤경생 강의에서 CoT **기법**을 배웠다면, 본 강의에서는 CoT를 '리뷰어 공격 방어'라는 **목표**에 전략적으로 활용"

> Image suggestion: A fortress with 5 defensive layers, each labeled with one of the 5 elements. At the center, a well-protected Methods/Results section. Outside, reviewer "attacks" (arrows) bouncing off each layer. At the bottom, text: "Impenetrable Defense Through Systematic Bulletproofing". Strong, confident completion theme.

---

## 💬 토론 주제

### 각자의 경험 공유

1. **Reproducibility**:
   - 자신의 Methods에서 가장 취약한 부분은?
   - AI가 찾아준 10가지 취약점 중 예상 못했던 것은?

2. **Overclaiming**:
   - Results에서 데이터를 넘어서는 주장을 하고 있었나?
   - Conservative phrasing으로 바꾸면 주장이 약해 보이는가?

3. **Statistical Rigor**:
   - Multiple comparison을 고려하면 결과가 여전히 유의한가?
   - Effect size가 실질적으로 의미 있는 크기인가?

4. **Reviewer Questions**:
   - AI가 예측한 리뷰어 질문 중 가장 날카로운 것은?
   - Preemptive defense를 Methods/Results에 어떻게 삽입했는가?

> Image suggestion: A discussion circle with 4-6 people talking, with speech bubbles showing the 4 discussion topics. Each person has a different Methods/Results document, sharing insights and learning from each other. Collaborative learning theme.

---

## 📚 다음 주 준비사항

### Week 5: Discussion 섹션

**과제:**
- **Discussion 섹션 초안 작성** (1000-1200 words)
  - 결과의 broader implications
  - 선행 연구와의 비교/통합
  - 한계점 및 future directions
  - Conclusion

**통합 작업:**
- Abstract → Introduction → Methods → Results → Discussion
- 전체 논문 일관성 체크
- Cross-referencing 확인

**AI 활용:**
- Discussion 섹션 전략 (Week 5에서 다룰 예정)
- 논문 전체의 narrative flow 체크

> Image suggestion: A roadmap showing the completed journey (Weeks 1-4: Abstract, Intro, Gap, Methods/Results) with checkmarks, and the upcoming destination (Week 5: Discussion, shown as a glowing target ahead). Also shows the final destination: "Complete Top-Tier Manuscript". Journey/progress theme.

---

## 🎓 참고 자료

### 추천 읽기

**Methods 섹션 참고:**
- Nature/Science Methods 섹션 10편
  - Reproducibility 달성 방법
  - Control strategy 패턴 파악

**Statistical Reporting:**
- APA Publication Manual (7th ed.)
  - Statistical reporting guidelines
  - Effect size reporting standards

**AI 도구 활용:**
- **ChatGPT**: Reproducibility audit, alternative explanation generation
- **Claude**: Statistical review, reviewer question prediction
- **Perplexity**: 통계 방법 best practices 검색
- **G*Power**: Power analysis (전용 소프트웨어)

### 프롬프트 레시피 라이브러리
- 공유 게시판에서 동료들의 효과적 bulletproofing 프롬프트 참고

> Image suggestion: A library shelf with different books labeled "Nature Methods Examples", "APA Manual", "AI Tools Guide", "Prompt Recipes". An AI assistant (robot character) pulling books and showing them to students. Resource/learning materials theme.

---

## ✨ 오늘의 핵심 Takeaway

### 3가지 기억할 점

1. **Reproducibility = 6가지 요소**
   - Participants, Materials, Procedure, Parameters, Software, Data processing
   - "다른 연구자가 재현할 수 있는가?" 자문

2. **Claim ≤ Data**
   - Overclaiming은 가장 흔한 거부 사유
   - Conservative language: "associated with", "consistent with", "suggests"

3. **Complete Statistical Reporting**
   - M, SD, t/F, p, effect size, CI 모두 보고
   - Assumptions, multiple comparisons, robustness 체크

**실천 사항:**
- 오늘 배운 AI 프롬프트 5개 이상 자신의 논문에 적용
- 동료 피드백을 진지하게 반영
- Bulletproofing은 방어가 아닌 **품질 향상**

> Image suggestion: Three key takeaway cards, each with an icon and concise summary. Card 1: 6-element checklist icon. Card 2: Balance scale (claim vs data). Card 3: Complete stats pyramid. Below, a student confidently working on their manuscript with all 3 cards visible on their desk. Confidence/mastery theme.

---

## 감사합니다! 🙏

**다음 주 (Week 5) Preview:**

📖 **Discussion 섹션 작성 전략**
- Implications: 결과가 왜 중요한가?
- Integration: 기존 문헌과 어떻게 연결되는가?
- Limitations: 약점을 어떻게 솔직하게 인정하는가?
- Future Directions: 다음 연구는?

**준비물:**
- Discussion 초안 (1000-1200 words)
- 전체 논문 통합본 (Abstract → Discussion)

**오늘 배운 Bulletproofing 전략을 바로 적용하세요!**

리뷰어가 공격할 틈이 없는 Methods/Results를 완성하세요! 💪

> Image suggestion: A celebratory scene with students successfully completing their bulletproofed Methods/Results sections. In the background, a preview poster of Week 5 showing "Discussion Section" with the 4 key elements (Implications, Integration, Limitations, Future). Forward-looking, encouraging, accomplished theme with warm, positive colors.
