# Notion 워크샵 구조 설계 (Week 2-6)

## 🎯 전체 Workspace 구조

```
📚 심리과학 연구방법 - 롸이팅 (Workspace Root)
│
├─ 📊 Student Submissions Database
│  └─ Properties: 학생명, Week, Section, Status, Peer Reviewer, Score, Feedback
│
├─ 🧪 AI Recipe Library Database
│  └─ Properties: Week, Recipe Name, Purpose, Prompt, Success Rate, Author
│
├─ 📅 Week 2: Nature/Science급 초록 작성
│  ├─ 📖 강의 자료 (전략 패널)
│  ├─ 🧪 AI 실험실 (학생 작업 공간)
│  └─ 📋 Template Buttons
│
├─ 📅 Week 3: 체계적 Research Gap 발견
│  ├─ 📖 강의 자료
│  ├─ 🧪 Gap Discovery Canvas
│  └─ 📋 Templates
│
├─ 📅 Week 4: Methods/Results Bulletproofing
│  ├─ 📖 강의 자료
│  ├─ 🧪 Red Team/Blue Team Game
│  └─ 📋 Templates
│
├─ 📅 Week 5: Discussion Section
│  ├─ 📖 강의 자료
│  ├─ 🧪 AI Diagnostic Canvas
│  └─ 📋 Templates
│
└─ 📅 Week 6: Final Polish & Peer Review
   ├─ 📖 강의 자료
   ├─ 🧪 Hook Generation Canvas
   └─ 📋 Templates
```

---

## 📊 Database 1: Student Submissions

**목적**: 학생별 제출물 및 진도 추적

### Properties

| Property | Type | Description |
|----------|------|-------------|
| 학생명 | Person | 제출자 |
| Week | Select | Week 2/3/4/5/6 |
| Section | Select | Abstract/Intro/Methods/Results/Discussion |
| Status | Status | Not Started/In Progress/Submitted/Peer Reviewed/Revised |
| 제출일 | Date | 제출 날짜 |
| Peer Reviewer | Person | 배정된 동료 리뷰어 |
| Peer Score | Number | 동료 평가 점수 (1-5) |
| Peer Feedback | Text | 동료 피드백 |
| Instructor Feedback | Text | 교수 피드백 |
| Version | Number | 버전 번호 (수정 횟수) |

### Views

1. **By Week** - Week별 그룹핑
2. **By Student** - 학생별 진도 확인
3. **Peer Review Board** - 리뷰 대기 중인 항목
4. **Instructor Review** - 교수 피드백 필요 항목

---

## 🧪 Database 2: AI Recipe Library

**목적**: 성공한 AI 프롬프트 레시피 축적 및 공유

### Properties

| Property | Type | Description |
|----------|------|-------------|
| Recipe Name | Title | 레시피 이름 |
| Week | Select | Week 2/3/4/5/6 |
| Category | Select | Opening/Gap/Methods/Results/Discussion |
| Purpose | Text | 이 레시피의 목적 |
| Prompt Template | Text | 프롬프트 템플릿 (복사 가능) |
| Success Rate | Number | 학생 평가 평균 점수 (1-5) |
| Submitted By | Person | 레시피 제출자 |
| Used Count | Number | 사용 횟수 |
| Example Output | Text | 예시 결과 |
| Tags | Multi-select | Nature, Science, Significance, Gap, etc. |

### Views

1. **By Week** - 주차별 레시피
2. **Top Rated** - Success Rate 높은 순
3. **Most Used** - 사용 빈도 높은 순
4. **By Category** - 카테고리별 그룹핑

---

## 📅 Week 2 Page 구조

### 페이지 레이아웃

```markdown
# Week 2: Nature/Science급 초록 작성 워크샵

## 📚 핵심 전략 (왼쪽 고정 패널)

> 📖 **4가지 Opening Patterns**
>
> <토글: Problem-Driven>
> "현재 문제를 명확히 제시"
> - Nature 예시: ...
> - Science 예시: ...
> </토글>
>
> <토글: Gap-Driven>
> "알려지지 않은 것을 강조"
> - Nature 예시: ...
> </토글>
>
> <토글: Opportunity-Driven>
> "가능성과 잠재력 제시"
> </토글>
>
> <토글: Challenge-Driven>
> "어려움을 해결하는 접근"
> </토글>

> 🎯 **평가 기준**
>
> - Broad Significance (0-2점)
> - Opening Impact (0-2점)
> - Result Clarity (0-1점)
> **Total: 5점**

> 💡 **예시 프롬프트**
>
> <토글: Recipe 1: Problem-Driven Opening>
> **목적**: Nature급 Problem-driven 초록 작성
>
> **프롬프트**:
> ```
> 내 연구를 Nature 수준의 Problem-driven opening으로
> 시작하는 초록을 작성해줘.
>
> 연구 내용:
> [학생이 입력]
>
> 요구사항:
> - 첫 문장에서 broad problem을 제시
> - 왜 이 문제가 중요한지 2-3 문장으로 설명
> - 정량적 수치로 문제의 심각성 표현
> ```
> </토글>
>
> [더 많은 레시피들...]

---

## 🧪 AI 실험실 (학생 작업 공간)

### 실험 1: Opening 전략 비교

<Database - Inline>
Linked to: Student Submissions Database
Filter: Week = "Week 2" AND Section = "Abstract"
</Database>

---

### 💬 실시간 협업 공간

<Template Button: "내 실험 영역 만들기">
Creates:
---
## 📝 [학생명]의 실험 영역

### 📥 Input
> **내 연구 요약**:
> [학생이 입력]

### 🤖 실험 1: Problem-Driven Opening
**사용한 프롬프트**:
```
[학생이 입력]
```

**AI 출력**:
> [AI 결과 붙여넣기]

**자기 평가**:
- Broad Significance: /2
- Opening Impact: /2
- Result Clarity: /1
**Total**: /5

**개선점**:
- [학생 메모]

---

### 🤖 실험 2: Gap-Driven Opening
[동일 구조]

---

### 💬 동료 피드백
> **리뷰어**: @[Peer]
> **피드백**:
> [동료 코멘트]

---
</Template Button>

---

## 📋 워크샵 진행 가이드

### Stage 1: 개인 실험 (10분)
1. "내 실험 영역 만들기" 버튼 클릭
2. 내 연구 요약 입력
3. 2-3가지 Opening 패턴 실험
4. AI 프롬프트와 결과 기록
5. 자기 평가 점수 입력

### Stage 2: 동료 리뷰 (10분)
1. 옆 사람의 실험 영역 방문
2. AI 출력 결과 읽기
3. 평가 기준에 따라 점수 부여
4. "💬 동료 피드백" 섹션에 코멘트 작성

### Stage 3: 집단 큐레이션 (10분)
1. 최고 점수 받은 프롬프트 공유
2. 교수자 해설
3. 성공한 레시피를 "AI Recipe Library"에 추가
4. 다음 실험 계획
```

---

## 📅 Week 3 Page 구조

```markdown
# Week 3: 체계적 Research Gap 발견 워크샵

## 📚 핵심 전략

> 📖 **Gap 유형 분류**
>
> <토글: Incremental Gap (탑티어 부적합)>
> "이 조건에서는 아직 실험 안 됨"
> ❌ Nature/Science 부적합
> </토글>
>
> <토글: Conceptual Gap (탑티어 적합)>
> "이론으로 설명 안 됨"
> ✅ Nature/Science 적합
> 예시: ...
> </토글>
>
> <토글: Mechanistic Gap>
> "작동 원리 불명확"
> ✅ Nature/Science 적합
> </토글>
>
> <토글: Paradox Gap>
> "모순 결과들 존재"
> ✅ Nature/Science 적합
> </토글>

> 🎯 **3-Stage Validation Workflow**
>
> **Stage 1**: Landscape Mapping
> - Consensus 파악
> - Contradiction 발견
> - Unexplored areas 식별
>
> **Stage 2**: Critical Review
> - Methodological limitations
> - Theoretical limitations
> - Generalizability issues
>
> **Stage 3**: Feasibility Check
> - 실현 가능성 평가
> - 자원 확인
> - 타임라인 검토

> 💡 **AI 프롬프트 레시피**
>
> <토글: Recipe 1: Gap Quality Assessment>
> [프롬프트 템플릿]
> </토글>
>
> <토글: Recipe 2: Landscape Mapping>
> [프롬프트 템플릿]
> </토글>

---

## 🧪 Gap Discovery Canvas

<Database - Inline>
Linked to: Student Submissions Database
Filter: Week = "Week 3"
</Database>

<Template Button: "내 Gap Discovery 시작하기">
Creates:
---
## 📝 [학생명]의 Gap Discovery

### Stage 1: Landscape Mapping
**AI 프롬프트**:
```
[학생이 입력]
```

**AI 결과**:
- **Consensus**: [정리]
- **Debates**: [정리]
- **Unexplored**: [정리]

### Stage 2: Gap Quality Assessment
**내 Gap Statement**:
> [학생이 작성]

**AI 평가 요청**:
```
다음 gap을 평가해줘:
(1) Gap 유형 분류
(2) Nature/Science 적합성 점수 (1-10)
(3) 강화 방안
```

**AI 평가 결과**:
- Gap 유형: [  ]
- 적합성: /10
- 강화 방안: [  ]

### Stage 3: 3-Stage Validation
- [ ] Evidence 1 확인됨
- [ ] Evidence 2 확인됨
- [ ] Evidence 3 확인됨
- [ ] Feasibility 검증됨

### 💬 동료 피드백
> **리뷰어**: @[Peer]
> **Is this gap truly conceptual/mechanistic?**
> [코멘트]

---
</Template Button>
```

---

## 📅 Week 4-6 구조 (간략)

**Week 4**: Methods/Results Bulletproofing
- Red Team/Blue Team 게임
- Reproducibility Checklist (6 critical elements)
- Control Validation Canvas

**Week 5**: Discussion Section
- AI Diagnostic Canvas
- 3-Pass Revision Worksheet
- Before/After Transformations

**Week 6**: Final Polish & Peer Review
- Hook Generation Canvas
- 3-Stage Structure Builder
- Impact Pyramid Worksheet
- Round-Robin Comprehensive Review

---

## 🔧 Notion 구현 기술 요구사항

### API 호출 순서
1. ✅ Create "Student Submissions" Database
2. ✅ Create "AI Recipe Library" Database
3. ✅ Create Week 2-6 Workshop Pages
4. ✅ Populate 강의 자료 (토글 블록으로)
5. ✅ Add Template Buttons (Notion API limitation: requires manual setup)
6. ✅ Create example submissions for demonstration

### Notion API Limitations
- ❌ Template Buttons는 API로 생성 불가 → 수동 설정 필요
- ✅ Database, Pages, Blocks는 모두 API로 생성 가능
- ✅ Database Views는 API로 생성 가능
- ✅ Relations/Rollups 설정 가능

### Python Script 구조
```python
# 1. create_databases.py - Database 생성
# 2. create_week_pages.py - Week 2-6 페이지 생성
# 3. populate_content.py - 강의 자료 입력
# 4. create_examples.py - 예시 제출물 생성
```

---

## 📝 수동 설정 필요 사항

### Template Button 설정 (각 Week 페이지에서)
1. `/template` 타이핑
2. "Template button" 선택
3. 버튼 이름: "내 실험 영역 만들기"
4. Template 내용: 위 설계대로 블록 구성
5. 완료

예상 시간: 주차당 5분 × 5주 = 25분

---

## ✅ 장점 요약

### Figma 대비 Notion의 장점
1. ✅ **API 자동 생성**: 강의 자료 및 구조 자동 생성
2. ✅ **Database 활용**: 학생 제출물 및 레시피 체계적 관리
3. ✅ **Template Button**: 학생별 작업 공간 빠른 복사
4. ✅ **익숙한 인터페이스**: 대부분 학생이 Notion 사용 경험 있음
5. ✅ **실시간 협업**: 동료 피드백을 인라인 코멘트로
6. ✅ **검색 및 필터링**: Database views로 원하는 정보 빠르게 접근
7. ✅ **지속적 사용**: 수업 후에도 레시피 라이브러리로 활용

### Notion 특화 기능
- **Linked Database**: 여러 페이지에서 같은 데이터 다른 뷰로 표시
- **Rollup**: 학생별 평균 점수 자동 계산
- **Formula**: 자동 채점/통계
- **@mention**: 동료 리뷰어 태그
- **Export**: PDF/Markdown으로 백업

---

## 🚀 다음 단계

1. ✅ 설계 문서 확정
2. 🔄 Python 스크립트 작성
3. 🔄 Notion Workspace에 자동 생성
4. 🔄 Template Button 수동 설정 (25분)
5. ✅ 학생 초대 및 권한 설정
6. ✅ Week 2 워크샵 실행 및 피드백 수집
