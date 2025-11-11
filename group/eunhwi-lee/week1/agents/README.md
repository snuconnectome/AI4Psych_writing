# Scientific Writing Assistant Commands

이 폴더에는 Duke Graduate School의 precision writing 원칙과 Kording & Mensh의 논문 구조 가이드라인을 기반으로 한 학술 논문 작성 도구들이 포함되어 있습니다.

## 📚 기반 자료

이 명령어들은 다음 자료들의 원칙을 구현합니다:
- **Duke Graduate School Scientific Writing Resource** ([/ref](../ref/) 참조)
  - Lesson 1: Subjects and Actions
  - Lesson 2: Cohesion, Coherence, and Emphasis
  - Lesson 3: Concision and Simplicity
- **"Ten Simple Rules for Structuring Papers"** (Kording & Mensh)

## 🚀 빠른 시작

### 1. `/quick-fix` - 빠른 수정
**언제 사용:** 문장을 빠르게 정리하고 싶을 때

```
/quick-fix

[논문 텍스트를 붙여넣기]
```

**제공 기능:**
- 불필요한 문구 제거
- 장황한 표현 간소화
- 명사화된 동사를 동사로 변환
- 과도한 hedging 줄이기
- ~20% 단어 수 감소

**사용 예시:**
```
원본: "It should be noted that we performed an analysis of the data
       prior to conducting further investigations."

수정: "We analyzed the data before further investigation."
```

---

### 2. `/writing-review` - 정밀 분석
**언제 사용:** 논문 섹션을 깊이 있게 리뷰받고 싶을 때

```
/writing-review

[분석할 텍스트 붙여넣기]
```

**제공 기능:**
- Subjects & Actions 분석
- Cohesion & Coherence 체크
- Concision 개선 제안
- 구체적인 before/after 예시
- 우선순위별 수정 사항

**분석 항목:**
1. **주어-동사 명확성**
   - 명사화 찾기
   - 주어-동사 거리
   - 문단 내 주어 일관성

2. **흐름과 연결성**
   - 새 정보/기존 정보 배치
   - 수동태 적절성
   - 문단 coherence

3. **간결성**
   - 제거할 문구
   - 단순화할 단어
   - 복잡한 주어 해결

---

### 3. `/draft-section` - 섹션 초안 작성
**언제 사용:** Abstract, Introduction 등 특정 섹션을 작성할 때

```
/draft-section

섹션: Abstract
주제: 기계학습을 이용한 단백질 구조 예측
주요 결과: 기존 방법보다 15% 정확도 향상
```

**지원 섹션:**
- **Abstract**: Context-Content-Conclusion 구조
- **Introduction**: Funnel 구조 (broad → narrow → gap)
- **Results**: 논리적 순서로 결과 제시
- **Discussion**: 발견 요약 → 한계점 → 의의
- **Methods**: 재현 가능한 수준의 상세 설명

**작성 프로세스:**
1. 필요한 정보 질문
2. 구조화된 아웃라인 제공
3. 단락별 초안 작성
4. 리뷰 노트 제공

---

### 4. `/citation-help` - 인용 분석
**언제 사용:** 어디에 citation이 필요한지 확인하고 싶을 때

```
/citation-help

[텍스트 붙여넣기]
```

**제공 기능:**
- Citation 누락 지점 식별
- 적절한 citation 전략 제안
- Citation 밀도 평가
- 통합 스타일 개선 제안

**분석 내용:**
- 인용이 필요한 주장 찾기
- 섹션별 적절한 인용 밀도
- Self-citation 적절성
- 인용 통합 스타일

**주의:** 실제 논문을 검색하거나 제공하지는 않습니다. 어떤 타입의 citation이 필요한지만 알려줍니다.

---

### 5. `/extract-concepts` - 핵심 개념 추출
**언제 사용:** 긴 논문에서 핵심 개념을 구조화하여 추출하고 싶을 때

```
/extract-concepts

[논문 텍스트 붙여넣기]

Focus areas: [선택사항 - 강조할 측면]
Target use: For introduction synthesis
```

**제공 기능:**
- 이론적 프레임워크 식별
- 핵심 constructs 정리
- 방법론적 접근 요약
- 주요 결과 추출
- Gap 및 한계점 파악

**출력 구조:**
- **개념별 카테고리**: Frameworks, Constructs, Methods, Findings
- **용어 사전**: 논문에서 사용된 정의
- **통합 준비도**: 다른 논문과 연결 가능한 개념들
- **Quick Reference**: 섹션별 핵심 포인트

**사용 시나리오:**
- 리뷰 페이퍼 작성 전 여러 논문 정리
- 큰 PDF 파일을 단계적으로 처리
- Literature synthesis 준비

---

### 6. `/synthesize-intro` - 다중 논문 통합 Introduction 작성
**언제 사용:** 여러 논문의 내용을 통합하여 새로운 리뷰 페이퍼 Introduction을 작성할 때

```
/synthesize-intro

New review topic: [새 리뷰의 주제와 범위]

Source materials:
=== PAPER 1 ===
[extract-concepts에서 추출한 핵심 내용]

=== PAPER 2 ===
[extract-concepts에서 추출한 핵심 내용]

New synthesis gap: [두 논문의 교집합에서 발견되는 gap]
```

**제공 기능:**
- Funnel 구조 (broad → narrow → gap) 자동 구성
- 여러 논문의 개념을 자연스럽게 통합
- 새로운 synthesis gap 명확화
- Citation 전략 제안
- 통합 맵 (어떤 개념을 어떻게 연결했는지)

**통합 전략:**
- **Overlapping concepts**: 공통 개념 통합
- **Complementary perspectives**: 보완적 관점 융합
- **Bridging concepts**: 논문 간 연결 고리 생성
- **Novel synthesis**: 통합에서 나오는 새로운 이해

**출력:**
- 완전한 Introduction 초안 (paragraph-by-paragraph)
- Integration notes (어떻게 통합했는지)
- Citation placement 제안
- Coherence assessment

---

## 💡 사용 팁

### 권장 워크플로우

#### 📄 단일 논문 작성 (처음부터 작성)
1. `/draft-section` - 섹션별 초안 작성
2. `/citation-help` - 인용 위치 확인
3. `/writing-review` - 정밀 분석
4. `/quick-fix` - 최종 다듬기

#### 📚 리뷰 페이퍼 작성 (여러 논문 통합)
**→ 상세 가이드: [WORKFLOW-synthesis.md](WORKFLOW-synthesis.md)**

1. **Phase 1 - Extract**: 각 논문별로 `/extract-concepts` 실행
2. **Phase 2 - Synthesize**: `/synthesize-intro`로 통합 Introduction 작성
3. **Phase 3 - Refine**: `/writing-review` → `/citation-help` → `/quick-fix`

**적용 시나리오:**
- 큰 PDF 파일 (10MB+)을 단계적으로 처리
- 2-3개 논문을 통합하여 새로운 리뷰 작성
- 체계적인 literature synthesis 필요

#### ✏️ 기존 논문 수정
1. `/quick-fix` - 빠른 정리
2. `/writing-review` - 정밀 분석
3. `/citation-help` - 인용 재확인

#### 🔍 최종 검토
1. `/writing-review` - 전체 흐름 확인
2. `/quick-fix` - 마지막 다듬기

### 각 명령어의 장단점

| 명령어 | 속도 | 깊이 | 용도 |
|--------|------|------|------|
| `/quick-fix` | ⚡⚡⚡ | ⭐ | 빠른 정리 |
| `/writing-review` | ⚡ | ⭐⭐⭐ | 정밀 분석 |
| `/draft-section` | ⚡⚡ | ⭐⭐ | 초안 작성 (단일) |
| `/citation-help` | ⚡⚡ | ⭐⭐ | 인용 확인 |
| `/extract-concepts` | ⚡⚡ | ⭐⭐⭐ | 개념 추출 (긴 논문) |
| `/synthesize-intro` | ⚡ | ⭐⭐⭐ | 다중 논문 통합 |

---

## 📖 핵심 원칙 요약

### Duke Writing Principles

**Lesson 1: Subjects and Actions**
- 동작은 동사에 (명사화 피하기)
- 주어는 명확하게
- 주어와 동사를 가까이

**Lesson 2: Cohesion and Coherence**
- 새 정보는 문장 끝에
- 기존 정보는 문장 시작에
- 수동태는 신중하게 (흐름 개선시에만)

**Lesson 3: Concision**
- 불필요한 단어 제거
- 단순한 단어 선호
- 단순한 주어 사용
- 형용사/부사 절제

### Kording & Mensh Structure

**10 Simple Rules:**
1. 논문당 하나의 핵심 기여
2. 일반 독자를 위해 작성
3. Context-Content-Conclusion 구조
4. 논리적 흐름 최적화
5. Abstract에 완전한 스토리
6. Introduction에서 중요성 전달
7. Results를 논리적 순서로
8. Discussion에서 gap 해결 논의

---

## 🎯 예시: 실제 사용 사례

### 예시 1: Abstract 작성

```
/draft-section

섹션: Abstract
연구 분야: computational biology
주제: Hi-C 데이터를 이용한 3D 게놈 구조 예측
갭: 기존 방법들은 low-resolution 데이터에서 부정확
방법: deep learning 기반 super-resolution
결과: 기존 대비 2배 해상도, 95% 정확도
의의: 저비용으로 고해상도 게놈 구조 연구 가능
```

### 예시 2: 문장 리뷰

**원본:**
```
It should be noted that we performed an extensive analysis of the
methylation patterns and our investigation revealed that there was
a very significant correlation between methylation and expression.
```

`/quick-fix` 결과:
```
We analyzed methylation patterns and found a significant correlation
between methylation and expression.

변화: 28 words → 14 words (50% 감소)
```

`/writing-review` 추가 분석:
- "performed an analysis" → "analyzed" (nominalization)
- "investigation revealed" → "found" (simpler)
- "very significant" → "significant" (remove intensifier)
- "there was" 구문 제거 (더 직접적)

---

## 📚 추가 학습 자료

프로젝트 [/ref](../ref/) 폴더에서 전체 가이드를 확인할 수 있습니다:

1. **Duke Lessons (PDF):**
   - Lesson 1: Subjects and Actions
   - Lesson 2: Cohesion, Coherence, and Emphasis
   - Lesson 3: Concision and Simplicity
   - Revising your Manuscript in 7 Steps

2. **Structure Guide:**
   - Ten Simple Rules for Structuring Papers (Kording & Mensh)
   - Paper_writing_guide.pdf

---

## ⚙️ 고급 사용

### 맞춤 설정

각 명령어의 프롬프트를 수정하여 본인의 작성 스타일에 맞출 수 있습니다:

- **분석 깊이 조절**: `/writing-review.md` 수정
- **섹션 템플릿 추가**: `/draft-section.md`에 custom section 추가
- **자주 쓰는 문구**: `/quick-fix.md`에 field-specific 문구 추가

### 향후 확장 계획

Phase 2 & 3 기능:
- [ ] MCP server로 PDF 자동 로딩
- [ ] 실제 논문 검색 통합 (citation agent)
- [ ] 저널별 스타일 가이드
- [ ] 협업 리뷰 기능
- [ ] Figure caption 생성

---

## 🤝 기여 및 피드백

이 도구들을 사용하면서 개선 사항이 있다면:
1. 특정 use case 공유
2. 추가로 필요한 체크 항목
3. 효과적이었던/아니었던 부분

---

**마지막 업데이트**: 2025-11-04
**버전**: 1.0 (Phase 1 - Revision Agent)
**기반**: Duke Graduate School Scientific Writing Resource + Kording & Mensh (2017)
