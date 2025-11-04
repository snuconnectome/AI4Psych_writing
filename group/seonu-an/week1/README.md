# 학술 논문 작성 Multi-Agent 시스템

심리학 논문 작성을 돕는 7가지 전문 AI Agent 시스템입니다. Google Gemini API를 활용하여 문헌 검색부터 초록 작성, 인용 검증, 문맥 분석, 요약, 시각화, 가독성 평가까지 학술 논문 작성의 전 과정을 지원합니다.

## 📋 구현된 Agent

| Agent | 기능 | 주요 도구 |
|-------|------|----------|
| 📚 **Literature Search** | PubMed 및 arXiv에서 논문 검색 및 CSV 저장 | `search_pubmed()`, `search_arxiv()`, `_extract_pubmed_info()`, `_extract_arxiv_info()` |
| ✍️ **Introduction Writer** | Abstract 기반 Introduction 초안 생성 | `analyze_abstract_structure()`, `generate_introduction_outline()`, `write_introduction_draft()` |
| 📝 **APA 7 Citation Checker** | APA 7판 형식 검증 및 인용-참고문헌 매칭 | `check_citations_in_text()`, `check_reference_format()`, `check_citation_reference_match()` |
| 🔗 **Coherence Checker** | 문맥 및 논리적 흐름 분석 | `check_cohesion()`, `check_comprehension()`, `check_vocabulary()` |
| 📋 **Summarizing** | 핵심 포인트 추출 및 Abstract 생성 | `extract_key_points()`, `generate_abstract()` |
| 📊 **Figure Generation** | APA 형식 준수 연구 그래프 생성 (300 DPI) | `create_bar_chart()`, `create_line_plot()`, `create_scatter_plot()` |
| 👥 **Reader Accessibility** | 대학 신입생 수준 가독성 평가 | `assess_readability_level()`, `identify_jargon()`, `suggest_simplifications()` |

## 🚀 설치 및 실행 방법 (uv 사용)

### 1. 필수 요구사항

- Python 3.10 이상
- [uv](https://github.com/astral-sh/uv) 설치

### 2. 환경 설정

프로젝트 루트 디렉토리에서 다음 명령어를 실행하세요:

```bash
# 프로젝트 루트로 이동
cd "d:\안선우\Winny\한글\5. 서울대학교 석사과정\수업\25-2 AI 심리과학연구방법론\seonu-an"

# uv로 dependencies 설치
uv sync
```

### 3. API 키 설정

`.env` 파일을 프로젝트 루트에 생성하고 다음 내용을 추가하세요:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Jupyter Lab 실행

```bash
# uv 환경에서 Jupyter Lab 실행
uv run jupyter lab
```

또는

```bash
# uv 환경 활성화 후 실행
source .venv/bin/activate  # Linux/Mac
# 또는
.venv\Scripts\activate  # Windows

jupyter lab
```

### 5. 노트북 실행

JupyterLab에서 `HW6/Academic_Writing_Agents_251103.ipynb`를 열고 셀을 순차적으로 실행하세요.

## 📦 설치된 패키지

이 프로젝트는 다음 패키지들을 사용합니다:

```toml
# 핵심 AI/ML
- google-generativeai>=0.8.5 # Google Gemini API (모델: gemini-2.5-flash)

# Jupyter 환경
- jupyterlab>=4.0.0          # Jupyter Lab 인터페이스
- notebook>=7.0.0            # Notebook 환경
- ipykernel>=6.0.0           # Python 커널
- ipywidgets>=8.1.0          # 인터랙티브 UI

# 학술 연구 도구
- biopython                  # PubMed/NCBI Entrez API
- pypdf2>=3.0.0              # PDF 처리 (APA 가이드라인 읽기)

# 데이터 처리 및 분석
- pandas>=2.3.2              # 데이터 처리
- numpy>=1.26.0              # 수치 계산

# 시각화
- matplotlib>=3.8.0          # 그래프 생성
- seaborn>=0.13.0            # 통계적 시각화

# 웹 및 파싱
- requests>=2.31.0           # HTTP 요청 (arXiv API)
- beautifulsoup4>=4.12.0     # HTML 파싱

# 유틸리티
- python-dotenv>=1.1.1       # 환경 변수 관리 (.env 파일)
```

## 🎯 사용 예시

### 1. Literature Search Agent

```python
# PubMed 및 arXiv에서 논문 검색
result = literature_search_agent(
    topic="emotion recognition",
    keywords="large language model cognitive appraisal empathy",
    max_results=50,
    email="student@snu.ac.kr",  # PubMed 필수
    sources=['pubmed', 'arxiv'],
    arxiv_categories=['cs.CL', 'q-bio.NC'],
    exclude_terms=['psychosis', 'neuro*']  # 와일드카드 지원
)
# 결과: literature_search_pubmed_YYYYMMDD_HHMMSS.csv
#       literature_search_arxiv_YYYYMMDD_HHMMSS.csv
```

### 2. Introduction Writer Agent

```python
# Abstract로부터 Introduction 초안 생성
result = introduction_writer_agent(
    abstract=sample_abstract,
    style="formal"
)
# 분석 결과 저장
saved_file = save_result_to_txt(result, "introduction_writer_analysis.txt")
# Introduction 초안 생성 (APA 7 형식 인용 포함)
intro_file = generate_introduction_from_txt(saved_file)
```

### 3. APA 7 Citation Checker Agent

```python
result = apa_citation_checker_agent(
    manuscript_text=sample_text,
    references=sample_references,
    pdf_path="HW6/APA7-Style.pdf"
)
print(result['result'])
```

### 4. Coherence Checker Agent

```python
result = coherence_checker_agent(
    text="Your manuscript text..."
)
# Cohesion, Comprehension, Vocabulary 분석
```

### 5. Summarizing Agent

```python
result = summarizing_agent(
    text="Your full text..."
)
# 핵심 포인트 추출 및 250단어 이내 Abstract 생성
```

### 6. Figure Generation Agent

```python
result = figure_generation_agent(
    data=sample_data,
    figure_type="bar",
    title="Group Comparison",
    x_label="Groups",
    y_label="Mean Score"
)
# 결과: figure_bar.png (300 DPI)
```

### 7. Reader Accessibility Agent

```python
result = reader_accessibility_agent(
    text="Your manuscript text..."
)
# 대학 신입생 수준 가독성 평가 및 개선 제안
```

## 📂 프로젝트 구조

```
seonu-an/
├── HW6/
│   ├── Academic_Writing_Agents_251103.ipynb  # 메인 노트북
│   ├── APA7-Style.pdf                        # APA 7판 가이드 (필수)
│   ├── README.md                             # 이 파일
│   ├── literature_search_*.csv               # 검색된 논문 목록
│   ├── introduction_*.txt                    # 생성된 Introduction 초안
│   ├── figure_*.png                          # 생성된 그래프 (300 DPI)
│   └── paper_review_report.txt               # 종합 리포트
├── pyproject.toml                            # 프로젝트 설정 및 dependencies
├── .env                                      # API 키 (생성 필요)
└── uv.lock                                   # uv 잠금 파일
```

## 🔧 문제 해결

### uv sync 실패 시

```bash
# uv 업데이트
pip install --upgrade uv

# 캐시 삭제 후 재시도
uv cache clean
uv sync
```

### Jupyter Lab이 실행되지 않을 때

```bash
# 커널 설치 확인
uv run python -m ipykernel install --user --name=seonu-an

# Jupyter Lab 재시작
uv run jupyter lab --no-browser
```

### PubMed API 오류

PubMed API 사용 시 이메일 주소가 필수입니다. NCBI 정책에 따라 `Entrez.email`을 반드시 설정해야 합니다.

```python
# 올바른 사용 예시
result = literature_search_agent(
    topic="your topic",
    keywords="your keywords",
    email="your_email@example.com"  # 필수!
)
```

### API Rate Limiting

PubMed API는 0.5초 간격으로 요청을 보내도록 제한되어 있습니다. 대량 검색 시 시간이 소요될 수 있습니다.

## 💡 주요 기능

### 1. 전문 학술 검색 (PubMed & arXiv)
- **PubMed**: Biopython의 Entrez 모듈을 통한 전문적인 의학/생물학 논문 검색
  - PMID, DOI, MeSH 키워드 자동 추출
  - 배치 처리: 10편씩 효율적 검색
  - 실시간 진행상황 표시
- **arXiv**: Computer Science, Neuroscience 등 카테고리별 검색
  - 카테고리 필터링 지원 (cs.CL, q-bio.NC 등)
- 와일드카드 제외 기능: `neuro*`로 neuro 접두사 포함 모든 용어 제외
- CSV 저장: UTF-8-sig 인코딩으로 Excel 호환

### 2. Introduction 자동 생성
- Abstract 구조 분석 (연구 목적, 방법, 결과, 의의)
- 체계적인 Introduction 개요 생성
- APA 7 형식 인용이 포함된 초안 작성
- 템플릿 형식으로 제공 (대괄호 섹션은 수동 작성 필요)

### 3. APA 7판 형식 검증
- PDF에서 APA 가이드라인 자동 추출
- 본문 인용 형식 확인 (예: Smith, 2020; Smith & Jones, 2020; Smith et al., 2020)
- 참고문헌 형식 검증
- 인용-참고문헌 매칭 확인

### 4. 문맥 및 논리성 분석
- **Cohesion**: 전환어(transition words)를 통한 논리적 연결성 평가
- **Comprehension**: 가독성 지표 분석
- **Vocabulary**: 어휘 선택 및 다양성 평가

### 5. 지능형 요약
- 핵심 논점 자동 추출
- 250단어 이내 간결한 Abstract 생성
- 연구의 주요 의도 파악

### 6. 고품질 시각화
- Bar chart, Line plot, Scatter plot 생성
- APA 형식 완벽 준수
- 300 DPI 고해상도 PNG 출력
- Seaborn 스타일 적용

### 7. 가독성 접근성 평가
- 대학 신입생 수준 기준 난이도 평가
- 전문 용어(jargon) 자동 식별
- 구체적인 단순화 제안 제공

## 📊 출력 파일

실행 후 다음 파일들이 생성됩니다:

### CSV 파일
- `literature_search_pubmed_YYYYMMDD_HHMMSS.csv`: PubMed 검색 결과 (PMID, DOI, MeSH 포함)
- `literature_search_arxiv_YYYYMMDD_HHMMSS.csv`: arXiv 검색 결과

### 텍스트 파일
- `introduction_writer_analysis.txt`: Abstract 구조 분석 결과
- `introduction_draft_YYYYMMDD_HHMMSS.txt`: APA 7 형식 인용이 포함된 Introduction 초안
- `paper_review_report.txt`: 종합 분석 리포트

### 이미지 파일 (300 DPI)
- `figure_bar.png`: Bar 차트
- `figure_line.png`: Line 플롯
- `figure_scatter.png`: Scatter 플롯

## 🤝 기여

버그 리포트나 기능 제안은 이슈로 등록해주세요.

## 🔑 API 및 기술 스택

### AI Model
- **Google Gemini API** (`gemini-2.5-flash`)
  - Function calling 기능 활용
  - Multi-turn 대화 (agent당 3-5회 반복)
  - Unified LLM client wrapper

### 데이터 소스 API
- **PubMed/NCBI E-utilities API**
  - Biopython의 `Bio.Entrez` 모듈 사용
  - 이메일 필수 (NCBI 정책)
  - Rate limiting: 0.5초 간격
- **arXiv API**
  - 인증 불필요
  - 카테고리 기반 필터링

## ⚠️ 주의사항

1. **환경 설정**
   - `.env` 파일에 `GEMINI_API_KEY` 필수
   - `load_dotenv()`로 환경 변수 로드 확인

2. **PubMed 검색**
   - 이메일 주소 필수 (NCBI 정책)
   - API rate limiting으로 대량 검색 시 시간 소요

3. **파일 인코딩**
   - CSV: UTF-8-sig (Excel 호환)
   - TXT: UTF-8
   - 타임스탬프: YYYYMMDD_HHMMSS 형식

4. **APA Citation Checker**
   - `HW6/APA7-Style.pdf` 파일 필수

5. **Introduction Writer**
   - 생성된 초안은 템플릿
   - 대괄호 섹션은 수동 작성 필요
   - 문헌 검색 결과를 기반으로 인용 추가 권장

6. **시각화**
   - 모든 그래프: 300 DPI, tight bounding box
   - Matplotlib + Seaborn 스타일

## 📝 라이선스

교육 목적으로 자유롭게 사용 가능합니다.

## 👨‍💻 개발 정보

- **Gemini Model**: `gemini-2.5-flash`
- **Python Version**: 3.10+
- **Package Manager**: uv
- **Notebook**: Academic_Writing_Agents_251103.ipynb
