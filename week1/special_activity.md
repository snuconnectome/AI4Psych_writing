# 특별활동: 나만의 Writing & Revising Agent 만들기

**소요 시간**: 30분
**도구**: Claude Code (무료)
**목표**: Week 1의 10가지 원칙을 내장한 personal writing coach 만들기

---

## 📋 활동 개요

오늘 수업에서 배운 **10가지 핵심 원칙**을 기억하고 계신가요?
이제 이 원칙들을 여러분의 개인 AI writing coach에 내장해서,
언제든지 자신의 논문을 분석하고 개선할 수 있는 도구를 만들어봅시다!

### 왜 이 활동이 중요한가?

1. **반복 사용 가능**: 한번 만들면 논문 작성 내내 사용
2. **즉각적 피드백**: 문장을 쓰는 즉시 개선안 확인
3. **학습 강화**: 원칙을 agent에 내장하면서 재학습
4. **맞춤형 코치**: 여러분의 연구 분야에 맞게 조정 가능

---

## 🎯 학습 목표

이 활동을 마치면 다음을 할 수 있습니다:

- [ ] Claude Code를 설치하고 기본 사용법 이해
- [ ] Slash Command를 만들어 개인 agent 생성
- [ ] 10가지 원칙을 agent에 내장
- [ ] 자신의 논문 문장을 agent로 분석하고 개선
- [ ] Before/After 비교로 개선 효과 확인

---

## ⏱️ 30분 타임라인

| 시간 | 활동 | 내용 |
|------|------|------|
| 0-5분 | 소개 & 설정 | Claude Code 설치, 프로젝트 구조 이해 |
| 5-15분 | Agent 만들기 | Slash command 작성, 10가지 원칙 내장 |
| 15-25분 | 실전 사용 | 예제 문장 개선, 자신의 초록 개선 |
| 25-30분 | 공유 & 정리 | 결과 공유, Q&A, 과제 안내 |

---

## Part 1: 소개 & 설정 (5분)

### Claude Code란?

Claude Code는 Anthropic이 만든 AI coding assistant입니다.
코딩뿐만 아니라 **문서 작성, 분석, 편집**에도 사용할 수 있습니다.

**특징**:
- 무료로 사용 가능 (개인 사용)
- VS Code, Cursor, Windsurf 등에 통합
- Slash commands로 custom agents 생성 가능

### 설치 방법

**Option 1: VS Code Extension (추천)**
1. VS Code 실행
2. Extensions (Ctrl/Cmd+Shift+X)
3. "Claude Code" 검색
4. Install
5. Anthropic 계정으로 로그인

**Option 2: Cursor IDE**
- Cursor에 기본 내장 (별도 설치 불필요)

**Option 3: Windsurf**
- Windsurf에 기본 내장

### 프로젝트 구조 이해

Claude Code는 프로젝트 폴더 구조를 이해합니다:

```
my-research-paper/
├── .claude/
│   └── commands/
│       └── writing-agent.md  ← 우리가 만들 파일
├── abstract.md
├── introduction.md
└── methods.md
```

`.claude/commands/` 폴더에 만든 `.md` 파일은 자동으로 slash command가 됩니다!

---

## Part 2: Agent 만들기 (10분)

### Step 1: 프로젝트 폴더 생성

1. 바탕화면 또는 문서 폴더에 새 폴더 생성:
   - 폴더명: `my-thesis-writing` (원하는 이름)

2. VS Code에서 폴더 열기:
   - File → Open Folder
   - 방금 만든 폴더 선택

### Step 2: .claude/commands 폴더 생성

VS Code 내에서:

1. 좌측 Explorer에서 New Folder 클릭
2. `.claude` 입력 (점 포함!)
3. `.claude` 폴더 안에 `commands` 폴더 생성

최종 구조:
```
my-thesis-writing/
└── .claude/
    └── commands/
        └── (여기에 writing-agent.md 생성 예정)
```

### Step 3: writing-agent.md 파일 생성

1. `commands` 폴더 우클릭 → New File
2. 파일명: `writing-agent.md`
3. 파일 열기

### Step 4: Agent 내용 작성

**방법 A: 템플릿 복사 (추천)**

교수자가 제공한 `writing-agent-template.md` 파일을 열고 전체 내용을 복사하여 붙여넣기.

**방법 B: 직접 작성**

다음 구조로 작성:

```markdown
당신은 과학 논문 작성을 돕는 **Writing & Revising Coach**입니다.

## 당신의 역할
사용자가 제공한 문장이나 문단을 분석하고, Duke Scientific Writing의 10가지 핵심 원칙을 적용하여 개선안을 제시합니다.

## 분석 프레임워크: 10가지 핵심 원칙

### Lesson 1: 주어-동사 (3가지 원칙)
[Week 1 강의 내용 복사]

### Lesson 2: 응집성 (3가지 원칙)
[Week 1 강의 내용 복사]

### Lesson 3: 간결성 (4가지 원칙)
[Week 1 강의 내용 복사]

## 분석 및 개선 프로세스
[분석 방법 및 출력 형식 명시]
```

**중요**: 10가지 원칙을 **모두** 포함해야 agent가 제대로 작동합니다!

### Step 5: 파일 저장

- Ctrl/Cmd+S로 저장
- 저장 후 Claude Code가 자동으로 `/writing-agent` 명령을 인식

---

## Part 3: 실전 사용 (10분)

### Agent 실행 방법

1. VS Code에서 Claude Code 패널 열기 (Ctrl/Cmd+Shift+P → "Claude")
2. 채팅창에 `/writing-agent` 입력
3. Agent가 시작 메시지 출력

### 예제 1: dukeWriting_lesson1.pdf의 문장 개선

교수자가 제공한 `dukeWriting_lesson1.pdf`를 열고, 다음 문장을 agent에게 입력:

**입력:**
```
Tyrosine phosphorylation by activated JAKs of cytokine-receptor cytoplasmic domains then provides binding sites for the Src-homology-2 domain of the STAT proteins.
```

**Agent의 분석:**
- Nominalization: "phosphorylation"
- 주어-동사 거리 과도
- 수동태로 주체 불명확

**개선안:**
```
Activated JAKs phosphorylate tyrosine on cytokine-receptor cytoplasmic domains, creating binding sites for the Src-homology-2 domain of STAT proteins.
```

**개선 효과:**
- 27 words → 20 words (-26% 감축)
- 동사 "phosphorylate" 사용
- 주체 "JAKs" 명확

### 예제 2: 자신의 초록 문장 개선

이제 자신의 연구 초록에서 한 문장을 선택해서 agent에게 입력해보세요.

**팁**:
- Methods 섹션 문장이 개선 효과가 크게 나타남
- 수동태가 많은 문장을 선택
- 길고 복잡한 문장일수록 개선 여지 많음

**실습 시간**: 5분

1. 자신의 초록에서 1-2개 문장 선택
2. `/writing-agent`에게 입력
3. Before/After 비교
4. 개선안을 초록에 반영

### 예제 3: 문단 수준 개선 (시간 있으면)

단일 문장이 아닌 전체 문단을 입력하면:
- Old→New 흐름 분석
- 문단 응집성 체크
- 문장 간 연결 개선

---

## Part 4: 공유 & 정리 (5분)

### 개선 사례 공유

**질문**:
- 가장 효과적이었던 개선은?
- 예상치 못한 발견이 있었나요?
- 어떤 원칙이 가장 많이 위반되었나요?

**공유 형식**:
```
문장: [원문]
문제: [발견한 문제]
개선: [개선안]
효과: -XX% 단어 감축
```

### Tips & Tricks

1. **반복 사용**: 논문 쓸 때마다 `/writing-agent` 사용
2. **커스터마이징**: 자신의 분야에 맞게 agent 수정
3. **학습 도구**: 개선안을 보면서 원칙 재학습
4. **비교 분석**: 여러 버전을 agent로 비교

### 한계점 인식

Agent는 도구일 뿐입니다:
- ✅ 문법, 구조, 명확성 개선
- ❌ 과학적 정확성, 논리 구조, 연구 방법 검증

**최종 판단은 항상 여러분이 해야 합니다!**

---

## 📝 과제

### 1. Agent 완성 및 제출

- `.claude/commands/writing-agent.md` 파일 완성
- 10가지 원칙 모두 포함 확인
- 파일을 LMS에 제출 (마감: 다음 주 수업 전)

### 2. 자신의 초록 개선

- 1주차 과제로 작성한 초록 (150-200 words)
- Agent로 문장별 분석
- 개선 전후 비교표 작성

**제출 형식**:
```markdown
## 초록 개선 보고서

### 문장 1
**Before**: [원문]
**문제점**: [Agent가 발견한 문제]
**After**: [개선안]
**개선 효과**: [단어 수, 원칙 적용]

### 문장 2
...

### 전체 요약
- 총 단어 수: XXX → YYY words (-ZZ%)
- 주요 개선: [3가지]
```

### 3. (선택) 나만의 원칙 추가

Agent에 다음을 추가할 수 있습니다:
- 심리학 특화 용어 가이드
- 자신의 연구실 스타일 가이드
- 자주 하는 실수 체크리스트

---

## 🔧 문제 해결 (Troubleshooting)

### Q1: `/writing-agent`가 인식되지 않아요
**A**:
1. 파일명 확인: `writing-agent.md` (하이픈, 소문자)
2. 위치 확인: `.claude/commands/` 폴더 안
3. VS Code 재시작

### Q2: Agent가 10가지 원칙을 적용하지 않아요
**A**:
1. `writing-agent.md` 파일에 10가지 원칙이 모두 명시되어 있는지 확인
2. "분석 프레임워크" 섹션 확인
3. 원칙을 구체적으로 작성 (예시 포함)

### Q3: Agent가 너무 길게 답변해요
**A**:
`writing-agent.md`에 다음 추가:
```markdown
## 출력 제약
- 간결하게 답변 (500자 이내)
- Before/After만 집중
```

### Q4: Claude Code 계정이 없어요
**A**:
1. https://claude.ai 방문
2. 무료 계정 생성 (이메일 또는 Google)
3. VS Code에서 해당 계정으로 로그인

### Q5: 초록이 아직 없어요
**A**:
1. dukeWriting_lesson1.pdf의 예제 문장으로 연습
2. 참고 논문의 초록에서 문장 선택해서 연습
3. 간단한 연구 아이디어를 2-3 문장으로 작성해서 연습

---

## 📚 추가 자료

### 참고 문서
- `dukeWriting_lesson1.pdf`: 9개 예제 문장
- `Lesson 1-3 PDFs`: Duke Scientific Writing 전체 자료
- `ten simple rules for writing.pdf`: PLOS 논문

### 온라인 리소스
- Claude Code Documentation: https://docs.claude.com/
- Duke Scientific Writing: https://cgi.duke.edu/web/sciwriting/

### 다음 주 예고

**Week 2: AI 활용 I - Nature/Science급 초록 작성**
- 오늘 만든 agent를 더욱 강화
- 최상위 저널 초록 작성 전략
- AI로 초록을 10배 개선하는 40+ 프롬프트

---

## 💬 Q&A

질문이 있으시면:
- 수업 중: 손들고 질문
- 수업 후: 이메일 또는 LMS 게시판
- 급한 경우: 오피스 아워 방문

---

**🎉 축하합니다!**

여러분은 이제 자신만의 Writing & Revising Agent를 가지고 있습니다!
논문을 쓸 때마다 agent에게 물어보세요.
점점 더 명확하고 강력한 글쓰기가 가능해질 것입니다.

**Good writing is rewriting. 그리고 이제 여러분에게는 AI coach가 있습니다!** 🚀
