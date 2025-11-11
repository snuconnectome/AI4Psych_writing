---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Noto Sans KR', sans-serif;
    font-size: 28px;
  }
  h1 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
  }
  h2 {
    color: #34495e;
  }
  table {
    font-size: 22px;
  }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
  .bad { color: #e74c3c; }
  .good { color: #27ae60; }
---

# Week 2: AI 활용 I
## Nature/Science급 초록 작성 전략

**심리과학 연구방법 - 롸이팅**

---

<!-- _class: lead -->

# Part 0: Orientation

---

## 📋 학습 목표

### 궁극 목표
**"어떻게 하면 Nature/Science급 탑티어 초록을 작성할 것인가?"**

### 구체적 목표
1. **Nature/Science 초록의 DNA 발견**: 탑티어 vs 일반 저널 차별화 요소 파악
2. **4가지 Opening 패턴 마스터**: Problem/Gap/Opportunity/Challenge-driven
3. **Broad Significance Framing**: 좁은 기여 → 넓은 임팩트로 확장
4. **AI 전략적 활용**: 효과적인 프롬프트 레시피 개발 및 공유

---

## ⚠️ 오늘은 AI 개념 설명 없음!

**윤경생 박사님 강의에서 이미 학습:**
- ✅ Prompt Engineering 기초 (Instruction, Context, Input, Output)
- ✅ Parameters (Temperature, Top-k, Top-p)
- ✅ In-context Learning (zero-shot, one-shot, few-shot)

**따라서 이 수업:**
- ❌ AI 개념 설명 생략
- ✅ **실전 적용에만 집중**
- ✅ "어떻게 탑 5% 초록을 쓸 것인가?"

---

<!-- _class: lead -->

# Part 1: Nature/Science DNA

---

## Nature/Science 초록 vs 일반 저널 초록

| 요소 | 🏆 탑티어 저널 | 📄 일반 저널 |
|------|---------------|-------------|
| **Significance** | Broad scientific/societal impact | Narrow disciplinary contribution |
| **Claims** | Bold + solid evidence | Cautious incremental findings |
| **Language** | Accessible to broad readership | Jargon-heavy technical writing |
| **"Why matters"** | Explicit from first sentence | Implicit or buried |
| **Impact** | Quantifiable (%, fold, effect size) | Descriptive ("significant") |

**핵심:** Nature/Science는 **넓은 독자층**을 위한 글쓰기

---

## Opening 차이: Real Example from Nature Human Behaviour (2025)

<div class="columns">

<div>

### ❌ 일반 저널 Opening (가상 예시)

```
Large language models like GPT-4
are becoming increasingly popular.

Previous research has investigated
AI persuasion capabilities.
```

**문제:**
- 기술 트렌드 소개만
- 왜 중요한지 불명확
- Narrow audience (AI 연구자만)

</div>

<div>

### ✅ Nature Human Behaviour Opening (2025)

```
Early work has found that LLMs can
generate persuasive content. However,
evidence on whether they can also
personalize arguments to individual
attributes remains limited, despite
being crucial for assessing misuse.
```

**강점:**
- Problem-driven 패턴: AI 오용 위험성
- "Despite being crucial" → 중요성 즉시 명확
- Broad impact: AI governance, platform design
- **순수 행동 실험 (N=900)으로도 Nature급 가능**

</div>

</div>

---

## Significance Framing 차이: Before/After

<div class="columns">

<div>

### ❌ Narrow Significance

```
This study advances our
understanding of memory
consolidation in rats.
```

**문제:**
- Rat memory (좁은 관심사)
- 기초과학만 언급
- Societal relevance 없음

</div>

<div>

### ✅ Broad Significance

```
Understanding how memories are
stabilized is fundamental to
treating neurodegenerative
diseases and enhancing learning—
this study reveals a previously
unknown mechanism.
```

**강점:**
- Human diseases (넓은 관심)
- Translational potential
- Cross-disciplinary appeal

</div>

</div>

---

<!-- _class: lead -->

# Part 2: 4 Opening Patterns

---

## 고임팩트 Opening의 4가지 패턴

### 1. 🚨 Problem-Driven
**"Despite decades of research, X remains unsolved..."**
→ 해결되지 않은 중요한 문제 강조

### 2. 🔍 Gap-Driven
**"While Y is well-established, we lack understanding of Z..."**
→ 알려진 것과 모르는 것의 대비

### 3. 🚀 Opportunity-Driven
**"Recent advances in X enable unprecedented investigation of Y..."**
→ 새로운 기술/방법론이 가능하게 한 연구

### 4. 💡 Challenge-Driven
**"X poses a fundamental challenge to our understanding of Y..."**
→ 기존 이론/패러다임에 대한 도전

---

## Opening 패턴 예시 1-2

### 1. Problem-Driven (우울증 치료 예시)

```
Despite extensive research on depression treatment, 60% of patients
fail to achieve remission with first-line therapies—a critical gap
limiting personalized psychiatric care.
```

**왜 효과적:**
- 즉시 문제의 심각성 (60% failure)
- Broad impact (환자 치료)
- Unmet need 명확

---

### 2. Gap-Driven (스트레스와 도파민 예시)

```
While the role of dopamine in reward learning is well-established,
we lack understanding of how dopamine systems adapt during chronic
stress—essential for depression pathophysiology.
```

**왜 효과적:**
- Established knowledge 인정
- Gap 명확히 제시
- Clinical relevance (우울증)

---

## Opening 패턴 예시 3-4

### 3. Opportunity-Driven (디지털 정신건강 예시)

```
Recent advances in smartphone sensing enable unprecedented real-time
monitoring of behavioral markers—opening new possibilities for early
detection of psychiatric episodes.
```

**왜 효과적:**
- 새로운 기술 (smartphone sensing)
- "Unprecedented" 강조
- Clinical application 명확

---

### 4. Challenge-Driven (재현성 위기 예시)

```
Replication failures in social psychology pose a fundamental challenge
to our understanding of human behavior—demanding new methodological
frameworks for robust science.
```

**왜 효과적:**
- 분야 전체의 위기 인식
- "Fundamental challenge" 강조
- Meta-scientific impact

---

<!-- _class: lead -->

# Part 3: Broad Significance + Quantitative Results

---

## Narrow → Broad Significance 변환

<div class="columns">

<div>

### ❌ Narrow Examples

```
"We investigated AI persuasion
in online debates."
```

```
"GPT-4 showed higher persuasion
rates than humans."
```

```
"AI can personalize arguments
to individuals."
```

</div>

<div>

### ✅ Broad Examples (Pair B - Nature 2025)

```
"Has implications for the
governance and design of
online platforms."
```

**Why Better:**
- AI governance → 정책, 규제
- Platform design → 소셜 미디어, 민주주의
- Misinformation → 사회적 위험
- Cross-disciplinary: AI + Ethics + Policy

</div>

</div>

**실제 Nature 예시:** "Our findings highlight the power of LLM-based persuasion and have **implications for the governance and design of online platforms.**" (Salvi et al., Nature Human Behaviour 2025)

---

## 정량적 결과 표현: Real Example (Pair B)

<div class="columns">

<div>

### ❌ 모호한 표현

```
"GPT-4 was more persuasive
than humans."
```

```
"AI showed significant effects
on agreement (p<0.05)."
```

```
"Personalization improved
persuasion."
```

</div>

<div>

### ✅ Nature 2025 Quantitative (5가지 지표!)

```
"GPT-4 with personalization was
more persuasive 64.4% of the time
(81.2% relative increase in odds;
95% CI: [+26.0%, +160.7%],
P < 0.01; N = 900)."
```

**5가지 정량 지표:**
1. **64.4%** - Success rate
2. **81.2% increase** - Effect size
3. **95% CI** - Confidence interval
4. **P < 0.01** - Statistical significance
5. **N = 900** - Sample size

</div>

</div>

**핵심:** Nature는 "얼마나 강했는가"를 정량적으로 요구!

---

<!-- _class: lead -->

# Part 4: Workshop Preparation

---

## ⚠️ 탑티어 저널 거부 사유 Top 5

Nature/Science 편집자들이 초록만 보고 desk-reject 하는 이유:

### 1. **Unclear novelty**
"What's actually new here?" → 기존 연구와 차별점 불명확

### 2. **Narrow scope**
"Why should broad readership care?" → 좁은 전문가만 관심

### 3. **Weak evidence**
"Results don't support the bold claims" → 주장과 증거 불일치

### 4. **Poor structure**
"Can't understand the story in one read" → 논리 흐름 끊김

### 5. **Overselling**
"Claims exceed what the data show" → 과장된 표현

**→ 오늘 Workshop에서 AI로 자가 검증!**

---

## 🎨 오늘의 Workshop (70분)

### 1. Abstract Autopsy Project (40분) ⭐ 핵심 활동
- **Expert Groups (15분)**: Nature/Science vs 일반 저널 초록 5쌍 분석
- **Home Groups (15분)**: 패턴 도출 및 공유
- **Class Synthesis (10분)**: "Class Top-Tier Abstract Checklist" 공동 작성

### 2. AI-Powered Writing Workshop (30분)
- **Round 1**: Opening 최적화 (10분)
- **Round 2**: Significance 확장 (10분)
- **Round 3**: AI Self-Critique (10분)

### 3. Recipe Sharing & Gallery Walk (10분)
- 최고의 프롬프트 공유 및 투표
- "Prompt Battle" - 가장 효과적이었던 레시피

---

## 📝 과제 (다음 주까지)

### Part A: Nature/Science급 초록 (250-300 words)
**필수 포함 요소:**
- ✅ "Class Top-Tier Abstract Checklist" 모든 항목 충족
- ✅ 4가지 Opening 패턴 중 하나 명확히 사용
- ✅ Broad significance framing
- ✅ 정량적 결과 제시
- ✅ Novelty 명시적 강조

### Part B: AI 활용 과정 문서 (500-700 words)
- 사용한 프롬프트 레시피 3개 이상
- AI 출력 평가 및 선택 과정
- AI 활용의 장단점 성찰

### Part C: Writing Circle 피드백 반영 (300-400 words)
- 받은 피드백 요약 및 반영
- 동료 학습 인사이트

---

## 💡 핵심 메시지

### 탑티어 초록의 공식

```
고임팩트 Opening (4가지 패턴 중 하나)
          +
Broad Significance (넓은 과학적/사회적 임팩트)
          +
정량적 Results (340% vs "significant")
          +
명시적 Novelty (first, unprecedented, novel mechanism)
          =
Nature/Science급 초록
```

---

## 🎯 AI의 역할

> **"AI는 다양한 버전을 빠르게 생성하는 도구.**
> **최종 판단과 선택은 인간의 비판적 사고."**

### 집단 지성의 힘

> **"Abstract Autopsy에서 우리가 함께 발견한**
> **'Class Top-Tier Abstract Checklist'는**
> **어떤 교과서보다 강력한 가이드입니다.**
> **왜냐하면 우리가 직접 발견했기 때문입니다."**

---

<!-- _class: lead -->

# 🚀 지금 바로 Workshop 시작!

**Abstract Autopsy Project로 이동 →**

---

## 📚 Appendix: AI 프롬프트 레시피 예시

### Recipe 1: Opening 4가지 패턴 생성

```
역할: 당신은 Nature/Science 편집 경험이 있는 과학 저널리스트입니다.

작업: 다음 연구 주제를 4가지 Opening 패턴으로 재작성해주세요.
[연구 주제 설명]

4가지 패턴:
1. Problem-driven: "Despite decades of research, [핵심 문제] remains unsolved..."
2. Gap-driven: "While [확립된 지식] is established, we lack understanding of [공백]..."
3. Opportunity-driven: "Recent advances in [기술] enable unprecedented investigation..."
4. Challenge-driven: "[현상] poses a fundamental challenge to our understanding..."

요구사항:
- 각 버전은 1-2문장
- Nature/Science 독자가 첫 문장에서 흥미를 느낄 수 있도록
- 전문용어는 최소화하되, 과학적 정확성 유지
```

---

### Recipe 2: Broad Significance 확장

```
역할: 당신은 Nature 편집자입니다.

현재 Significance 문장: [현재 문장]

이 문장이 "왜 Nature의 넓은 독자층이 관심을 가져야 하는가?"에
답하도록 재작성해주세요.

고려사항:
- Scientific impact (다른 분야 연구자들에게)
- Societal relevance (일반 대중 또는 정책 입안자들에게)
- Cross-disciplinary connections (어떤 분야와 연결되는가)

3가지 버전을 제시하되, 각각 다른 관점에서 접근해주세요.
```

---

### Recipe 3: AI Self-Critique

```
역할: 당신은 Nature 편집자입니다.

다음 초록 초안을 5가지 흔한 거부 사유로 평가해주세요:
[초록 초안]

5가지 평가 항목:
1. Unclear novelty: 무엇이 새로운지 불명확한가? (1-10점, 이유)
2. Narrow scope: 좁은 독자층만 관심 가질 내용인가? (1-10점, 이유)
3. Weak evidence: 주장이 증거를 초과하는가? (1-10점, 이유)
4. Poor structure: 논리적 흐름이 부족한가? (1-10점, 이유)
5. Overselling: 과장된 표현이 있는가? (1-10점, 이유)

각 항목에 대해:
- 점수 (1=매우 취약, 10=매우 강함)
- 구체적 문제점
- 개선 제안
```

---

<!-- _class: lead -->

# Thank you!

**Questions?**
