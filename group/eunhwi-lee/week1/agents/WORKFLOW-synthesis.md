# Workflow: Synthesizing Review Paper Introduction from Multiple Papers

**목표**: 여러 기존 논문(특히 큰 PDF 파일)에서 핵심 내용을 추출하여 새로운 리뷰 페이퍼의 Introduction을 작성

**대상 시나리오**:
- PDF 파일이 커서 한 번에 업로드/분석이 어려운 경우
- 2-3개 이상의 논문을 통합하여 새로운 리뷰를 작성하는 경우
- 체계적인 단계별 작업이 필요한 경우

---

## 📋 전체 워크플로우 Overview

```
Phase 1: Extract        Phase 2: Synthesize      Phase 3: Refine
  (개별 처리)              (통합)                   (다듬기)

PDF 1 → Extract          Concept Maps     →      Draft Intro
PDF 2 → Extract              ↓                        ↓
                         Synthesize              Review/Fix
                                                      ↓
                                                  Citations
```

---

## Phase 1: Concept Extraction (개념 추출)

### Step 1.1: PDF 텍스트 준비

**방법 A - 수동 복사** (권장, 가장 안정적):
1. PDF를 열기 (Preview, Adobe Reader 등)
2. 핵심 섹션 텍스트 복사:
   - **필수**: Abstract, Introduction (전체)
   - **선택**: Results (main findings), Discussion (처음/마지막 부분)
3. 텍스트 파일로 저장:
   ```
   review-paper/extracts/Q1-text.txt
   review-paper/extracts/Q2-text.txt
   ```

**방법 B - PDF to Text 변환**:
```bash
# macOS에서 pdftotext 사용
brew install poppler
pdftotext review-paper/PhD_Qual_Q1_final.pdf review-paper/extracts/Q1-text.txt
pdftotext review-paper/PhD_Qual_Q2_final.pdf review-paper/extracts/Q2-text.txt
```

**방법 C - 섹션별 부분 추출**:
- Introduction만 필요한 경우, 해당 페이지만 선택적으로 복사

### Step 1.2: Concept Extraction 실행

각 논문에 대해 개별적으로 실행:

**Paper 1 (Q1 - Addiction + RLDM):**
```
/extract-concepts

[Q1 텍스트 붙여넣기 - Introduction 섹션 위주]

Focus areas:
- Reinforcement learning models in addiction
- Computational mechanisms
- Decision-making paradigms
- Key RLDM parameters (learning rate, discount factor, etc.)

Target use: For introduction synthesis
```

**Paper 2 (Q2 - Addiction + TMS/tDCS):**
```
/extract-concepts

[Q2 텍스트 붙여넣기 - Introduction 섹션 위주]

Focus areas:
- Non-invasive brain stimulation techniques
- Target brain regions for addiction
- TMS/tDCS mechanisms and effects
- Clinical outcomes

Target use: For introduction synthesis
```

### Step 1.3: Extraction 결과 저장

각 extraction 결과를 파일로 저장:
```
review-paper/extracts/Q1-concepts.md
review-paper/extracts/Q2-concepts.md
```

**저장할 핵심 내용**:
- Key Concepts 섹션 전체
- Terminology Dictionary
- Synthesis Readiness 섹션
- Quick Reference for Introduction

---

## Phase 2: Introduction Synthesis (통합 작성)

### Step 2.1: Synthesis 준비

추출된 개념들을 검토하고 통합 전략 수립:

**체크리스트**:
- [ ] Paper 1의 핵심 프레임워크 파악
- [ ] Paper 2의 핵심 프레임워크 파악
- [ ] 공통 개념 (overlapping) 찾기
- [ ] 보완 개념 (complementary) 찾기
- [ ] 브릿지 개념 (bridging) 구상

**통합 맵 작성** (수동으로 정리):
```
공통 개념:
- Addiction as disorder of [X]
- Brain circuits: [regions from both papers]

Paper 1 기여:
- Computational mechanisms: [list]
- RLDM framework: [details]

Paper 2 기여:
- NIBS techniques: [list]
- Intervention mechanisms: [details]

브릿지 개념:
- Computational targets for brain stimulation
- Circuit-based understanding → intervention
```

### Step 2.2: Synthesize Introduction 실행

```
/synthesize-intro

New review topic:
Integrating computational and brain stimulation approaches to addiction:
A synthesis of reinforcement learning and decision-making (RLDM) mechanisms
with non-invasive brain stimulation (NIBS) interventions

Source materials:

=== PAPER 1: Addiction + RLDM ===
[Q1-concepts.md의 "Quick Reference for Introduction" 섹션 붙여넣기]

Key frameworks:
- [추출된 프레임워크들]

Key constructs:
- [추출된 constructs]

Main gap identified:
- [Q1에서 식별한 gap]

=== PAPER 2: Addiction + TMS/tDCS ===
[Q2-concepts.md의 "Quick Reference for Introduction" 섹션 붙여넣기]

Key frameworks:
- [추출된 프레임워크들]

Key constructs:
- [추출된 constructs]

Main gap identified:
- [Q2에서 식별한 gap]

=== NEW SYNTHESIS GAP ===
The intersection of computational understanding (RLDM) and intervention
methods (NIBS) has not been systematically integrated. This review aims
to synthesize these perspectives to identify:
1. Computational targets for brain stimulation
2. How NIBS affects RLDM parameters
3. Circuit-level mechanisms linking computation and intervention

Target audience: Computational psychiatry and clinical neuroscience researchers

Specific focus:
- RLDM mechanisms in addiction
- NIBS effects on decision-making circuits
- Translational implications for treatment
```

### Step 2.3: Draft 결과 저장

```
review-paper/drafts/intro-v1.md
```

저장할 내용:
- Full introduction draft
- Integration notes
- Citation strategy

---

## Phase 3: Refinement (다듬기)

### Step 3.1: Structure & Flow Review

Draft를 `/writing-review`로 분석:

```
/writing-review

[intro-v1.md 전체 붙여넣기]
```

**검토 항목**:
- Funnel 구조 (broad → narrow → gap) 제대로 되어있나?
- 문단 간 coherence
- Subject-verb clarity
- Nominalization 제거
- Concision

결과를 바탕으로 수정:
```
review-paper/drafts/intro-v2.md
```

### Step 3.2: Quick Fixes

구체적인 문장 수정:

```
/quick-fix

[수정이 필요한 특정 문단들 붙여넣기]
```

### Step 3.3: Citation Strategy

```
/citation-help

[intro-v2.md 붙여넣기]
```

**출력**:
- 어디에 citation이 필요한지
- 어떤 타입의 reference가 필요한지 (original study, review, method paper 등)

결과를 바탕으로:
```
review-paper/drafts/intro-v3-with-citations.md
```

### Step 3.4: Final Polish

1. **Terminology 일관성 체크**:
   - Q1과 Q2에서 다르게 쓰인 용어가 있나?
   - 통일된 용어로 수정

2. **Transition 강화**:
   - 문단 간 연결이 자연스러운가?
   - 필요시 transition 문장 추가

3. **Gap 명확성**:
   - 새로운 synthesis가 제공하는 가치가 명확한가?
   - Gap이 구체적으로 표현되었나?

4. **Length 체크**:
   - 리뷰 페이퍼 intro 적정 길이: 4-6 페이지 (double-spaced)
   - 너무 길면 `/quick-fix`로 압축

---

## 📁 폴더 구조 (권장)

```
review-paper/
├── PhD_Qual_Q1_final.pdf
├── PhD_Qual_Q2_final.pdf
├── extracts/
│   ├── Q1-text.txt              # 추출한 원본 텍스트
│   ├── Q2-text.txt
│   ├── Q1-concepts.md           # /extract-concepts 결과
│   ├── Q2-concepts.md
│   └── synthesis-map.md         # 통합 전략 메모
├── drafts/
│   ├── intro-v1.md              # /synthesize-intro 결과
│   ├── intro-v2.md              # /writing-review 후 수정
│   ├── intro-v3-with-citations.md
│   └── intro-final.md
└── notes/
    ├── terminology.md           # 용어 정리
    └── citation-list.md         # 필요한 citation 리스트
```

---

## ⏱️ 예상 소요 시간

| Phase | Task | Time |
|-------|------|------|
| Phase 1 | PDF 텍스트 준비 | 15-30분 |
| Phase 1 | Extract concepts (Q1) | 5-10분 |
| Phase 1 | Extract concepts (Q2) | 5-10분 |
| Phase 2 | Synthesis 준비 | 10-15분 |
| Phase 2 | Synthesize intro | 10-15분 |
| Phase 3 | Writing review | 5-10분 |
| Phase 3 | Citation help | 5분 |
| Phase 3 | Final polish | 15-30분 |
| **Total** | | **90-135분 (1.5-2시간)** |

---

## 💡 Tips & Best Practices

### Extraction Phase
- **한 번에 너무 많이 하지 말기**: 섹션별로 나눠서 extract
- **핵심만 집중**: Introduction과 Discussion이 가장 중요
- **용어 정리**: 같은 개념을 다르게 표현한 경우 메모

### Synthesis Phase
- **Integration, not compilation**: 두 논문을 단순 나열하지 말고 융합
- **New gap이 핵심**: 두 논문 각각의 gap이 아니라 교집합의 gap
- **Specific examples**: 추상적인 설명보다 구체적인 예시

### Refinement Phase
- **여러 번 iterate**: 한 번에 완벽하게 하려고 하지 말기
- **소리 내서 읽기**: Flow 확인하는 최고의 방법
- **Peer feedback**: 가능하면 동료에게 읽어달라고 요청

---

## 🚨 자주 발생하는 문제 & 해결

### Problem 1: PDF가 너무 커서 에러
**해결**:
- 섹션별로 나눠서 처리
- Introduction만 먼저 extract
- 필요시 이미지/table 제외하고 텍스트만 추출

### Problem 2: 두 논문의 용어가 달라서 혼란
**해결**:
- `extracts/terminology.md` 파일에 매핑 정리
- `/synthesize-intro`에서 명시적으로 용어 통일 요청

### Problem 3: Intro가 너무 길어짐
**해결**:
- 각 논문에서 정말 핵심만 가져오기
- `/quick-fix`로 20% 압축
- 일부 내용은 Background/Methods로 이동

### Problem 4: Gap이 명확하지 않음
**해결**:
- 각 논문의 gap을 명확히 이해하기
- "Why does integration matter?" 질문에 답하기
- Specific research questions 제시

---

## 📝 Example Scenario

**당신의 케이스**: Addiction + NIBS + RLDM

### Phase 1 Output 예시:

**Q1 핵심 개념**:
- RL parameters: learning rate, discount factor
- Model-based vs model-free learning
- Value-based decision making
- Reward prediction error

**Q2 핵심 개념**:
- TMS types: rTMS, iTBS, cTBS
- tDCS: anodal, cathodal
- Target regions: DLPFC, ACC, striatum
- Neuromodulation mechanisms

### Phase 2 Output 예시:

**Synthesis gap**:
"While computational models identify specific parameters altered in addiction (Q1) and brain stimulation can modulate neural circuits (Q2), we lack a systematic understanding of how NIBS affects computational parameters and which parameters should be targeted for optimal intervention."

**Integration example**:
- DLPFC stimulation → affects model-based learning
- Striatal modulation → changes learning rate
- ACC targeting → modifies conflict monitoring

### Phase 3 Output:

Clean, concise intro with:
- Broad: Addiction as computational disorder
- Narrow: RLDM mechanisms + NIBS techniques
- Gap: Lack of integration
- Scope: This review synthesizes...

---

## ✅ Final Checklist

Before considering your intro complete:

- [ ] Funnel structure clearly evident
- [ ] Both source papers adequately represented
- [ ] Synthesis creates something new (not just summary)
- [ ] Gap is specific and compelling
- [ ] Scope is clearly defined
- [ ] Terminology is consistent
- [ ] Citations appropriately placed
- [ ] Length appropriate (4-6 pages)
- [ ] Transitions are smooth
- [ ] Writing is concise (no nominalization, clear subjects/verbs)

---

**마지막 업데이트**: 2025-11-04
**관련 명령어**: `/extract-concepts`, `/synthesize-intro`, `/writing-review`, `/citation-help`, `/quick-fix`
