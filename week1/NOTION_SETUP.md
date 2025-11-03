# Week 1 Notion Workshop - 완벽 가이드 🚀

## 🎯 왜 Notion이 최고인가?

### Google Docs vs Notion

| 기능 | Google Docs | **Notion** |
|------|-------------|------------|
| 셋업 시간 | 1분 | **30초** (스크립트 실행) |
| 구조화 | ❌ 선형만 | ✅ **토글, 컬럼, Database** |
| 학생 작업 관리 | ❌ 텍스트만 | ✅ **Database 필터/정렬** |
| UI/UX | ⚠️ 평범 | ✅ **깔끔하고 예쁨** |
| 템플릿 복제 | ❌ 복사-붙여넣기 | ✅ **Duplicate 버튼** |
| 진행 상황 추적 | ❌ 수동 | ✅ **자동 (Database)** |
| 실시간 협업 | ✅ | ✅ |
| 댓글 | ✅ | ✅ |

### Notion만의 장점

```
📊 Database로 학생 작업 관리:
- 상태: ⏳ 대기 → 🔄 작업중 → ✅ 완료
- 필터: "내 작업만 보기", "완료된 것만"
- 정렬: 학생 이름, 진행률, 완료 시간

🎨 시각적으로 예쁨:
- 컬러 코딩 (Stage별)
- 아이콘 (🔬, 📄, ✅)
- 토글로 깔끔한 구조

🔄 Synced Block:
- Week 1 원칙을 어디서나 참조
- 한 번 수정하면 모든 곳에 반영

✨ 템플릿 버튼:
- "새 학생 추가" 버튼 클릭
- 7-Step 구조 자동 생성
```

---

## ⚡ 30초 시작 방법

### 준비물
1. ✅ Notion 계정
2. ✅ Integration Token (아래 단계 참조)
3. ✅ 페이지 ID: `29a41454561d809f871eef8102006369`

### Step 1: Notion Integration Token 발급 (1분)

1. https://www.notion.so/my-integrations 접속
2. "+ New integration" 클릭
3. 이름: `Week 1 Workshop Builder`
4. 권한: 기본값 (Read, Update, Insert content)
5. "Submit" 클릭
6. **Secret Token 복사** (나중에 사용)

   ```
   예: secret_FxA7B...
   ```

### Step 2: 페이지에 Integration 연결 (30초)

1. Notion 페이지 열기: https://www.notion.so/29a41454561d809f871eef8102006369
2. 우측 상단 `⋯` (More) 클릭
3. `+ Add connections` 클릭
4. `Week 1 Workshop Builder` 선택

### Step 3: 스크립트 실행 (10초)

```bash
cd week1
python create_notion_workshop.py \
  --page-id 29a41454561d809f871eef8102006369 \
  --token "secret_여기에_토큰_붙여넣기"
```

또는 환경변수로:

```bash
export NOTION_TOKEN="secret_여기에_토큰_붙여넣기"
python create_notion_workshop.py --page-id 29a41454561d809f871eef8102006369
```

### 완료! ✨

Notion 페이지로 돌아가면 워크샵 구조가 자동으로 생성되어 있습니다!

---

## 📊 생성되는 Notion 구조

### 1. 📚 Week 1 원칙 참조 (Synced Block)
```
3개 컬럼 레이아웃:
┌─────────────┬─────────────┬─────────────┐
│ Lesson 1    │ Lesson 2    │ Lesson 3    │
│ 주어-동사   │ 응집성      │ 간결성      │
│ • 동작→동사 │ • Old→New   │ • 불필요제거│
│ • 주체→주어 │ • 전략수동  │ • 간단언어  │
│ • 가깝게    │ • 문단응집  │ • 수식제한  │
└─────────────┴─────────────┴─────────────┘
```

어디서든 이 블록을 참조 가능!

### 2. 🔬 STAGE 1A: Bad Sentences Database

**Database 컬럼**:
- 문장 (Title)
- 학생 (Select)
- 문제점 (Rich Text)
- 수정안 (Rich Text)
- 상태 (Select: ⏳ 대기 / 🔄 작업중 / ✅ 완료)
- Peer Feedback (Rich Text)

**초기 데이터** (3개 필수 문장):
1. #1: Nominalization
2. #5: Old→New 흐름
3. #9: 복잡한 주어

**View 옵션**:
- 📋 Table View: 전체 현황
- 👤 내 작업: Filter by "학생 = 나"
- ✅ 완료된 것: Filter by "상태 = 완료"

### 3. 📄 STAGE 1B: Bad Paragraphs Database

**Database 컬럼**:
- 문단 (Title)
- 학생 (Select)
- 문제점 (Rich Text)
- 개선안 (Rich Text)
- 상태 (Select)
- 단어수 개선 (Number)

**초기 데이터** (4개 문단):
1. P1: Abstract - 수동태 + Nominalization (44 words)
2. P2: Introduction - 주어-동사 거리 (52 words)
3. P3: Introduction - Old→New 흐름 (58 words)
4. P4: Introduction - 간결성 (65 words)

### 4. ✅ STAGE 2: Smart Revising Database

**Database 컬럼**:
- 학생 (Title)
- 페어 (Select) - 자동 매칭 (A↔B, C↔D...)
- Step 1-7 (Checkbox)
- 진행률 (Number) - 0-100%
- 단어수 개선 (Rich Text)
- 상태 (Select: ⏳/🔄/📝/✅)

**각 학생 페이지 구조**:
```
📄 내 초록 (원문)
[여기에 붙여넣기]

───────────────────────

▶ Step 1: Nominalization 찾기 (Toggle)
   발견한 내용...

▶ Step 2: 주어 확인 (Toggle)
   주제 vs 주어...

▶ Step 3-7 (Toggle)
   나머지 단계...

───────────────────────

💬 Peer Feedback (from 페어)
[페어가 댓글로 피드백]

───────────────────────

📝 최종 수정 버전
[최종 결과]
```

**초기 설정** (10명 학생):
- 학생A ↔ 학생B
- 학생C ↔ 학생D
- 학생E ↔ 학생F
- 학생G ↔ 학생H
- 학생I ↔ 학생J

---

## 🎬 수업 진행 방법

### 수업 전 (5분)
1. Notion 링크 학생들에게 공유
2. 권한 설정: "Can edit" (학생들이 편집 가능)
3. 간단한 Notion 사용법 안내 (2분)

### Stage 1A (15분)

**학생 작업**:
1. Database에서 "학생" 컬럼에 본인 이름 선택
2. 필수 3개 문장 작업 (#1, #5, #9)
3. "문제점", "수정안" 컬럼에 작성
4. "상태"를 ✅ 완료로 변경

**교수자 모니터링**:
- Database Table View로 전체 현황 실시간 확인
- 댓글로 즉각 피드백
- 우수 사례에 👍 반응

### Stage 1B (15분)

**학생 작업**:
1. 4개 문단 중 2개 선택
2. Database에 본인 이름 입력
3. 문제점 분석 → 개선안 작성
4. "단어수 개선" 계산 (예: 44 → 38)

### Stage 2 (20분)

**학생 작업**:
1. Smart Revising Database에서 본인 이름 클릭
2. 페이지 열기 → 초록 붙여넣기
3. 각 Step Toggle 열어서 작업
4. Checkbox 클릭으로 진행 표시
5. 페어 페이지로 이동 → 댓글로 피드백

**교수자 모니터링**:
- Database에서 "진행률" 컬럼 확인
- 막히는 학생에게 댓글로 가이드
- 우수 사례 공유

---

## 💡 Notion 고급 기능 활용

### 1. Database View 커스터마이징

**Stage 1A 유용한 View**:

```
View 1: 📋 전체 현황 (Table)
- 모든 컬럼 표시
- 정렬: 문장 번호

View 2: 👤 내 작업만
- Filter: 학생 = 본인
- Hidden: 다른 학생 작업

View 3: ✅ 완료된 것
- Filter: 상태 = 완료
- 정렬: 완료 시간

View 4: 📊 진행 현황 (Board)
- Group by: 상태
- Card layout: 문장 + 학생
```

### 2. Template Button 추가

**"새 학생 추가" 버튼**:

Stage 2 Database에 Template Button 추가:
```
템플릿 내용:
- 📄 내 초록 (원문)
- 7개 Step Toggle
- 💬 Peer Feedback 섹션
- 📝 최종 수정 버전

사용: 버튼 클릭 → 학생 이름 입력 → 자동 생성
```

### 3. Synced Block 활용

Week 1 원칙을 여러 곳에 복사:
1. 원본 Synced Block 생성 (이미 스크립트에 포함)
2. 다른 위치에 복사: `/synced` → "Original" 선택
3. 원본 수정하면 모든 복사본 자동 업데이트

### 4. 댓글 알림

학생들이 댓글 달면 실시간 알림:
- Notion 앱에서 알림
- 이메일 알림 (설정 가능)
- @멘션으로 특정 학생 호출

### 5. 진행률 자동 계산

Smart Revising Database에 Formula 추가:

```javascript
// 진행률 계산 (7개 Step 중 체크된 개수)
prop("Step 1") ? 14 : 0 +
prop("Step 2") ? 14 : 0 +
prop("Step 3") ? 14 : 0 +
prop("Step 4") ? 14 : 0 +
prop("Step 5") ? 14 : 0 +
prop("Step 6") ? 14 : 0 +
prop("Step 7") ? 14 : 0
```

---

## 📱 학생 사용 가이드 (1-Page)

```markdown
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Notion Workshop 학생 가이드
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📱 Notion 기본 조작:
• Database: 표처럼 생긴 곳
• Page: 클릭하면 열리는 개별 문서
• Toggle: ▶ 클릭하면 펼쳐짐
• Comment: 텍스트 선택 → 댓글 버튼

🔬 STAGE 1A: Bad Sentences
1. Database에서 문장 #1 클릭
2. "학생" 컬럼에서 본인 이름 선택
3. "문제점" 컬럼에 발견한 문제 작성
4. "수정안" 컬럼에 수정 버전 작성
5. "상태"를 ✅ 완료로 변경
6. #5, #9 반복

📄 STAGE 1B: Bad Paragraphs
1. 4개 문단 중 2개 선택
2. 같은 방식으로 작업
3. "단어수 개선" 계산해서 입력

✅ STAGE 2: Smart Revising
1. Database에서 본인 이름 클릭
2. 페이지가 열림
3. "내 초록" 영역에 붙여넣기
4. 각 Step Toggle 열어서 작업
5. Checkbox 클릭으로 완료 표시
6. 페어 페이지로 이동 → 댓글로 피드백

💡 팁:
• Database에서 "내 작업만" View 사용
• 페어 이름은 자동 표시됨
• 댓글에 @이름으로 멘션 가능
• 실시간 자동 저장

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🆘 문제 해결

### "스크립트 실행 시 오류"

**오류 1**: `notion-client not found`
```bash
pip install notion-client
```

**오류 2**: `Unauthorized`
→ Integration Token 확인
→ 페이지에 Integration 연결 확인

**오류 3**: `Page not found`
→ 페이지 ID 확인: `29a41454561d809f871eef8102006369`
→ Integration이 페이지에 접근 권한 있는지 확인

### "학생이 편집 못 함"

→ 페이지 권한 확인:
1. 우측 상단 `Share` 클릭
2. "Anyone with the link" → "Can edit"
3. 링크 복사 → 학생들에게 발송

### "Database가 복잡함"

→ View 단순화:
1. Database 우측 상단 `...` 클릭
2. `Properties` 클릭
3. 불필요한 컬럼 숨기기 (Hide)

---

## 📊 수업 후 활용

### 1. 통계 확인

**Database에서 자동 집계**:
- 완료율: ✅ 완료 / 전체
- 평균 진행률: 진행률 컬럼 평균
- 단어수 개선: 평균 개선율 계산

### 2. 우수 사례 북마크

좋은 수정안에:
1. 댓글로 "⭐ 우수 사례" 표시
2. 또는 Database에 "우수 사례" 컬럼 추가 (Checkbox)
3. Filter로 우수 사례만 보기

### 3. 다음 학기 재사용

1. 페이지 우측 상단 `...` 클릭
2. `Duplicate` 클릭
3. 학생 이름만 변경
4. Database 내용 초기화

또는:

```bash
# 스크립트 재실행
python create_notion_workshop.py --page-id 새페이지ID
```

---

## 🎁 보너스: 확장 아이디어

### 1. 진행률 Progress Bar

Database에 Formula 추가:
```javascript
// Progress Bar 시각화
if(prop("진행률") == 100, "✅✅✅✅✅",
if(prop("진행률") >= 80, "✅✅✅✅⬜",
if(prop("진행률") >= 60, "✅✅✅⬜⬜",
if(prop("진행률") >= 40, "✅✅⬜⬜⬜",
if(prop("진행률") >= 20, "✅⬜⬜⬜⬜", "⬜⬜⬜⬜⬜")))))
```

### 2. 자동 피드백 템플릿

Peer Feedback 섹션에 Template Button:
```
[템플릿 1: 긍정 피드백]
✅ 잘된 점:
-

💡 개선 제안:
-

[템플릿 2: 구체적 피드백]
주어-동사:
Old→New:
간결성:
```

### 3. Gallery View로 시각화

Stage 1B Database를 Gallery View로:
- Card Preview: 문단 원문
- Card Property: 학생, 상태, 단어수 개선
- 한눈에 모든 작업 확인

---

## ✅ 최종 체크리스트

**실행 전**:
- [ ] Notion Integration Token 발급
- [ ] 페이지에 Integration 연결
- [ ] `notion-client` 설치 확인

**실행**:
- [ ] 스크립트 실행
- [ ] Notion 페이지 확인
- [ ] Database 3개 생성 확인
- [ ] 10명 학생 페이지 생성 확인

**수업 전**:
- [ ] 링크 학생들에게 공유
- [ ] 권한 "Can edit" 확인
- [ ] 학생 가이드 공유

**수업 후**:
- [ ] 우수 사례 북마크
- [ ] 통계 확인
- [ ] 다음 학기 템플릿 복제

---

## 🚀 시작하기

1. Integration Token 발급 (위 Step 1)
2. 페이지에 Integration 연결 (위 Step 2)
3. 스크립트 실행:

```bash
python create_notion_workshop.py \
  --page-id 29a41454561d809f871eef8102006369 \
  --token "YOUR_TOKEN"
```

**30초 후 Notion 페이지 확인!** ✨

---

## 💬 추가 질문?

- Notion API 공식 문서: https://developers.notion.com
- notion-client GitHub: https://github.com/ramnes/notion-sdk-py
- Notion 커뮤니티: https://www.notion.so/help

**이제 Notion으로 훨씬 더 나은 워크샵을 진행하세요!** 🎉
