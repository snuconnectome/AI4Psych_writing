# 다중 에이전트 학술 논문 작성 시스템 개요

**개발자**: 신정연 (Jeongyeon Shin)
**소속**: 서울대학교 심리학과
**수업**: 심리과학 연구방법 - 롸이팅 (AI4Psych Writing Course)
**날짜**: 2025년 11월

---

## 🎯 내가 실제로 만든 것

Introduction 섹션 개선을 위해 **4개의 전문 에이전트**가 협업하는 AI 시스템. 심리학 연구 논문 작성에 특화되어 있습니다.

**중요**: 이 문서는 **실제로 내 Introduction 수정에 사용한 내용**을 설명합니다. 시스템의 모든 기능이 아닙니다.

---

## 🤖 사용한 에이전트 (Gap Discovery Workflow)

### Workflow: gap_discovery

```
┌─────────────────────────────────────────┐
│  입력: Introduction 초안 (LaTeX)         │
└──────────────┬──────────────────────────┘
               │
    ┌──────────▼──────────┐
    │ 02. Literature      │
    │     Validator       │
    │ (연구 gap 검증)     │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 04. Logic Auditor   │
    │ (논리 구조 검토)    │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 01. Writer Agent    │
    │ (텍스트 수정)       │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 06. Coordinator     │
    │ (피드백 통합)       │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │ 출력: 수정된        │
    │ Introduction +      │
    │ 상세 피드백         │
    └─────────────────────┘
```

**사용 안 함**: LaTeX Converter (00), Quality Checker (03), Statistics Reviewer (05)

---

## 📚 학습 자료

모든 에이전트는 다음의 학술 논문 작성 원칙을 학습했습니다:

### 1. **Joseph M. Williams - "Style: Lessons in Clarity and Grace"**

**적용된 핵심 원칙**:

**동사로 행동 표현 (Actions in Verbs)**:
- ❌ "ELS와 인지 기능 간 관계에 대한 검토가 연구자들에 의해 수행되었다"
- ✅ "연구자들은 ELS가 인지 기능과 어떻게 관련되는지 검토했다"

**주어 위치에 중요한 개념 (Subjects as Subjects)**:
- ❌ "Threat가 정서 처리에 영향을 미친다고 연구자들에 의해 믿어진다"
- ✅ "연구자들은 threat가 정서 처리에 영향을 미친다고 믿는다"

**구정보→신정보 흐름 (Old→New Information Flow)**:
- 문장을 친숙한 정보로 시작
- 새로운 정보는 문장 끝에 배치
- 자연스러운 읽기 흐름 생성

**간결성 (Conciseness)**:
- 불필요한 메타담론 제거 ("주목할 점은..." 등)
- 불필요한 수식어 삭제
- 주어와 동사를 가깝게 유지

---

### 2. **Mensh & Kording - "Ten Simple Rules for Structuring Papers" (PLOS Comp Bio, 2017)**

**적용된 핵심 규칙**:

| 규칙 | 설명 | 내 Introduction에 적용된 방식 |
|------|------|------------------------------|
| **규칙 1** | 하나의 핵심 기여에 집중 | 모든 단락이 주요 연구 gap을 지지하도록 구성 |
| **규칙 3** | Context-Content-Conclusion (CCC) 구조 | 단락 수준에서 적용 - 각 단락이 명확한 목적 가짐 |
| **규칙 4** | 논리적 흐름 최적화 (지그재그 금지) | 문헌 검토 섹션을 재구성하여 주제 간 왔다갔다 방지 |
| **규칙 6** | Introduction은 '왜 중요한가'를 설명 | 명시적 significance statement 추가 (왜 gap이 중요한지 설명) |

**원문**: https://doi.org/10.1371/journal.pcbi.1004205

---

## 🔍 에이전트 상세 설명 (실제로 한 일)

### **에이전트 02: Literature Validator**

**내 intro에서 한 일**:
1. ✅ Gap 주장이 정확한지 검증
   - "ABCD 데이터에서 task-based fMRI와 dimensional approach를 함께 사용한 연구 없음"
   - 최근 문헌 확인 (Beck 2024, Jeong 2024 등)

2. ✅ Gap이 너무 모호하다고 지적
   - 원래: "findings remain inconsistent" (결과가 일관되지 않다)
   - 문제점: 무엇이 일관되지 않고 왜 중요한지 설명 안 함

3. ✅ Gap을 더 구체적으로 만들라고 제안
   - "neural mechanisms remain unclear, limiting understanding of specific pathways"라고 명시해야 함

**피드백 예시**:
```
문제: 12번째 줄의 gap statement가 모호함 - "findings are inconsistent"

권장사항: 무엇이 일관되지 않고 왜 중요한지 명시:
"이러한 서로 다른 효과의 신경학적 기반은 여전히 불명확하며,
구체적으로 threat와 deprivation이 뇌 기능을 어떻게 차별적으로
조절하는지에 대한 일관되지 않은 결과가 제시되고 있어, 각 차원이
신경인지 발달에 영향을 미치는 특정 신경 경로에 대한 우리의
이해를 제한하고 있다."
```

---

### **에이전트 04: Logic Auditor**

**내 intro에서 한 일**:
1. ✅ 논증 흐름 점검
   - 문제 → 증거 → 한계점 → Gap → 우리 접근법

2. ✅ "지그재그" 구성 발견
   - 보상 처리 → 정서 처리 → 다시 보상 처리로 왔다갔다
   - 주제 연속성을 유지하도록 재구성 제안

3. ✅ 누락된 연결 고리 발견
   - Gap은 언급했지만 significance 설명 안 함
   - "이것이 중요한 이유는..." 추가 제안

**피드백 예시**:
```
논리적 흐름: 4/5

문제: 5번째 단락이 정서 처리 논의 후 보상 처리로 돌아감 (지그재그 발견)

권장사항:
1. 보상 처리 논의를 정서 처리 이전에 모두 완료
2. 전환 문구 추가: "보상에 대한 X를 확립한 후, 이제 정서로 넘어간다..."

GAP 명시: 3/5
현재: "이 연구들은 threat와 deprivation을 구분하지 않았다"
누락: 왜 이것이 중요한가? 이 gap 때문에 우리가 무엇을 못 하는가?

권장사항: gap 언급 후 significance statement 추가
```

---

### **에이전트 01: Writer**

**내 intro에서 한 일**:
1. ✅ Williams 원칙을 문장별로 적용
   - 명사화를 동사로 변환
   - 주어-동사 정렬 수정
   - 구정보→신정보 흐름 개선

2. ✅ 단락 구조 개선
   - 누락된 topic sentence 추가
   - 단락 간 전환 강화

3. ✅ 명확성 향상
   - 긴 문장 분리 (>40 단어)
   - 복잡한 구조 단순화
   - 전문 용어 첫 사용 시 정의

**수정 예시**:
```
수정 전 (15번째 줄, 47 단어):
"However, the existing literature presents findings that are inconsistent
regarding the question of how threat and deprivation, as distinct dimensions
of early life stress, differentially modulate patterns of brain function,
thus limiting our understanding of the specific neural pathways through
which each dimension impacts neurocognitive development."

수정 후 (두 문장, 23 + 19 단어):
"However, the neural underpinnings of these distinct effects remain unclear.
Specifically, the existing literature presents inconsistent findings regarding
how threat and deprivation differentially modulate brain function, limiting
our understanding of the specific neural pathways through which each dimension
impacts neurocognitive development."

개선점:
- 두 문장으로 분리 (가독성 향상)
- 더 명확한 topic sentence ("neural underpinnings remain unclear")
- 모든 원래 정보 유지
```

---

### **에이전트 06: Coordinator**

**내 intro에서 한 일**:
1. ✅ 3개 에이전트로부터 피드백 수집
   - Literature Validator: "Gap이 너무 모호함"
   - Logic Auditor: "Significance statement 누락"
   - Writer: "긴 문장, 약한 전환"

2. ✅ 우선순위 할당
   - **Priority 1 (Critical)**: 없음 (치명적 결함 없음)
   - **Priority 2 (High)**: 모호한 gap statement, significance 누락
   - **Priority 3 (Medium)**: 단락 구성, 전환
   - **Priority 4 (Low)**: 문장 길이, 단어 선택

3. ✅ 통합 수정본 생성
   - Priority 2 피드백 먼저 반영
   - 가능한 곳에 Priority 3 개선 적용
   - 각 편집을 설명하는 변경 로그 제공

**출력 예시 구조**:
```json
{
  "executive_summary": {
    "overall_assessment": "명확한 연구 질문을 가진 탄탄한 기반이지만
                          gap 명시와 significance statement 개선 필요",
    "overall_score": "7.5/10",
    "top_3_issues": [
      "Gap statement가 모호함 - 신경 메커니즘 명시 필요",
      "Significance statement 누락 - 왜 gap이 중요한지 설명 필요",
      "문헌 검토가 지그재그 구성"
    ]
  },
  "integrated_feedback": {
    "priority_2_high": [
      "신경 메커니즘에 대한 구체적 gap statement 추가 (Lit Validator + Logic Auditor)",
      "이 연구가 왜 중요한지 설명하는 significance statement 추가 (Logic Auditor)"
    ],
    "priority_3_medium": [
      "지그재그 방지를 위해 보상/정서 섹션 재구성 (Logic Auditor)",
      "단락 간 전환 개선 (Writer)"
    ]
  },
  "integrated_revision": {
    "revised_text": "[Priority 2 변경사항이 적용된 전체 수정본]",
    "change_log": [
      "12번째 줄: 'findings are inconsistent'를 'neural underpinnings remain unclear'로 변경",
      "15번째 줄: Significance statement 추가 (89 단어)",
      "23번째 줄: 단락 순서 재구성 (보상 → 정서, 혼합 안 함)"
    ]
  }
}
```

---

## 📊 실제 결과 (내 Introduction)

### 입력
- **파일**: 1-intro-en.tex (LaTeX 형식)
- **길이**: 950 단어 (테이블 이전 텍스트)
- **날짜**: 2025년 11월 4일
- **처리 시간**: 45분

### 출력
- **수정된 텍스트**: 3,012 단어
- **상세 피드백**: 25KB JSON 파일
- **변경 사항**: 모든 단락에 걸쳐 ~50개 편집

### 품질 개선

| 항목 | 수정 전 | 수정 후 | 변화 |
|------|---------|---------|------|
| **Gap 명확성** | 3/5 (모호한 "일관되지 않음") | 5/5 (구체적 메커니즘) | +67% |
| **Significance Statement** | 2/5 (누락) | 5/5 (명시적 89단어 statement) | +150% |
| **논리적 흐름** | 3/5 (일부 지그재그) | 4.5/5 (재구성됨) | +50% |
| **문장 명확성** | 3/5 (일부 >40 단어) | 4.5/5 (대부분 <25 단어) | +50% |
| **전체 품질** | 2.8/5 | 4.6/5 | **+64%** |

---

## 💡 가장 영향력 있었던 변경사항

### 1. **Significance Statement 추가** (89 단어)

**추가된 내용**:
> "이 연구는 ELS의 서로 다른 차원이 신경인지 발달에 영향을 미치는
> 특정 신경 메커니즘에 대한 새로운 통찰을 제공할 것이기 때문에
> 중요하다. Task-based fMRI를 사용함으로써, 우리는 threat와
> deprivation의 구별되는 신경 상관물을 식별하여, 누적적 또는
> 데이터 주도 접근법보다 더 미묘한 이해를 제공하고자 한다.
> 구체적으로, 우리는 보상, 정서, 작업 기억, 충동성 회로를 활성화하는
> 것으로 알려진 신중하게 선택된 과제를 사용하여 ABCD 연구의 데이터를
> 분석할 것이다."

**왜 중요했는가**:
- 우리가 **무엇**을 하는지뿐만 아니라 **왜** 중요한지 명확히 함
- 더 넓은 목표와 연결 (표적 개입, 메커니즘 이해)
- 기존 ABCD 연구들과 우리 접근법 차별화

---

### 2. **Research Gap 명확화**

**수정 전**:
> "그러나 뇌 기능에 대한 결과는 일관되지 않는다."

**수정 후**:
> "그러나 이러한 서로 다른 효과의 신경학적 기반은 여전히 불명확하다.
> 구체적으로, 기존 문헌은 threat와 deprivation이 뇌 기능을 어떻게
> 차별적으로 조절하는지에 대해 일관되지 않은 결과를 제시하고 있어,
> 각 차원이 신경인지 발달에 영향을 미치는 특정 신경 경로에 대한
> 우리의 이해를 제한하고 있다."

**왜 중요했는가**:
- 모호한 "일관되지 않음"에서 구체적인 "신경 메커니즘 불명확"으로 변경
- 결과 설명: "경로에 대한 이해 제한"
- 우리 연구의 명확한 동기 설정

---

### 3. **논리적 흐름 개선**

**발견된 문제**:
- 문헌 검토가 주제 간 왔다갔다함 (보상 → 정서 → 보상 → 정서)

**적용된 해결책**:
- 재구성: 보상 (전체) → 정서 (전체) → 작업 기억 (전체) → 충동성 (전체)
- 전환 추가: "X를 확립한 후, 이제 Y로 넘어간다"

**왜 중요했는가**:
- 독자가 따라가기 쉬움
- 다음 주제로 넘어가기 전에 각 구성 개념을 포괄적으로 논의
- 정서 섹션 읽을 때 이전 보상 논의를 "기억"할 필요 없음

---

## 🤖 기술 세부사항

### 사용한 시스템
- **제공자**: Google Gemini (무료)
- **모델**: gemini-2.0-flash-exp
- **프로그래밍**: Python 3.8+
- **총 API 호출**: ~15개 요청 (Literature Validator → Logic Auditor → Writer → Coordinator, 여러 단락)

### 왜 이 Workflow인가?
**gap_discovery**는 Introduction 섹션을 위해 특별히 설계되었기 때문:
1. Literature Validator가 gap 주장의 정확성 보장
2. Logic Auditor가 논증 구조 점검 (문제 → 증거 → gap → 우리 접근법)
3. Writer가 문장 수준 개선 적용
4. Coordinator가 우선순위 기반 피드백으로 모든 것 통합

---

## 📁 생성된 파일

1. **intro_complete_revised_RECOVERED_CLEAN.docx** (42KB)
   - 최종 수정된 introduction
   - 3,012 단어, 적절한 형식

2. **intro_improvement_full_result_RECOVERED.json** (25KB)
   - 모든 에이전트의 상세 피드백
   - 우선순위가 할당된 권장사항
   - 설명이 포함된 변경 로그

3. **COMPARISON_REPORT.md**
   - 원본 vs 수정본 나란히 비교
   - 품질 지표 및 개선 퍼센트

---

## ✅ 잘 작동한 점

1. **Gap 명시가 극적으로 개선됨**
   - 모호함에서 구체적으로
   - Gap이 왜 중요한지 명확한 설명

2. **다중 에이전트 접근법이 다양한 이슈 포착**
   - Literature Validator: gap 주장의 정확성
   - Logic Auditor: significance statement 누락
   - Writer: 문장 수준 개선
   - 단일 에이전트로는 모든 것을 포착할 수 없었을 것

3. **우선순위 기반 피드백이 도움됨**
   - 먼저 critical 이슈에 집중 (Priority 2)
   - 중간 우선순위 항목을 반복적으로 처리 (Priority 3)

---

## ⚠️ 한계점

1. **수동 검토 필요**
   - 에이전트가 제안을 제공했지만, 어떤 것을 받아들일지는 내가 결정
   - 일부 제안은 너무 보수적이거나 내 작문 스타일에 맞지 않음

2. **처리 시간**
   - 전체 분석 + 수정에 45분
   - 유료 API로 더 빠를 수 있음 (OpenAI GPT-4, Anthropic Claude)

3. **테이블 처리 없음**
   - Introduction에 8개 대형 테이블 있었음
   - 에이전트는 텍스트 부분만 처리 (테이블은 별도 추출)

---

## 🎓 배운 점

### 글쓰기에 대해
1. **Significance가 gap만큼 중요**
   - "아무도 X를 하지 않았다"라고만 하면 부족
   - "왜 X가 중요하고 X 없이 우리가 무엇을 못 하는지" 설명해야 함

2. **구정보→신정보 흐름이 강력함**
   - 친숙한 정보로 문장을 시작하면 텍스트가 훨씬 읽기 쉬움
   - 작은 변화, 큰 가독성 영향

3. **구체성 > 일반성**
   - "신경 메커니즘 불명확" >> "결과가 일관되지 않음"
   - 구체적 주장이 더 강력하고 설득력 있음

### AI 글쓰기 도구에 대해
1. **다중 에이전트 > 단일 에이전트**
   - 다양한 관점이 다양한 이슈 포착
   - Coordinator 통합이 충돌하는 제안 방지

2. **특정 자료 학습이 도움됨**
   - Williams + Kording/Mensh 학습한 에이전트가 일관되고 증거 기반 피드백 제공
   - 일반 ChatGPT 제안보다 훨씬 나음

3. **우선순위 기반 피드백이 필수**
   - 모든 제안이 동등하지 않음
   - 출판을 위해 실제로 중요한 것에 집중 도움

---

## 📞 연락처

**개발자**: 신정연 (Jeongyeon Shin)
**이메일**: tlswjddus98@snu.ac.kr
**소속**: 서울대학교 심리학과

**수업**: 심리과학 연구방법 - 롸이팅 (AI4Psych Writing Course)

---

## 📚 참고문헌

1. **Williams, J. M., & Bizup, J. (2017)**. *Style: Lessons in Clarity and Grace* (12th ed.). Pearson.

2. **Mensh, B., & Kording, K. (2017)**. Ten simple rules for structuring papers. *PLOS Computational Biology*, *13*(9), e1005619. https://doi.org/10.1371/journal.pcbi.1004205

---

**마지막 업데이트**: 2025년 11월 10일
**버전**: 1.0 (정확)
**상태**: 완료 ✅
