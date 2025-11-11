# 심리과학 연구방법 - 롸이팅 (Psychology Research Writing Course)

## 📚 Course Overview

6주 집중 대학원 논문 작성 과정 (심리학과 석사/박사)
- **대상**: 심리학과 대학원생 (석사/박사)
- **목표**: "어떻게 하면 탑티어 저널에 출불할 만한 탑 5%의 논문을 쓸 것인가"
- **구조**: IMRaD format (Introduction, Methods, Results, and Discussion)
- **AI 도구**: ChatGPT, Claude, Perplexity, Elicit

## 🎯 Ultimate Learning Goal

**"어떻게 하면 탑티어 저널에 출판할 만한 탑 5%의 논문을 쓸 것인가"**

이 목표를 달성하기 위해:
- AI 툴을 적극적으로 사용
- 각자의 레시피를 공유
- 결과를 공유하고 서로 피드백
- 개념 설명보다는 실전 전략에 집중

## ⚠️ CRITICAL CONTEXT: Week 2-4 Revision Principle

**윤경생 박사님의 AI 개념 강의와 중복 제거**

학생들은 윤경생 박사님 강의에서 이미 다음을 학습했습니다:
- Prompt Engineering 기초 (Instruction, Context, Input, Output)
- Parameters (Temperature, Top-k, Top-p)
- In-context Learning (zero-shot, one-shot, few-shot)
- RAG (Retrieval-Augmented Generation)
- Chain-of-Thought (CoT) prompting
- RLHF, Multimodal models

따라서 Week 2-4는 **개념 설명을 완전히 제거**하고 **실전 전략에만 집중**:

| Week | 변경 전 | 변경 후 |
|------|---------|---------|
| Week 2 | 프롬프트 엔지니어링 기초 | Nature/Science 초록 전략 |
| Week 3 | RAG 개념 설명 | 체계적 Gap 발견 워크플로우 |
| Week 4 | CoT 개념 설명 | Methods/Results Bulletproofing |

## 📁 File Structure

```
.
├── CLAUDE.md                           # This file
├── 강의계획.md                         # Overall course structure
├── overlap_analysis.md                 # Analysis of overlap with 윤경생's lectures
│
├── claudedocs/                         # Strategy documents (for instructors)
│   ├── comprehensive_revision_plan.md  # Master implementation plan
│   ├── week2_revision_strategy.md      # Nature/Science abstract strategies
│   ├── week3_revision_strategy.md      # Gap discovery workflows
│   ├── week4_revision_strategy.md      # Methods/Results bulletproofing
│   └── figma_workshop_weeks2-6.md      # Figma AI workshop strategies (Week 2-6)
│
├── week1/                              # Human-centered writing (no AI)
│   ├── lecture_notes.md                # Original detailed notes (reference)
│   ├── lesson_notes_compressed_90min.md # Compressed slides: 62→23 (90min workshop)
│   ├── workshop_materials.md           # Bad Sentences + Bad Paragraphs + Smart Revising (Figma integrated)
│   ├── bad_paragraphs_real_papers.md   # 4 real PLOS ONE/MDPI paragraphs with before/after analysis
│   ├── teaching_guide_90min.md         # Minute-by-minute teaching guide (Figma facilitation)
│   ├── figma_workshop_guide.md         # Figma workshop comprehensive guide
│   ├── NOTION_WORKSHOP_DESIGN.md       # Notion workspace design specification (Week 2-6)
│   ├── create_notion_workshop_simple.py # Working automation script ✅
│   └── create_notion_workshop_week2_6.py # Full-featured script (reference)
│
├── week2/                              # AI 활용 I - 초록
│   ├── lecture_notes.md                # Nature/Science abstract strategies (1421 lines, 69KB)
│   ├── lesson_slides_15min.md          # Marp slides with real Nature/Science examples
│   ├── peer_feedback_session_plan.md   # Complete workshop design (2000+ lines)
│   ├── selected_papers.md              # 3 Nature/Science abstract pairs (A, B, C)
│   └── upload_lecture_notes.py         # Notion upload script using notion-client ✅
│
├── week3/                              # AI 활용 II - 문헌 리뷰
│   └── lecture_notes.md                # Systematic gap discovery (553 lines)
│
├── week4/                              # AI 활용 III - 방법/결과
│   └── lecture_notes.md                # Methods/Results bulletproofing (718 lines)
│
├── week5/                              # Discussion section
│   └── lecture_notes.md
│
├── week6/                              # Peer review & revision
│   └── lecture_notes.md
│
└── 윤경생슬라이드/                     # Dr. Yoon's AI concept lectures
    ├── 1주차.pdf
    ├── 2주차.pdf                       # 68-page Prompt Engineering lecture
    └── 3주차.pdf
```

## 📖 Weekly Structure

### Week 1: Human-Centered Writing (no AI)
**90-Minute Figma Workshop Model** (62 slides → 23 slides, 63% compression)

**Structure**:
- Lecture: 35 min (23 slides) - 10 core principles
- **Figma Workshop: 50 min (56%)** - Real-time collaborative practice
- Wrap-up: 5 min - Q&A, assignment

**10 Core Principles**:
1. **Lesson 1** (주어-동사): Actions in verbs, subjects as subjects, keep them close
2. **Lesson 2** (응집성): Old→New flow, strategic passive, paragraph coherence
3. **Lesson 3** (간결성): Remove unnecessary words, simple language, simple subjects, limit modifiers

**Figma Workshop Components**:
- **Stage 1A** (15min): Bad Sentences 수술실 - 10 sentences on shared canvas
  - Individual work with Sticky Notes
  - Real-time peer review with comments
  - Instructor live feedback
- **Stage 1B** (15min): Bad Paragraphs from Real Papers - 4 paragraphs from actual PLOS ONE 2024 paper
  - Students select 2 of 4 paragraphs to analyze
  - Paragraph-level analysis (Old→New flow, coherence)
  - Real-world application of Week 1 principles
- **Stage 2** (20min): Smart Revising with 7-step checklist
  - Personal work zones for each student
  - Peer feedback through Figma comments
  - Live progress monitoring

**Why Figma?**:
- ✅ Real-time collaboration - see everyone's work simultaneously
- ✅ Instant feedback - comments and reactions in real-time
- ✅ Visual learning - compare good/bad examples side-by-side
- ✅ Persistent record - workshop results saved for future reference

**Materials**:
- `lesson_notes_compressed_90min.md`: 23 slides with core concepts + best examples
- `workshop_materials.md`: Practice materials with Figma instructions (now includes Bad Paragraphs)
- `bad_paragraphs_real_papers.md`: 4 real paper paragraphs with detailed analysis
- `teaching_guide_90min.md`: Minute-by-minute guide with Figma facilitation
- `figma_workshop_guide.md`: Comprehensive Figma setup and operation guide

### Week 2: 초록 쓰기 워크샵 (AI 활용 I)
**NO PROMPT ENGINEERING BASICS** (students already learned from 윤경생)

Focus areas:
- Top-tier abstract differentiation (Nature/Science vs general journals)
- 4 opening patterns (Problem/Gap/Opportunity/Challenge-driven)
- Broad significance framing
- Quantitative result presentation
- 40+ AI prompt recipes for abstract writing

### Week 3: AI 활용 II - 체계적 Research Gap 발견
**NO RAG CONCEPT EXPLANATIONS** (students already learned from 윤경생)

Focus areas:
- Gap classification (Conceptual vs Incremental)
- 3-stage gap validation workflow
- False gap prevention strategies
- Cross-disciplinary connection mining
- 30+ AI prompt recipes for gap discovery

### Week 4: AI 활용 III - Methods/Results Bulletproofing
**NO COT CONCEPT EXPLANATIONS** (students already learned from 윤경생)

Focus areas:
- Top 10 rejection reasons for Methods/Results
- Reproducibility checklist (6 critical elements)
- Control validation strategies
- Overclaiming prevention
- Statistical rigor verification
- 40+ AI prompt recipes for bulletproofing

### Week 5-6: Discussion, Peer Review, Revision
- Discussion section strategies
- Structured peer review protocols
- Iterative improvement workflows

## 🎓 Teaching Philosophy

### Core Principle: Learn by Writing

**"Write Every Week, Improve in Class, Apply Immediately"**

학생들은 자신의 실제 논문을 매주 조금씩 작성하며 배웁니다:
- **Week 1**: 초록 작성 + Week 1 원칙 적용
- **Week 2**: 초록을 Nature/Science급으로 개선 (AI 활용)
- **Week 3**: Literature review 작성 + Gap discovery
- **Week 4**: Methods/Results 작성 + Bulletproofing
- **Week 5-6**: Discussion, Peer review, Final polish

### NO Flipped Classroom

이 과정은 flipped classroom을 **사용하지 않습니다**:
- ❌ Pre-class videos, readings, Google Forms
- ❌ 사전학습 60-90분 요구
- ✅ 수업 전 준비: 자신의 논문 섹션 작성 (매주 과제)
- ✅ 수업 시간: 가져온 글을 workshop에서 개선

**Why?**
- 대학원생들은 이미 바쁨 - 사전학습 부담 최소화
- 실제 논문으로 배우는 게 가장 효과적
- Workshop에서 즉각적 피드백과 개선이 핵심

### 90-Minute Class Structure

**Week 1** (기초 원칙 교육):
- **강의 35분**: 10 core writing principles
  - IMRaD 오리엔테이션 (5분)
  - 핵심 원칙 강의 (30분)
- **Workshop 50분**: Figma collaborative practice
  - Bad Sentences (15분)
  - Bad Paragraphs (15분)
  - Smart Revising (20분)
- **Wrap-up 5분**: Q&A + 과제 안내
- **과제**: 초록을 7-step checklist로 수정

**Week 2-6** (AI-Enhanced Workshop):
- **짧은 강의 15-20분**: Top-tier strategies + AI recipes
  - 주요 전략 소개 (10-15분)
  - 프롬프트 레시피 시연 (5분)
- **Workshop/Discussion 70-75분**:
  - AI로 자신의 글 개선 (30-40분)
  - Peer feedback & discussion (20-30분)
  - Recipe sharing & 모범 사례 (10-20분)
- **과제**: 다음 섹션 작성

**Key Ratio**:
- Week 1: 40% lecture / 60% workshop
- Week 2-6: 20% lecture / 80% workshop/discussion

### Recipe Sharing Culture
- Students share their successful AI prompts
- Build a collective knowledge base
- Learn from each other's workflows
- Iterate and improve recipes together

### Structured Peer Review
- Use provided templates (in lecture notes)
- Focus on top-tier journal criteria
- Constructive feedback protocols
- Evidence-based suggestions

## 🎨 Figma Interactive Workshops

### Overview
All workshops (Week 1-6) use **Figma real-time collaborative canvas** for interactive, engaging learning experiences.

### Why Figma Across All Weeks?
- **Real-time Collaboration**: All students see each other's work simultaneously
- **Instant Feedback**: Comments, reactions, and instructor guidance in real-time
- **Visual Learning**: Side-by-side comparison of approaches and results
- **Persistent Record**: Workshop results archived for future reference
- **Scalable**: Works for 6-50 students equally well

### Week 1: Human-Centered Writing Workshop
**Canvas Structure**:
- Left Panel: Writing principles reference (read-only)
- Right Area: Bad Sentences + Smart Revising work zones
- Student work with Sticky Notes
- Real-time peer review with comments

**Key Features**:
- Individual Sticky Notes for problem identification
- Collaborative peer feedback
- Live instructor curation
- Model answers revealed progressively

### Week 2-6: AI-Enhanced Workshops
**Canvas Structure**:
- Left Panel: Strategy reference + evaluation criteria + example prompts
- Right Area: Individual student experiment zones
- Recipe library section (accumulates over weeks)

**3-Stage Process**:
1. **Individual Experimentation** (10min): Students test AI prompts, record Input-Prompt-Output in their zones
2. **Peer Review** (10min): Students evaluate each other's results using criteria, provide feedback via comments
3. **Collective Curation** (10min): Instructor highlights best recipes, adds to recipe library

**Week-Specific Adaptations**:
- **Week 2**: Opening strategy experiments, significance framing
- **Week 3**: Gap discovery validation, 3-stage workflow
- **Week 4**: Red Team/Blue Team bulletproofing game
- **Week 5**: Discussion section construction
- **Week 6**: Round-robin comprehensive peer review

### Recipe Library (Cumulative)
A persistent section in Figma that grows each week:
```
Week 2 Best Recipes:
• Problem-Driven Opening (학생C, 4.8/5)
• Quantitative Result Emphasis (학생A, 4.6/5)

Week 3 Best Recipes:
• Conceptual Gap Discovery (학생B, 4.9/5)
• 3-Stage Validation (학생D, 4.7/5)

[Continues Week 4-6...]
```

### Instructor Facilitation
**Real-time Monitoring**:
- Watch all student zones simultaneously
- Instant feedback via comments
- Highlight good examples with @mentions
- Guide struggling students with hints

**Quality Curation**:
- React to good work with emojis/comments
- Share exceptional examples with @everyone
- Build recipe library from best contributions
- Export to PDF after each session

### Setup Requirements
**Before Class** (10 minutes prior):
1. Copy Figma template for the week
2. Adjust student work zones (6-12 typical)
3. Generate sharing link with edit permissions
4. Send link to students via email/messaging

**Class Start** (5 minutes):
1. Confirm all students connected
2. Quick Figma tour (N key for notes, C key for comments)
3. Show canvas structure
4. Begin lecture

### Technical Notes
- **No app installation required**: Works in any browser
- **Auto-save**: No manual saving needed
- **Concurrent editing**: Figma handles conflicts automatically
- **Export options**: PDF, images, or keep in Figma permanently

### Files
- `week1/figma_workshop_guide.md`: Week 1 complete guide with canvas layouts, scripts, troubleshooting
- `claudedocs/figma_workshop_weeks2-6.md`: Week 2-6 strategies, AI experiment structures, recipe library system

## 📱 Notion Interactive Workshops (Week 2-6)

### Overview
Week 2-6 workshops have been implemented in **Notion** for persistent, structured AI experimentation with built-in database tracking.

### Why Notion for Week 2-6?
- **API-Driven Setup**: Automated workspace generation using Python scripts
- **Database Integration**: Student submissions and AI recipe tracking in linked databases
- **Template Buttons**: Quick student workspace duplication for each workshop
- **Familiar Interface**: Most students already use Notion
- **Persistent Memory**: Recipe library accumulates across weeks
- **Search & Filter**: Easy access to past experiments and successful recipes

### Implementation Status ✅

**Successfully Created** (2025-01-02):
- ✅ **Student Submissions Database** (`29f41454-561d-811d-9253-eed62e257c47`)
  - Properties: Name, 학생, Week, Section, Status, Peer Score, Peer Feedback
  - Tracks all student work across Week 2-6

- ✅ **AI Recipe Library Database** (`29f41454-561d-8129-8620-c67cc0aa62d9`)
  - Properties: Recipe Name, Week, Category, Prompt, Success Rate, Submitted By
  - Collective knowledge base that grows each week

- ✅ **5 Workshop Pages** (Week 2-6)
  - Week 2: 초록 쓰기 워크샵 (`29f41454-561d-8172-a4e9-d63c7eee0f0a`)
  - Week 3: 체계적 Research Gap 발견 (`29f41454-561d-817c-842d-f653dac8b2cd`)
  - Week 4: Methods/Results Bulletproofing (`29f41454-561d-818e-acd5-eb56e0bb807a`)
  - Week 5: Discussion Section (`29f41454-561d-8121-ad35-fdf8e5536a6b`)
  - Week 6: Final Polish & Peer Review (`29f41454-561d-81df-ac5e-cbf9f0a50160`)

**Parent Page**: `심리과학 연구방법-롸이팅` (`29f41454-561d-80ec-9fde-d005c16efcaf`)

### Workspace Structure

```
📚 뇌데사 2025
│
├─ 📊 Student Submissions Database
│  └─ Filters by Week, Status, Student
│
├─ 🧪 AI Recipe Library Database
│  └─ Filters by Week, Category, Success Rate
│
├─ 📅 Week 2: 초록 쓰기 워크샵
│  ├─ 📖 강의 자료 (전략 + 평가 기준)
│  ├─ 💡 예시 프롬프트 레시피
│  ├─ 🧪 학생 실험 영역 (Template Button)
│  └─ 📊 Student Submissions (Linked DB)
│
├─ 📅 Week 3: 체계적 Research Gap 발견
│  ├─ 📖 Gap 유형 분류
│  ├─ 💡 3-Stage Validation 레시피
│  ├─ 🧪 Gap Discovery Canvas
│  └─ 📊 Student Submissions
│
├─ 📅 Week 4: Methods/Results Bulletproofing
│  ├─ 📖 Reproducibility Checklist
│  ├─ 💡 Red Team/Blue Team 레시피
│  ├─ 🧪 Bulletproofing Workspace
│  └─ 📊 Student Submissions
│
├─ 📅 Week 5: Discussion Section
│  └─ [Similar structure]
│
└─ 📅 Week 6: Final Polish & Peer Review
   └─ [Similar structure]
```

### Automation Scripts

**Primary Script** (Simplified, Working):
- `week1/create_notion_workshop_simple.py`
- Creates databases + week pages with basic structure
- Successfully executed on 2025-01-02
- Usage: `python create_notion_workshop_simple.py <parent_page_id>`

**Full Script** (Complex, Reference):
- `week1/create_notion_workshop_week2_6.py`
- Attempted full content generation with detailed blocks
- Encountered Notion API limitations with complex nested blocks
- Kept as reference for understanding full vision

**Markdown Upload Script** ✅ (2025-01-04):
- `week2/upload_lecture_notes.py`
- Uploads markdown files to Notion pages using notion-client
- Successfully uploaded 617 blocks (1421 lines, 69KB) in 7 batches
- Converts markdown → Notion blocks (headings, lists, code, tables, quotes)
- Usage: `python upload_lecture_notes.py <page_id>`
- Example: https://notion.so/2a141454561d8077b956df19394fcf24

**Design Document**:
- `week1/NOTION_WORKSHOP_DESIGN.md`
- Complete specification of databases, properties, views, templates
- Includes API limitations and manual setup requirements

### 🔧 Notion Upload Best Practice

**ALWAYS use notion-client Python library for Notion uploads**

When uploading files or content to Notion:
- ❌ **DO NOT** suggest manual copy-paste first
- ❌ **DO NOT** suggest Notion's import feature first
- ✅ **ALWAYS** write Python script using notion-client library

**Why notion-client First:**
1. **Automation**: Repeatable, scriptable, version-controlled
2. **Batch Processing**: Handles 100-block API limit automatically
3. **Format Conversion**: Programmatic markdown → Notion blocks
4. **Error Handling**: Retry logic and detailed error messages
5. **Speed**: < 2 minutes for 69KB file (vs manual copy-paste)

**Implementation Pattern:**
```python
from notion_client import Client
import os

# Initialize
notion = Client(auth=os.getenv('NOTION_TOKEN'))

# Upload blocks (max 100 per request)
notion.blocks.children.append(block_id=page_id, children=blocks)
```

**Environment Setup:**
```bash
export NOTION_TOKEN='your_notion_integration_token'
pip install notion-client
```

**Working Example:**
- See `week2/upload_lecture_notes.py` for complete implementation
- Parses markdown, batches blocks, handles tables/code/lists
- Successfully tested with 1421-line lecture notes (2025-01-04)

**Fallback Only When:**
- User explicitly requests manual method
- NOTION_TOKEN not available or setup not possible
- Simple content that's faster to copy-paste (<100 words)

### Manual Setup Required ⚠️

The automation scripts created the basic infrastructure. These steps need to be completed manually in Notion:

1. **Add Detailed Content to Week Pages** (~30min per week):
   - Copy strategies from `weekN/lecture_notes.md`
   - Add evaluation criteria as callout blocks
   - Insert example AI prompts as toggle blocks
   - Add "좋은 예시" and "나쁜 예시" sections

2. **Create Template Buttons** (~5min per week):
   - Use `/template` command in each week page
   - Name: "내 실험 영역 만들기"
   - Template structure:
     ```
     ## 📝 [학생명]의 실험 영역
     ### 📥 Input: 내 연구 요약
     ### 🤖 실험 1: [Strategy Name]
     - 사용한 프롬프트:
     - AI 출력:
     - 자기 평가: /5
     ### 💬 동료 피드백
     ```

3. **Link Databases to Week Pages** (~2min per week):
   - Type `/database` in each week page
   - Select "Student Submissions"
   - Add filter: `Week = "Week N"`
   - Set view: Table or Board

4. **Configure Database Views** (~10min total):
   - Student Submissions: By Week, By Student, Peer Review Board
   - AI Recipe Library: By Week, Top Rated, Most Used

### Workshop Workflow (3-Stage Process)

**Stage 1: Individual Experimentation** (30-40min)
- Student clicks "내 실험 영역 만들기" button
- Tests 2-3 AI prompts from recipe library
- Records Input, Prompt, Output in their zone
- Self-evaluates using provided criteria

**Stage 2: Peer Review** (20-30min)
- Students visit each other's experiment zones
- Provide feedback using Notion comments
- Rate prompts and outputs
- Suggest improvements

**Stage 3: Collective Curation** (10-20min)
- Instructor highlights best examples
- Top recipes added to AI Recipe Library database
- Class discussion of what worked and why
- Next week preview

### Files & Documentation

- `week1/create_notion_workshop_simple.py`: Working automation script ✅
- `week1/create_notion_workshop_week2_6.py`: Full-featured script (reference)
- `week1/NOTION_WORKSHOP_DESIGN.md`: Complete design specification
- `week2-6/lecture_notes.md`: Content source for manual population

### Next Steps for Instructor

1. **Week 2 Setup** (estimated 45 minutes):
   - Add 4 Opening Patterns to 강의 자료 section
   - Create 10+ example prompt recipes as toggles
   - Set up Template Button for student workspace
   - Link Student Submissions database with filter
   - Test by creating sample student entry

2. **Weeks 3-6 Setup** (estimated 30 minutes each):
   - Follow same pattern as Week 2
   - Customize for week-specific strategies
   - Build on Recipe Library from previous weeks

3. **First Class** (Week 2):
   - 15min: Orient students to Notion workspace
   - 70min: Run 3-stage workshop process
   - 5min: Collect feedback for improvements

### Advantages Over Figma for Week 2-6

| Feature | Figma | Notion |
|---------|-------|--------|
| API automation | ❌ Read-only | ✅ Full CRUD |
| Database tracking | ❌ No | ✅ Built-in |
| Template buttons | ❌ No | ✅ Native |
| Search & filter | ⚠️ Limited | ✅ Powerful |
| Long-term storage | ✅ Yes | ✅ Yes |
| Real-time collab | ✅ Excellent | ✅ Good |
| Recipe accumulation | ⚠️ Manual | ✅ Database |

**Recommendation**:
- **Week 1**: Continue with Figma (visual, real-time, already implemented)
- **Week 2-6**: Use Notion (structured, trackable, accumulative learning)

## 🔑 Key Documents

### For Understanding Course Philosophy
- `강의계획.md`: Overall course structure and goals
- `overlap_analysis.md`: Why Week 2-4 were completely revised
- `claudedocs/comprehensive_revision_plan.md`: Complete implementation plan

### For Understanding Week-Specific Strategies
- `claudedocs/week2_revision_strategy.md`: Nature/Science abstract strategies
- `claudedocs/week3_revision_strategy.md`: Gap discovery workflows
- `claudedocs/week4_revision_strategy.md`: Methods/Results bulletproofing

### For Teaching
**Week 1** (Workshop Model):
- `week1/lesson_notes_compressed_90min.md`: 23 slides, 10 core principles (RECOMMENDED)
- `week1/workshop_materials.md`: Bad Sentences + Smart Revising checklist
- `week1/teaching_guide_90min.md`: Minute-by-minute guide with scripts
- `week1/lecture_notes.md`: Original detailed notes (reference only)

**Week 2-6** (AI-Enhanced):
- `week2/lecture_notes.md`: Top-tier abstract writing (395 lines)
- `week3/lecture_notes.md`: Systematic gap discovery (553 lines)
- `week4/lecture_notes.md`: Methods/Results bulletproofing (718 lines)

## 💡 Common Tasks

### Adding New AI Prompt Recipes
1. Identify the week and section
2. Follow the existing format:
   ```markdown
   ### [Recipe Number]. [Recipe Name]
   **목적**: [What this achieves]
   **프롬프트**:
   ```
   [Actual prompt template]
   ```
   **결과 평가 기준**: [How to evaluate output]
   ```
3. Add to the appropriate section in `weekN/lecture_notes.md`

### Updating Strategies
1. Consult `claudedocs/weekN_revision_strategy.md` for strategic direction
2. Modify `weekN/lecture_notes.md` for student-facing content
3. Ensure no AI concept explanations creep back in
4. Focus on practical application and top-tier publication criteria

### Creating New Examples
- Use real Nature/Science papers as examples
- Provide both "before" and "after" versions
- Include specific metrics (e.g., citation counts, impact factors)
- Explain why the "after" version is better for top-tier journals

### Uploading Materials to Notion
**ALWAYS use notion-client Python library for Notion uploads**

1. **Write Upload Script** (don't suggest manual copy-paste):
   ```python
   from notion_client import Client
   import os

   notion = Client(auth=os.getenv('NOTION_TOKEN'))
   notion.blocks.children.append(block_id=page_id, children=blocks)
   ```

2. **Convert Markdown to Notion Blocks**:
   - Headings (H1, H2, H3) → heading_1, heading_2, heading_3
   - Code blocks (```) → code blocks
   - Lists (-, *, 1.) → bulleted_list_item, numbered_list_item
   - Tables → code blocks (markdown format)
   - Quotes (>) → quote blocks

3. **Handle API Limits**:
   - Maximum 100 blocks per request
   - Batch larger files into multiple requests
   - See `week2/upload_lecture_notes.py` for implementation

4. **Success Pattern** (2025-01-04):
   - File: lecture_notes.md (1421 lines, 69KB)
   - Result: 617 blocks in 7 batches
   - Time: < 2 minutes
   - Page: https://notion.so/2a141454561d8077b956df19394fcf24

**Only fallback to manual methods when:**
- User explicitly requests it
- NOTION_TOKEN unavailable
- Content is very short (<100 words)

## 🚫 What NOT to Do

**DO NOT add AI concept explanations to Week 2-4:**
- ❌ "프롬프트는 Instruction, Context, Input, Output으로 구성됩니다" (students already know)
- ❌ "Temperature는 생성의 무작위성을 조절합니다" (students already know)
- ❌ "RAG는 외부 문서를 검색하여 답변합니다" (students already know)
- ❌ "CoT는 단계별로 사고하게 합니다" (students already know)

**DO add application strategies:**
- ✅ "Nature 초록은 일반 초록과 다르게 broad significance를 강조합니다"
- ✅ "Gap validation을 위한 3단계 워크플로우를 사용하세요"
- ✅ "Methods 섹션의 reproducibility checklist 6가지 항목"

## 🎯 Success Metrics

Students should be able to:
1. Write Nature/Science-level abstracts with differentiated opening strategies
2. Systematically discover and validate conceptual gaps (not incremental gaps)
3. Bulletproof Methods/Results sections against top-tier journal rejection
4. Use AI tools effectively (not just know what they are)
5. Share prompts, results, and provide structured peer feedback
6. Apply strategies to their own research immediately

## 📝 Notes for Future Claude Instances

### General Principles
- This is **not a software project** - it's course material
- No code to build, test, or deploy
- Focus on content quality, pedagogical effectiveness, and strategic alignment
- Always check overlap with 윤경생's lectures before adding content
- The ultimate goal is always: "어떻게 하면 탑 5%의 논문을 쓸 것인가"
- Students are psychology graduate students, not computer science students
- Examples should come from psychology/neuroscience research when possible
- All AI tool usage should be practical and immediately applicable to research writing

### Notion Integration
**CRITICAL: Always use notion-client Python library for Notion uploads**

When user requests uploading content to Notion:
1. **DO NOT suggest manual copy-paste** - write Python script first
2. **DO NOT suggest Notion's import feature** - use notion-client library
3. **Write automation script** using `from notion_client import Client`
4. **Reference working example**: `week2/upload_lecture_notes.py`

**Why this matters:**
- Manual methods don't scale (imagine uploading 10 weeks of materials)
- Automation is repeatable and version-controlled
- Batch processing handles API limits automatically
- Much faster: < 2 minutes vs 30+ minutes manual work

**Proven success** (2025-01-04):
- Uploaded lecture_notes.md (1421 lines, 69KB)
- Converted to 617 Notion blocks in 7 batches
- Handled headings, lists, code blocks, tables, quotes
- Page: https://notion.so/2a141454561d8077b956df19394fcf24

**Environment requirement:**
```bash
export NOTION_TOKEN='your_token'
pip install notion-client
```

**Only suggest manual methods when:**
- User explicitly requests it
- NOTION_TOKEN not available and user can't set it up
- Content is trivially short (<100 words)

### Week 1 Specific Guidelines
- **Use the compressed workshop model**: `lesson_notes_compressed_90min.md` is the primary teaching material
- **Practice-first philosophy**: Minimum 40% hands-on time (44% achieved in current design)
- **Cognitive load management**: 10 core principles is the limit, not 40+
- **Workshop over lecture**: 20min practice > 20min theory explanation
- **Peer learning**: Always include pair/group activities
- **Original materials**: `lecture_notes.md` is reference only, not for teaching
- If adding content: Compress first, then add to workshop materials, not lecture slides
