# Week 2: selected_papers.md 활용 가이드
## 90분 수업에서 언제, 어떻게 사용할 것인가

---

## 📋 전체 구조 (90분)

| 시간 | 활동 | selected_papers.md 사용 |
|------|------|-------------------------|
| **0-15분** | 강의 (Opening Patterns + Broad Significance) | ✅ **Pair B 초록 사용** (슬라이드에 임베드) |
| **15-35분** | Peer Feedback - Exemplar Calibration | ✅ **Pair A, C 초록 사용** (전체 초록 분석) |
| **35-60분** | Peer Feedback - 학생 초록 평가 Round 1 | ❌ (학생이 가져온 초록 사용) |
| **60-75분** | AI-Enhanced Revision | ❌ (학생 초록 + AI) |
| **75-85분** | Peer Feedback - Validation Round 2 | ❌ (학생 초록 revised) |
| **85-90분** | Wrap-up & Assignment | ✅ **Pair A, B, C 초록 링크 제공** (과제용 참고자료) |

---

## 🎯 Part 1: 강의 (0-15분) - Pair B 초록 사용

### 사용 초록: **Pair B - AI Persuasiveness & Human Behavior**

**파일 위치**: `selected_papers.md` Lines 70-131

**사용 이유**:
- ✅ **Problem-driven opening** 패턴의 가장 명확한 예시
- ✅ **Experimental psychology** (순수 행동 연구, No fMRI) - 학생들이 "탑티어 = neuroscience"라는 편견 깨기
- ✅ **최신 논문** (2025년) - 학생들이 ChatGPT/AI에 익숙하여 흥미 유발
- ✅ **Broad significance** 명확 (AI governance, online platforms, misinformation)
- ✅ **정량적 결과** 풍부 (N=900, 64.4%, 81.2% increase, 95% CI)

---

### 🎬 정확한 사용 시점

#### **Slide 13-14: Opening 차이 Before/After** (강의 5-7분 지점)

**현재 슬라이드 내용** (lesson_slides_15min.md Lines 91-136):
```markdown
### ❌ 일반 저널 Opening
Spatial memory in rodents has been extensively studied...
Previous work has shown that hippocampal neurons play a role...

### ✅ Nature Opening (Problem-Driven)
Despite decades of research, the molecular mechanisms linking
spatial navigation to memory consolidation remain unknown—
a fundamental gap limiting Alzheimer's intervention strategies.
```

**🔄 수정 제안 - Pair B 초록으로 교체**:

```markdown
## Opening 차이: Real Example from Nature Human Behaviour (2025)

### ❌ 일반 저널 Opening (가상 예시)
```
Large language models like GPT-4 are becoming increasingly popular.
Previous research has investigated AI persuasion capabilities.
This study examines whether AI can persuade humans effectively.
```

**문제**:
- 기술 트렌드 단순 소개
- 왜 중요한지 불명확
- Narrow audience (AI 연구자만)

### ✅ Nature Human Behaviour Opening (Salvi et al., 2025)
```
Early work has found that large language models (LLMs) can
generate persuasive content. However, evidence on whether they
can also personalize arguments to individual attributes remains
limited, despite being crucial for assessing misuse.
```

**강점**:
- **Problem-driven 패턴**: AI 오용 위험성이라는 문제 명시
- **"Despite being crucial"** → 왜 중요한지 즉시 명확
- **Broad impact**: AI governance, misinformation, platform design
- **No brain imaging**: 순수 행동 실험 (N=900)으로도 Nature급 가능!
```

**강의자 스크립트** (7분 지점):
> "이것은 실제 Nature Human Behaviour 2025년 논문입니다. 주목할 점:
> 1. **Problem-driven opening** - AI 개인화 설득의 위험성이라는 문제를 즉시 제시
> 2. **Broad significance** - AI 오용, 플랫폼 거버넌스, 허위정보 - 여러 분야에 영향
> 3. **No fMRI** - 순수 행동 실험 (N=900 debate task)만으로 Nature급 저널에 출판
> 4. 여러분이 ChatGPT 사용하죠? 바로 그 GPT-4를 연구한 논문입니다."

---

#### **Slide 18-19: 정량적 결과 표현** (강의 10-12분 지점)

**현재 슬라이드 내용** (lesson_slides_15min.md Lines 336-386):
```markdown
### ❌ 모호한 표현
"We found significant improvements in performance."

### ✅ 정량적 임팩트
"Performance improved by 340%, exceeding theoretical predictions by twofold."
```

**🔄 추가 - Pair B 초록 결과 삽입**:

```markdown
## 정량적 결과 표현: Real Example

### ❌ 모호한 표현
```
Our results showed that GPT-4 was more persuasive than humans.
The effect was statistically significant (p < 0.05).
```

### ✅ Nature Human Behaviour의 정량적 임팩트 (Salvi et al., 2025)
```
GPT-4 with personalization was more persuasive 64.4% of the time
(81.2% relative increase in odds of higher post-debate agreement;
95% confidence interval [+26.0%, +160.7%], P < 0.01; N = 900).
```

**차이점**:
- **64.4%** (구체적 승률)
- **81.2% relative increase** (효과 크기)
- **95% CI** (신뢰구간)
- **N = 900** (표본 크기)
- **P < 0.01** (통계적 유의성)

→ 독자가 결과의 크기와 신뢰도를 즉시 판단 가능
```

**강의자 스크립트** (12분 지점):
> "Nature 저널은 '유의미했다'가 아니라 '얼마나 강했는가'를 요구합니다.
> 이 논문은 5가지 정량적 지표를 한 문장에 집약했습니다.
> 여러분의 초록에도 이런 구체성이 필요합니다."

---

#### **Slide 20: Broad Significance 확장** (강의 12-14분 지점)

**현재 슬라이드 내용** (lesson_slides_15min.md Lines 280-333):
```markdown
### ❌ Narrow Examples
"We found improved memory in mice."

### ✅ Broad Examples
"Targeting this pathway could reverse age-related cognitive decline."
```

**🔄 추가 - Pair B의 Broad Significance 문장**:

```markdown
## Broad Significance: Real Example

### ❌ Narrow Significance (가상)
```
This study contributes to our understanding of AI persuasion
capabilities in controlled experimental settings.
```
→ AI 연구자만 관심

### ✅ Nature Human Behaviour의 Broad Significance (Salvi et al., 2025)
```
Our findings highlight the power of LLM-based persuasion and
have implications for the governance and design of online platforms.
```

**Broad Impact 포인트**:
1. **Governance** → 정책 입안자, 규제 기관
2. **Platform design** → 소셜 미디어, 테크 기업
3. **LLM-based persuasion power** → 마케팅, 정치, 교육, 허위정보 대응
4. Implicit: 민주주의, 정보 환경, 사용자 자율성

→ 심리학 + 컴퓨터과학 + 정책학 + 철학 + 커뮤니케이션학 독자 모두 관심
```

**강의자 스크립트** (14분 지점):
> "이 한 문장이 논문의 독자층을 AI 연구자에서 플랫폼 디자이너, 정책 입안자,
> 허위정보 연구자, 윤리학자까지 확장시킵니다. 이것이 Broad Significance입니다."

---

## 🎯 Part 2: Peer Feedback - Exemplar Calibration (15-35분)

### 사용 초록: **Pair A + Pair C**

**파일 위치**:
- Pair A: `selected_papers.md` Lines 15-69
- Pair C: `selected_papers.md` Lines 133-187

**사용 이유**:
- **Pair A (Gap-driven)**: Memory & Temporal Context - 명확한 gap 지적 ("However, limited evidence characterizes...")
- **Pair C (Opportunity-driven)**: Sleep & Memory Consolidation - 새로운 기술 활용 ("Here, we implemented real-time closed-loop deep brain stimulation")
- Pair B는 강의에서 이미 사용했으므로 제외
- 학생들이 3가지 opening pattern을 직접 비교 분석

---

### 🎬 정확한 사용 시점

#### **Minutes 15-17: Exemplar 제시 및 Silent Reading**

**강의자 행동**:
1. **(15:00-15:30)** 화면에 **Pair A** 투사
   - Nature Communications 초록 전문 (selected_papers.md Lines 29-30)
   - 컬러 코딩: Opening sentence 초록색, Significance 노란색, Results 파란색

2. **(15:30-16:00)** 학생들에게 지시:
   > "이 Nature Communications 초록을 읽으면서 다음을 표시하세요:
   > 1. Opening sentence - 어떤 패턴인가? (Problem/Gap/Opportunity/Challenge)
   > 2. Broad significance 문장 - 누구에게 중요한가?
   > 3. Quantitative results - 구체적 숫자가 있는가?"

3. **(16:00-17:00)** 개별 작업 시간 (학생들이 초록 분석)

**자료 준비**:
- **Pair A 초록 슬라이드**:
```markdown
## Pair A: Nature Communications 2023

> Converging, cross-species evidence indicates that memory for time
> is supported by hippocampal area CA1 and entorhinal cortex.
> **However, limited evidence characterizes how these regions preserve
> temporal memories over long timescales (e.g., months).** At long
> timescales, memoranda may be encountered in multiple temporal contexts,
> potentially creating interference. Here, using 7T fMRI, we measured
> CA1 and entorhinal activity patterns as human participants viewed
> thousands of natural scene images distributed, and repeated, across
> many months. We show that memory for an image's original temporal
> context was predicted by the degree to which CA1/entorhinal activity
> patterns from the first encounter with an image were re-expressed
> during re-encounters occurring minutes to months later...

**DOI**: 10.1038/s41467-023-40100-8
**Citations**: 45+ (as of 2024)
```

---

#### **Minutes 17-25: Whole-Class Discussion - Pattern Discovery**

**강의자 Socratic 질문**:

1. **(17:00-19:00)** Opening Pattern 분석:
   > Q: "첫 문장을 보세요. 어떤 패턴으로 시작하나요?"
   > A (유도): "Converging evidence indicates..." → 기존 연구 인정
   > Q: "그 다음은?"
   > A (유도): "**However, limited evidence**..." → **Gap-driven!**
   >
   > **확인**: "이것이 Gap-driven opening입니다. 기존 연구는 있지만,
   > '장기 기억 (months)'에 대한 증거가 부족하다는 gap을 명시했습니다."

2. **(19:00-21:00)** Broad Significance 분석:
   > Q: "'Long timescales' (months)가 왜 중요한가요?"
   > A (유도): "실험실 기억 연구는 주로 수 분~수 일. 실생활은 수개월~수 년"
   > Q: "Temporal context memory가 왜 중요한가요?"
   > A (유도): "Alzheimer's 환자들이 '언제' 기억했는지 혼란. 치료 전략 개발에 중요"
   >
   > **확인**: "이 논문은 기초과학 (hippocampus)을 실생활 (months) 및
   > 임상 응용 (Alzheimer's)으로 확장시켰습니다."

3. **(21:00-23:00)** Quantitative Results 분석:
   > Q: "구체적인 숫자나 측정값이 있나요?"
   > A (유도): "7T fMRI (고해상도), thousands of images, minutes to months"
   >
   > **확인**: "정확한 측정 도구와 시간 범위를 명시했습니다."

4. **(23:00-25:00)** Pair C 간략 소개 (Opportunity-driven 패턴):
   > "이제 다른 패턴을 봅시다. Pair C - Nature Neuroscience 2023"
   >
   > 화면에 Pair C opening 투사:
   > ```
   > Memory consolidation during sleep is thought to depend on...
   > but direct evidence is lacking. **Here, we implemented
   > real-time closed-loop deep brain stimulation**...
   > ```
   >
   > Q: "이 opening은 어떤 패턴인가요?"
   > A (유도): "Here, we implemented... → **Opportunity-driven!** 새로운 기술 활용"
   >
   > **확인**: "Gap은 있었지만 (direct evidence lacking), 이 논문은
   > '새로운 기술 (closed-loop stimulation)'으로 해결했다는 기회를 강조합니다."

**자료 준비**:
- **Pair C Opening 슬라이드**:
```markdown
## Pair C: Nature Neuroscience 2023 - Opportunity-Driven

> Memory consolidation during sleep is thought to depend on the
> coordinated interplay between cortical slow waves, thalamocortical
> sleep spindles and hippocampal ripples, **but direct evidence is
> lacking**. **Here, we implemented real-time closed-loop deep brain
> stimulation** in human prefrontal cortex during sleep and tested
> its effects on sleep electrophysiology and on overnight consolidation
> of declarative memory...

**Opening Pattern**: Opportunity-driven
- Gap exists ("direct evidence is lacking")
- **New technology enables solution** ("real-time closed-loop DBS")
- Emphasis on methodological innovation

**DOI**: 10.1038/s41593-023-01324-5
**Citations**: 90+ (highly cited)
```

---

#### **Minutes 25-35: Checklist Derivation**

**강의자 행동**:
1. **(25:00-28:00)** 화이트보드에 "Nature/Science Checklist" 공동 작성:

   > "우리가 발견한 것을 정리해봅시다. Nature/Science 초록의 5가지 핵심 요소:"
   >
   > **학생들과 함께 도출** (Socratic method):
   > 1. **Opening Pattern**: Problem/Gap/Opportunity/Challenge 중 하나 명확?
   > 2. **Broad Significance**: 좁은 전공 넘어 누구에게 중요한가?
   > 3. **Quantitative Results**: 구체적 숫자, %, effect size 있는가?
   > 4. **Explicit Novelty**: "First", "novel", "unprecedented" 명시?
   > 5. **Logical Structure**: 문제 → 방법 → 결과 → 의미 논리적 흐름?

2. **(28:00-30:00)** 5-Dimension Rubric 배포 및 설명:
   - 각 dimension 1-5 점수
   - 5 = Nature/Science ready
   - 1-2 = Desk reject
   - 학생들에게 인쇄본 또는 Notion page 링크 제공

3. **(30:00-35:00)** Editor Protocol 시연:
   > "이제 Nature 편집자처럼 평가해봅시다. 예시를 보겠습니다."
   >
   > **가상의 나쁜 초록 투사**:
   > ```
   > Stress affects college students. We studied 89 students.
   > WCST performance showed significant effects (p<0.05).
   > This contributes to the stress literature.
   > ```
   >
   > **Editor Protocol 시연**:
   > - **Desk Reject?** Yes
   > - **Fatal Flaw?** Narrow significance (only college mental health researchers care)
   > - **Strongest Element?** Logical structure (3/5)
   > - **Concrete Revision**:
   >   - Current: "This contributes to the stress literature."
   >   - Revision: "Understanding which cognitive processes are most vulnerable to stress is critical for designing effective interventions for 60% of college students experiencing chronic stress—this study reveals selective impairment in cognitive flexibility (not memory or speed), suggesting targeted training can reduce dropout risk."

**자료 준비**:
- 5-Dimension Rubric 인쇄본 (bilingual)
- Editor Protocol template (Notion 또는 인쇄본)
- 가상의 나쁜 초록 예시 슬라이드

**Transition to Round 1**:
> "이제 여러분의 초록을 평가할 차례입니다. 조별로 모여서
> Editor Protocol을 사용하여 서로의 초록을 평가해주세요.
> 기억하세요: Nature 편집자는 80%를 desk-reject 합니다.
> 엄격한 피드백이 친절한 피드백입니다."

---

## 🎯 Part 3: Wrap-up (85-90분) - 모든 Pair 참고자료 제공

### 사용 초록: **Pair A, B, C 모두**

**파일 위치**: `selected_papers.md` 전체 파일

---

### 🎬 정확한 사용 시점

#### **Minutes 85-88: 과제 안내**

**강의자 행동**:
> "다음 주까지 과제:
> 1. Nature/Science급 초록 작성 (250-300 words)
> 2. AI 활용 과정 문서 (500-700 words)
> 3. Peer feedback 반영 문서 (300-400 words)
>
> **참고자료로 오늘 분석한 3개 논문 초록을 Notion에 올려두었습니다:**

**Notion page에 추가할 내용**:

```markdown
## 📚 참고: 오늘 분석한 Nature/Science 초록 3개

### 1️⃣ Pair A: Memory & Temporal Context (Gap-driven)
**Journal**: Nature Communications 2023
**Link**: https://www.nature.com/articles/s41467-023-40100-8
**Opening Pattern**: Gap-driven ("However, limited evidence...")
**Why Study This**:
- Gap-driven opening 패턴의 모범 사례
- Long timescales (months) → Broad significance
- 7T fMRI + thousands of images → Quantitative rigor

### 2️⃣ Pair B: AI Persuasiveness (Problem-driven) ⭐ 강의에서 사용
**Journal**: Nature Human Behaviour 2025
**Link**: https://www.nature.com/articles/s41562-025-02194-6
**Opening Pattern**: Problem-driven ("...crucial for assessing misuse")
**Why Study This**:
- Problem-driven opening 패턴의 최신 사례
- AI governance, platform design → Extremely broad significance
- N=900, 64.4%, 81.2% increase, 95% CI → Quantitative mastery
- **Experimental psychology (No fMRI)** → 순수 행동 연구도 Nature급 가능

### 3️⃣ Pair C: Sleep & Memory Consolidation (Opportunity-driven)
**Journal**: Nature Neuroscience 2023
**Link**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10244181/
**Opening Pattern**: Opportunity-driven ("Here, we implemented...")
**Why Study This**:
- Opportunity-driven opening 패턴 (새로운 기술)
- Causal evidence (not just correlation) → Strong claim
- Real-time closed-loop DBS → Methodological innovation

---

## 💡 과제 작성 팁

각 논문을 읽으면서:
1. **Opening sentence 분석**: 어떤 패턴? 왜 효과적?
2. **Broad significance 찾기**: "implications for...", "fundamental to...", "critical for..." 문장
3. **정량적 결과 추출**: 모든 숫자를 노트에 적기 (%, n=, CI, p-value)
4. **AI에게 물어보기**: "이 Nature 초록의 opening을 내 연구에 적용하려면?"

여러분의 초록에 이 3가지 패턴 중 하나를 적용해보세요!
```

---

## 📊 Summary: selected_papers.md 사용 빈도

| Pair | Opening Pattern | 강의 (0-15분) | Exemplar (15-35분) | Wrap-up (85-90분) | 총 사용 시간 |
|------|----------------|---------------|-------------------|------------------|-------------|
| **Pair A** | Gap-driven | ❌ | ✅ **8분 집중 분석** | ✅ 참고자료 | ~8분 |
| **Pair B** | Problem-driven | ✅ **6분 집중 사용** | ❌ | ✅ 참고자료 | ~6분 |
| **Pair C** | Opportunity-driven | ❌ | ✅ **2분 패턴 소개** | ✅ 참고자료 | ~2분 |
| **Total** | | 6분 (Pair B) | 10분 (Pair A+C) | 참고자료 | ~16분 |

**전략적 배분 이유**:
- **Pair B (6분)**: 강의에서 Problem-driven 패턴 + Broad significance + Quantitative results 3가지 모두 시연
- **Pair A (8분)**: Exemplar에서 Gap-driven 패턴 깊이 있는 분석, 학생들이 직접 발견하도록 유도
- **Pair C (2분)**: Opportunity-driven 패턴 간략 소개, 시간 절약하면서 3가지 패턴 모두 커버

---

## ✅ 강의자 체크리스트

### 수업 2일 전:
- [ ] `selected_papers.md`에서 3개 초록 복사
- [ ] Pair B 초록 → lesson_slides_15min.md Slide 13-14, 18-19에 삽입
- [ ] Pair A, C 초록 → 별도 슬라이드 제작 (컬러 코딩: opening 초록, significance 노랑, results 파랑)
- [ ] Notion Week 2 page에 "참고: 오늘 분석한 Nature/Science 초록 3개" 섹션 추가

### 수업 당일:
- [ ] Pair A 초록 인쇄본 각 조에 배포 (15분 시점)
- [ ] Pair C opening 슬라이드 준비 (23분 시점)
- [ ] 가상의 나쁜 초록 예시 슬라이드 (Editor Protocol 시연용, 30분 시점)
- [ ] Notion 참고자료 링크 학생들에게 공유 (85분 시점)

### 수업 후:
- [ ] 학생 피드백 수집: "오늘 분석한 3개 초록 중 가장 도움된 것은?"
- [ ] 다음 주 수업 조정: 학생들이 어떤 opening pattern을 선택했는지 파악

---

**Last Updated**: 2025-01-02
**Purpose**: 강의자가 정확히 언제, 어떤 초록을 사용할지 알 수 있도록 minute-by-minute 가이드 제공
