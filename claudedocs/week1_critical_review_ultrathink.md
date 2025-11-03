# Week 1 수업 자료 비판적 검토 (Ultrathink Analysis)

**분석 날짜**: 2025-10-28
**분석 방법**: Sequential Thinking (18-step deep analysis)
**전체 평가**: 85/100점

---

## 📊 Executive Summary

Week 1 자료는 **전반적으로 우수한 설계**이나, **시간 관리와 인지 부하**에서 현실성이 부족합니다.

**핵심 강점**:
- ✅ 실제 PLOS ONE 2019 논문 사용 (매우 가치 있음)
- ✅ 체계적 구조 (3 Lessons, 3-stage Workshop)
- ✅ 실습 중심 (56% 시간 배분)
- ✅ 혁신적 Figma 협업

**핵심 약점**:
- ❌ 10개 원칙을 35분에 - 인지 부하 과다
- ❌ 8분에 10문장 수정 - 비현실적 시간
- ❌ 생물학/컴퓨터 예제 - 심리학과 무관
- ❌ 주관적 평가 기준
- ❌ 파일 간 정보 불일치

**예상 결과**:
- 수정 없이 진행: 60-70%만 목표 달성 (시간 부족, 학생 혼란)
- Critical 3개 수정 후: 85-95% 목표 달성 가능

---

## 🔴 CRITICAL 이슈 (즉시 수정 필요)

### 1. 시간 배분 비현실성 ⚠️ 수업 실패 위험

**문제:**
```
현재 설계: Stage 1A (Bad Sentences)
- 개인 수정: 5분에 10개 문장
- 실제 소요: 문장당 3.5분 필요 = 35분

현재 설계: Stage 2 (Smart Revising)
- 7단계 체크리스트 적용: 10분
- 수정본 작성: 2분
- 실제 소요: 최소 20분 필요
```

**영향**:
- 학생들이 시간 내 완료 못 함 → 좌절감
- 교수자가 계속 재촉 → 학습 효과 감소
- Workshop 중간에 진도 조정 필요 → 혼란

**해결책 (Option A - 권장):**
```markdown
Stage 1A 수정:
- Bad Sentences: 10개 → 5개로 축소
- 개인 수정: 5분 → 10분
- 5개 선택 기준: Nominalization, 주어-동사 거리, Old→New, 간결성, 복합

Stage 2 수정:
- 명확히: "발견"에 집중 (수업 중)
- 실제 "수정"은 과제로 (수업 후)
```

**해결책 (Option B):**
```markdown
전체 시간 재배분:
- IMRaD 오리엔테이션: 5분 → 2분 (-3분)
- Lesson 1-3 강의: 30분 → 25분 (-5분)
- Workshop: 50분 → 58분 (+8분)
```

**작업 시간**: 30분
**우선순위**: P0 (최우선)

---

### 2. 학습 목표 불일치 🎯

**문제:**
```
lesson_notes_compressed_90min.md (강의 자료):
"독자 중심 글쓰기의 3가지 핵심 원칙 습득"

teaching_guide_90min.md (교수 가이드):
"독자 중심 글쓰기의 10가지 핵심 원칙 습득"

실제 내용:
- Lesson 1: 3원칙
- Lesson 2: 3원칙
- Lesson 3: 4원칙
= 총 10개
```

**영향**:
- 학생 혼란: "3개를 배우나요, 10개를 배우나요?"
- 평가 기준 모호: "3가지 원칙 습득"을 어떻게 평가?
- 과제 연결 불명확: 7단계 체크리스트와의 관계?

**해결책:**
```markdown
모든 문서에서 통일:

"독자 중심 글쓰기의 10가지 핵심 원칙 습득 (3개 영역)"

- Lesson 1 (주어-동사): 3원칙
- Lesson 2 (응집성): 3원칙
- Lesson 3 (간결성): 4원칙

또는 더 명확히:

"3가지 핵심 영역의 글쓰기 원칙 습득"
```

**수정 파일**:
- `lesson_notes_compressed_90min.md` (line 3-5)
- `teaching_guide_90min.md` (line 9)

**작업 시간**: 10분
**우선순위**: P0

---

### 3. 과제 명세 불명확 📝

**문제:**
```
assignment.md:
"개인 연구주제 설정 및 개요 작성"

teaching_guide_90min.md (85-90분):
"과제: 자신의 논문 초록 또는 서론 첫 문단을
      Smart Revising 7단계로 수정"

teaching_guide_90min.md (다음 주 안내):
"필수 준비물: 초록 baseline draft (150-200 words)"
```

**영향**:
- 학생들이 뭘 해야 하는지 모름
- 과제가 1개? 2개? 3개?
- Week 2 준비 못 함

**해결책:**
```markdown
assignment.md를 확인하고 명확히:

Week 1 과제:
1. 자신의 연구 초록 작성 (150-200 words) - 완벽하지 않아도 됨
2. Smart Revising 7단계 체크리스트 적용
3. 수정 전/후 버전 + 체크리스트 기록 제출

Week 2 준비:
- Week 1 과제로 만든 초록 baseline draft 가져오기
- AI로 개선할 예정
```

**수정 파일**:
- `assignment.md` 전체 확인 및 재작성
- `teaching_guide_90min.md` (line 600-650) 과제 안내 통일

**작업 시간**: 30분
**우선순위**: P0

---

## 🟡 IMPORTANT 이슈 (수업 품질 향상)

### 4. 예제의 학습자 관련성 부족 🧪

**문제:**
```
Bad Sentence #1: "The ABC database has been subject to..."
→ Database/Computer Science

Bad Sentence #2: "Using sarkosyl to induce nuclear run-on..."
→ Molecular Biology

Bad Sentence #9: "C-terminal tandem affinity purification (TAP)-tagged proteins..."
→ Biochemistry

대상 학습자: 심리학과 대학원생
```

**영향**:
- 학생 반응: "이건 우리 논문에 안 나오는데요?"
- 관련성 저하 → 동기 감소
- Transfer learning 어려움

**긍정적 예외:**
```
Bad Paragraphs (Stage 1B):
- PLOS ONE 2019 social psychology 논문 ✅
- Self-control, prosocial behavior, life satisfaction ✅
- 학생들이 익숙한 주제 ✅
```

**해결책:**
```markdown
Bad Sentences를 심리학 논문에서 선정:

제안 출처:
1. Journal of Personality and Social Psychology
2. Psychological Science
3. PLOS ONE (Psychology section)
4. Frontiers in Psychology

선정 기준:
- 각 원칙당 1개 문장
- 심리학 전공용어 포함
- 학생들이 쓸 법한 문장

예시 (임시):
#1 (Nominalization): "The investigation of cognitive biases was conducted..."
#2 (주어-동사): "Working memory capacity, which has been shown to predict..."
#3 (Old→New): "Anxiety disorders affect millions. Treatment options have..."
```

**작업 시간**: 2-3시간 (논문 검색 + 선정)
**우선순위**: P1
**대안**: Stage 1A는 유지하고, Stage 1B (심리학 논문)에 더 시간 할애

---

### 5. 평가 기준 주관성 📊

**문제:**
```
현재 Rubric (assignment.md):

Excellent (90-100점):
- "성실히 적용" ← 정량 기준?
- "적절하고 효과적" ← 누가 판단?
- "명확" ← 측정 방법?

Good (80-89점):
- "대부분 적용" ← 7개 중 몇 개?
- "미흡" ← 어느 정도?
```

**영향**:
- Inter-rater reliability 낮음 (채점자마다 다른 점수)
- 학생 불만 가능성
- 채점 시간 증가 (주관적 판단)

**해결책: Analytic Rubric**

```markdown
## 평가 기준 (총 100점)

### 1. 7단계 체크리스트 완성도 (40점)
- 7단계 모두 기록: 40점
- 6단계 기록: 35점
- 5단계 기록: 30점
- 4단계 이하: 20점

### 2. 문제 발견의 정확성 (30점)
- Nominalization 3개 이상 발견: 10점
- 주어-동사 문제 2개 이상 발견: 10점
- Old→New 흐름 문제 1개 이상 발견: 10점

### 3. 수정의 적절성 (20점)
- 발견한 문제 80% 이상 적절히 수정: 20점
- 60-79% 수정: 15점
- 40-59% 수정: 10점

### 4. 최종 품질 (10점)
- 수정 후 글이 10가지 원칙에 대부분 부합: 10점
- 일부 부합: 7점
- 여전히 많은 문제: 4점
```

**추가: 샘플 과제 제공**
- Excellent 예시 1개
- Good 예시 1개
- Needs Improvement 예시 1개

**작업 시간**: 2시간
**우선순위**: P1

---

### 6. "Why No AI?" 설명 부재 🤖

**문제:**
- Week 1만 AI 사용 금지
- 하지만 이유 설명 없음
- 2025년 AI 시대에 학생들이 의문 가질 수 있음

**학생 예상 질문:**
- "왜 AI를 안 쓰나요?"
- "다른 과목에서는 ChatGPT 쓰는데..."
- "비효율적이지 않나요?"

**해결책:**

```markdown
## 새 슬라이드 추가 (오리엔테이션 후, 3분)

### Slide 4: Why "No AI" in Week 1?

**3가지 이유:**

1. **평가 기준 확립**
   - 먼저 "좋은 글쓰기"가 무엇인지 알아야 함
   - 이 기준으로 Week 2-6에서 AI 결과 평가

2. **독립적 판단 능력**
   - AI 의존 없이 스스로 문제 발견
   - 비판적 사고력 개발

3. **AI 도구 사용법의 기초**
   - AI에게 "더 나은" 결과를 요구하려면
   - 무엇이 "더 나은지" 알아야 함

**Week 2부터:** AI를 적극 활용!
- 하지만 Week 1 원칙으로 평가하고 개선
```

**작업 시간**: 30분
**우선순위**: P1

---

## 🟢 RECOMMENDED 이슈 (장기 개선)

### 7. 인지 부하 과다 (Cognitive Load Theory)

**분석:**
- 10개 원칙 × 5단계 학습 과정 = 50 cognitive steps
- 35분 강의 + 50분 실습 = 85분에 50 steps?
- Working memory 한계: 7±2 chunks

**문제:**
- Intrinsic Load 높음 (10개 원칙)
- Extraneous Load 높음 (Figma 학습, IMRaD 표)
- Germane Load 부족 (실제 학습 시간 부족)

**장기 해결책 (Week 2 이후 재설계):**

```markdown
Week 1 재구성:
- 6개 핵심 원칙만 (Lesson 1-2)
  1-3. 주어-동사 3원칙
  4-6. 응집성 3원칙

- 4개 심화 원칙은 Week 2-6에 분산
  7-8. 간결성 (Week 2: Abstract)
  9-10. 수식어 절제 (Week 5: Discussion)
```

**작업 시간**: 전체 코스 재설계 필요
**우선순위**: P2 (다음 학기)

---

### 8. Contrastive Rhetoric 부재

**문제:**
- 한국 학생들의 전형적 오류 (수동태 과다, 명사화, hedging)
- **왜** 이런 오류가 발생하는지 설명 없음
- 한국어-영어 학술 문화 차이 미언급

**해결책:**

```markdown
각 원칙마다 "한국 학생들이 주의할 점" 추가:

예시 - Lesson 1-1 (Nominalization):

한국어 학술 문체:
"본 연구는 데이터의 분석을 실시하였다"
→ 명사형 선호

영어 학술 문체:
"We analyzed the data"
→ 동사 선호

왜? 영어는 동사 중심 언어, 명확성이 객관성보다 우선
```

**작업 시간**: 각 원칙당 10분 × 10개 = 1.5시간
**우선순위**: P2

---

### 9. Figma 리스크 관리

**문제:**
- 학생들이 Figma 처음 사용
- 기술적 실패 시 백업 플랜 없음
- 네트워크 문제, 성능 저하 가능성

**백업 플랜:**

```markdown
Plan B: Google Docs Template 준비

구조:
1. 문서 1: Bad Sentences
   - 10개 문장 (또는 5개)
   - 각 문장 아래에 댓글 영역
   - 학생별 섹션

2. 문서 2: Smart Revising
   - 학생별 페이지
   - 7단계 체크리스트 템플릿

장점:
- 학생들이 익숙함
- 실시간 협업 가능
- 댓글 기능 있음

단점:
- 시각적 효과 부족
- 구조화 어려움
```

**작업 시간**: 1시간
**우선순위**: P2

---

### 10. 파일 구조 재정리

**문제:**
- 9개 파일이 평면적 구조
- 정보 중복 (Figma 설명 3곳)
- Master 파일 불명확

**제안 구조:**

```
week1/
├── README.md (시작점, 전체 가이드)
│
├── core/
│   ├── learning_objectives.md
│   ├── lesson_plan.md (시간 배분)
│   └── slides.md (강의 슬라이드)
│
├── workshop/
│   ├── stage1a_bad_sentences.md
│   ├── stage1b_bad_paragraphs.md
│   └── stage2_smart_revising.md
│
├── assessment/
│   ├── assignment.md
│   ├── rubric.md
│   └── sample_submissions.md
│
├── technical/
│   └── figma_setup.md
│
└── archive/
    ├── lecture_notes.md (legacy)
    └── practice.md (legacy)
```

**작업 시간**: 3-4시간
**우선순위**: P3 (다음 학기)

---

## ✅ Quick Wins (30분 내 즉시 실행)

### 1. 학습 목표 통일 (5분)
```bash
# lesson_notes_compressed_90min.md line 3-5
- "독자 중심 글쓰기의 3가지 핵심 원칙 습득"
+ "독자 중심 글쓰기의 10가지 핵심 원칙 습득 (3개 영역)"
```

### 2. Bad Sentences 선택 옵션 추가 (5분)
```markdown
workshop_materials.md에 추가:

"10개 문장이 제공됩니다. 시간 제약상 **5개를 선택**해서 작업하세요.
권장: #1 (Nominalization), #3 (주어-동사), #5 (Old→New), #8 (간결성), #10 (복합)"
```

### 3. Stage 2 목적 명확화 (5분)
```markdown
workshop_materials.md Stage 2 설명:

"Stage 2 목표: 문제 **발견**에 집중
- 7단계에서 발견한 문제를 Sticky Note로 기록
- 실제 **수정**은 과제에서 진행
- 수업 중에는 '어떻게 수정할지' 계획만"
```

### 4. IMRaD 표 삭제 (5분)
```markdown
lesson_notes_compressed_90min.md

Slide 3 삭제:
"Week 1의 역할" 표 → 너무 추상적, 지금 필요 없음

대신 간단히:
"오늘 배울 원칙들은 Introduction부터 Discussion까지 모든 섹션의 기초입니다"
```

### 5. 시간 안내 강화 (10분)
```markdown
teaching_guide_90min.md 각 섹션에:

[40-55분] Stage 1A: Bad Sentences (15분) ⏰ STRICT TIMING
  → 교수자: 타이머 설정, 5분 남았을 때 알림
  → "완성 못 해도 괜찮습니다. 다음 단계로 넘어갑니다"
```

---

## 📈 예상 효과

### 현재 (수정 전)
- 시간 부족으로 Workshop 불완전 완료: **60%**
- 학생 학습 목표 달성: **70%**
- 학생 만족도: **75%**
- 교수자 스트레스: **높음** (시간 관리 실패)

### Critical 3개 수정 후
- Workshop 완료율: **85%**
- 학습 목표 달성: **85%**
- 학생 만족도: **85%**
- 교수자 스트레스: **중간** (명확한 가이드)

### Important 3개 추가 수정 후
- Workshop 완료율: **90%**
- 학습 목표 달성: **90%**
- 학생 만족도: **90%**
- 교수자 스트레스: **낮음** (모든 준비 완료)

---

## 🎯 Action Plan

### Phase 1: 수업 전 필수 (2-3시간)
- [ ] **P0-1**: Bad Sentences 개수 조정 (30분)
- [ ] **P0-2**: 학습 목표 통일 (10분)
- [ ] **P0-3**: 과제 명세 확인 및 통일 (30분)
- [ ] **Quick Wins**: 5개 항목 (30분)
- [ ] **P1-5**: Analytic rubric 초안 (1시간)

**합계**: ~3시간

### Phase 2: 수업 후 개선 (다음 주)
- [ ] **P1-4**: 심리학 예제 선정 (3시간)
- [ ] **P1-6**: "Why No AI?" 슬라이드 (30분)
- [ ] **P2-9**: Figma 백업 플랜 (1시간)

### Phase 3: 장기 개선 (다음 학기)
- [ ] **P2-7**: 원칙 수 축소 (전체 재설계)
- [ ] **P2-8**: Contrastive Rhetoric 추가 (1.5시간)
- [ ] **P3-10**: 파일 구조 재정리 (4시간)

---

## 📝 최종 권고사항

### 수업 진행한다면 (현재 자료로)
1. **반드시** Bad Sentences 5개 선택 안내
2. **반드시** Stage 2 목적 명확히 (발견 vs 수정)
3. **시간 엄수** 포기하고 유연하게 운영
4. 학생들에게 "완벽 불필요" 강조

### 수정 시간이 있다면 (2-3시간)
1. Phase 1 Action Plan 전부 실행
2. 특히 과제 명세 확인 (학생 혼란 방지)
3. Analytic rubric 준비 (채점 시간 절약)

### 이상적으로 (1주일 여유)
1. Phase 1 + Phase 2 모두 실행
2. 심리학 예제로 교체
3. Figma 템플릿 실제 제작 및 테스트
4. 모의 수업 진행 (시간 측정)

---

## 🌟 강점 재확인

비판적 검토이지만, Week 1 자료의 강점을 재확인:

✅ **실제 논문 사용**: PLOS ONE 2019 - 교육적으로 매우 가치 있음
✅ **구조적 명확성**: 3 Lessons + 3 Stages - 이해하기 쉬움
✅ **실습 중심**: 56% 시간 - 올바른 방향
✅ **혁신적 시도**: Figma 협업 - 차별화 포인트
✅ **체계적 접근**: 10가지 원칙 + 7단계 체크리스트 - 재현 가능

**이 강점들을 유지하면서 시간 관리와 명확성만 개선하면 훌륭한 수업이 될 것입니다.**

---

**분석 완료일**: 2025-10-28
**다음 검토 예정**: 첫 수업 후 학생 피드백 수집 및 재분석
