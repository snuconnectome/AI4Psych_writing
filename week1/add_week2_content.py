#!/usr/bin/env python3
"""
Week 2 Notion 페이지에 상세 콘텐츠 자동 추가 스크립트

Usage:
    python add_week2_content.py
"""

import os
import requests
import json

# Notion API 설정
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
NOTION_VERSION = '2022-06-28'
WEEK2_PAGE_ID = '29f41454-561d-8172-a4e9-d63c7eee0f0a'

headers = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': NOTION_VERSION
}

def add_blocks(page_id, blocks):
    """페이지에 블록 추가"""
    url = f'https://api.notion.com/v1/blocks/{page_id}/children'

    # Notion API는 한 번에 최대 100개 블록만 허용
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i+100]
        data = {'children': batch}

        response = requests.patch(url, headers=headers, json=data)

        if response.status_code != 200:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return False
        else:
            print(f"✅ Added {len(batch)} blocks (batch {i//100 + 1})")

    return True

def create_heading_1(text, color="blue_background"):
    """Heading 1 블록 생성"""
    return {
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }

def create_heading_2(text, color="default"):
    """Heading 2 블록 생성"""
    return {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }

def create_heading_3(text, color="default"):
    """Heading 3 블록 생성"""
    return {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }

def create_paragraph(text, color="default", bold=False):
    """Paragraph 블록 생성"""
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {"content": text},
                "annotations": {"bold": bold}
            }],
            "color": color
        }
    }

def create_callout(text, emoji="💡", color="gray_background"):
    """Callout 블록 생성"""
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "icon": {"type": "emoji", "emoji": emoji},
            "color": color
        }
    }

def create_bullet(text, color="default"):
    """Bulleted list item 블록 생성"""
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "color": color
        }
    }

def create_code(text, language="markdown"):
    """Code block 생성"""
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
            "language": language
        }
    }

def create_divider():
    """Divider 블록 생성"""
    return {
        "object": "block",
        "type": "divider",
        "divider": {}
    }

# ========================================
# Part 1: 강의 자료 블록
# ========================================
def get_part1_blocks():
    """Part 1: 강의 자료 섹션 블록"""
    blocks = []

    # 타이틀
    blocks.append(create_heading_1("📖 강의 자료: Nature/Science급 초록의 DNA"))
    blocks.append(create_divider())

    # 학습 목표
    blocks.append(create_heading_2("🎯 학습 목표"))
    blocks.append(create_bullet("Top-tier 저널과 일반 저널 초록의 결정적 차이 3가지 파악"))
    blocks.append(create_bullet("4가지 Opening 전략 중 내 연구에 맞는 패턴 선택"))
    blocks.append(create_bullet("Broad Significance 확장 기법으로 영향력 범위 극대화"))
    blocks.append(create_bullet("정량적 결과 제시로 임팩트 강조"))

    blocks.append(create_divider())

    # 4가지 Opening 전략
    blocks.append(create_heading_2("🔑 4가지 Opening 전략"))

    # 1. Problem-Driven
    blocks.append(create_heading_3("1️⃣ Problem-Driven Opening (문제 중심)"))
    blocks.append(create_paragraph("언제 사용: 오래된 난제, 해결되지 않은 문제", bold=True))
    blocks.append(create_paragraph("구조:", bold=True))
    blocks.append(create_code('Despite [decades/years] of research, [핵심 문제] remains [unsolved/poorly understood]...'))

    blocks.append(create_paragraph("예시:", bold=True))
    blocks.append(create_callout(
        '"Despite decades of research on ADHD, the neurobiological mechanisms underlying attention deficits remain poorly understood, affecting 5-10% of children worldwide."',
        emoji="📌"
    ))

    blocks.append(create_paragraph("차별화 포인트:", bold=True))
    blocks.append(create_bullet('시간적 긴급성 ("decades")'))
    blocks.append(create_bullet('실패의 역설 ("remains unsolved")'))
    blocks.append(create_bullet('광범위한 영향 ("5-10% of children")'))

    # 2. Gap-Driven
    blocks.append(create_heading_3("2️⃣ Gap-Driven Opening (공백 중심)"))
    blocks.append(create_paragraph("언제 사용: 확립된 이론 vs 미지의 영역", bold=True))
    blocks.append(create_paragraph("구조:", bold=True))
    blocks.append(create_code('While [확립된 지식] is well-established, we lack understanding of [critical gap]...'))

    blocks.append(create_paragraph("예시:", bold=True))
    blocks.append(create_callout(
        '"While the role of dopamine in reward learning is well-established, we lack understanding of how dopaminergic signaling interacts with social context—a gap critical for treating addiction in real-world settings."',
        emoji="📌"
    ))

    blocks.append(create_paragraph("차별화 포인트:", bold=True))
    blocks.append(create_bullet('기존 지식 인정 ("well-established")'))
    blocks.append(create_bullet('명확한 gap 진술 ("we lack understanding of")'))
    blocks.append(create_bullet('Real-world relevance ("treating addiction in real-world settings")'))

    # 3. Opportunity-Driven
    blocks.append(create_heading_3("3️⃣ Opportunity-Driven Opening (기회 중심)"))
    blocks.append(create_paragraph("언제 사용: 새로운 기술/방법론 활용", bold=True))
    blocks.append(create_paragraph("구조:", bold=True))
    blocks.append(create_code('Recent advances in [technology/method] enable unprecedented investigation of [phenomenon]...'))

    blocks.append(create_paragraph("예시:", bold=True))
    blocks.append(create_callout(
        '"Recent advances in large-scale neuroimaging enable unprecedented investigation of brain network dynamics across development, revealing how neural architecture reorganization supports cognitive maturation."',
        emoji="📌"
    ))

    # 4. Challenge-Driven
    blocks.append(create_heading_3("4️⃣ Challenge-Driven Opening (도전 중심)"))
    blocks.append(create_paragraph("언제 사용: 기존 패러다임 도전, 반직관적 발견", bold=True))
    blocks.append(create_paragraph("구조:", bold=True))
    blocks.append(create_code('[현상] poses a fundamental challenge to our understanding of [theory]...'))

    blocks.append(create_paragraph("예시:", bold=True))
    blocks.append(create_callout(
        '"The finding that meditation training can alter brain structure within weeks poses a fundamental challenge to classical neuroscience\'s view of adult neuroplasticity as limited and slow."',
        emoji="📌"
    ))

    blocks.append(create_divider())

    # Broad Significance 전략
    blocks.append(create_heading_2("🌍 Broad Significance 확장 전략"))

    blocks.append(create_heading_3("전략 1: Vertical Expansion (수직 확장)"))
    blocks.append(create_paragraph("개별 사례 → 보편적 원리", bold=True))
    blocks.append(create_bullet('"ADHD 아동의 주의력 결핍" → "인간 주의 시스템의 발달적 취약성"'))
    blocks.append(create_bullet('"쥐의 해마 신경가소성" → "포유류 학습의 신경생물학적 기반"'))
    blocks.append(create_bullet('"한국 청소년 우울증" → "발달 과정에서의 정서 조절 실패 메커니즘"'))

    blocks.append(create_heading_3("전략 2: Horizontal Expansion (수평 확장)"))
    blocks.append(create_paragraph("단일 분야 → 다학제 융합", bold=True))
    blocks.append(create_callout(
        'This mechanism has implications not only for clinical psychology (treatment of ADHD) but also for education (personalized learning systems), AI (attention-based algorithms), and public policy (early intervention programs).',
        emoji="💡"
    ))

    blocks.append(create_heading_3("전략 3: Temporal Expansion (시간적 확장)"))
    blocks.append(create_paragraph("현재 → 미래 영향", bold=True))
    blocks.append(create_code('These findings may enable [future application] and inform [long-term strategy]...'))

    blocks.append(create_divider())

    # 정량적 결과 제시
    blocks.append(create_heading_2("📊 정량적 결과 제시"))

    blocks.append(create_heading_3("Before vs After"))
    blocks.append(create_paragraph("❌ 나쁜 예시 (모호함):", bold=True))
    blocks.append(create_callout('"We found significant differences in brain activity."', emoji="❌", color="red_background"))

    blocks.append(create_paragraph("✅ 좋은 예시 (구체적):", bold=True))
    blocks.append(create_callout(
        '"Meditation training increased prefrontal cortex thickness by 8% (Cohen\'s d = 1.2, p < 0.001), equivalent to reversing 2 years of age-related decline."',
        emoji="✅",
        color="green_background"
    ))

    blocks.append(create_heading_3("3-Layer Quantification"))
    blocks.append(create_bullet('Layer 1: Raw numbers - "8% increase"'))
    blocks.append(create_bullet('Layer 2: Effect size - "Cohen\'s d = 1.2" (large effect)'))
    blocks.append(create_bullet('Layer 3: Real-world anchor - "equivalent to reversing 2 years..."'))

    return blocks

# ========================================
# Part 2: AI 프롬프트 레시피 블록
# ========================================
def get_part2_blocks():
    """Part 2: AI 프롬프트 레시피 섹션 블록"""
    blocks = []

    blocks.append(create_divider())
    blocks.append(create_heading_1("💡 AI 프롬프트 레시피 (복사해서 바로 사용)"))

    # Recipe 1
    blocks.append(create_heading_2("Recipe 1: 4-Pattern Opening Generator"))

    blocks.append(create_heading_3("📥 Input 준비사항"))
    blocks.append(create_bullet("내 연구 주제 1-2문장 요약"))
    blocks.append(create_bullet("주요 발견 1가지"))
    blocks.append(create_bullet("Target impact (누구에게 도움?)"))

    blocks.append(create_heading_3("🤖 프롬프트 (ChatGPT/Claude)"))

    prompt1 = """역할: 당신은 Nature/Science 편집 경험 10년의 과학 저널리스트입니다.

작업: 다음 연구를 4가지 Opening 패턴으로 재작성해주세요.

[내 연구 내용 붙여넣기]

4가지 패턴으로 작성:

1. Problem-driven Opening
- 구조: "Despite [time span] of research, [problem] remains [unsolved]..."
- 포함: 시간적 긴급성 + 실패의 역설 + 영향 받는 인구

2. Gap-driven Opening
- 구조: "While [established knowledge] is well-known, we lack understanding of [gap]..."
- 포함: 기존 지식 인정 + 명확한 gap + real-world relevance

3. Opportunity-driven Opening
- 구조: "Recent advances in [technology] enable unprecedented investigation of [phenomenon]..."
- 포함: 최신 기술 + unprecedented 수준 + 과학적 기여

4. Challenge-driven Opening
- 구조: "[Finding] poses a fundamental challenge to [theory]..."
- 포함: 반직관적 발견 + 기존 패러다임 도전

각 패턴마다 2-3문장으로 작성해주세요."""

    blocks.append(create_code(prompt1, language="plain text"))

    blocks.append(create_heading_3("📊 평가 기준 (5점 만점)"))
    blocks.append(create_bullet("4가지 패턴 모두 명확히 구분됨 (1점)"))
    blocks.append(create_bullet("구체적 수치/범위 포함 (1점)"))
    blocks.append(create_bullet("Broad significance 확장 시도 (1점)"))
    blocks.append(create_bullet("긴급성/중요성 전달 (1점)"))
    blocks.append(create_bullet("내 연구의 고유성 드러남 (1점)"))

    blocks.append(create_callout(
        "Success Tip: 가장 마음에 드는 패턴을 선택한 후, '이 패턴을 더 강하게 만들려면?'이라고 후속 질문하세요.",
        emoji="💬",
        color="yellow_background"
    ))

    # Recipe 2
    blocks.append(create_heading_2("Recipe 2: Broad Significance Expander"))

    blocks.append(create_heading_3("📥 Input 준비사항"))
    blocks.append(create_bullet("현재 초록의 Significance 문장"))
    blocks.append(create_bullet("내 연구 분야 (예: cognitive neuroscience)"))

    blocks.append(create_heading_3("🤖 프롬프트 (Claude 추천)"))

    prompt2 = """역할: 당신은 학제간 연구 전문 Science Advisor입니다.

작업: 다음 연구의 significance를 3가지 방향으로 확장하세요.

[현재 significance 문장 붙여넣기]
[연구 분야: ___________]

확장 방향:

1. Vertical Expansion (수직 확장)
- 개별 사례 → 보편적 원리
- "이 메커니즘은 [broader category]에 대한 이해를 넓힌다"

2. Horizontal Expansion (수평 확장)
- 최소 3개 분야 연결: 내 분야 + 응용 분야 + 정책/사회
- "이는 [field 1], [field 2], [field 3]에 함의를 갖는다"

3. Temporal Expansion (시간적 확장)
- 단기 → 장기 영향
- "이 발견은 [future application]을 가능케 하고 [long-term strategy]에 정보를 제공한다"

각 확장마다 구체적 예시와 함께 2-3문장으로 작성하세요."""

    blocks.append(create_code(prompt2, language="plain text"))

    blocks.append(create_callout(
        "Success Tip: Horizontal Expansion에서 'Clinical + AI + Policy'처럼 예상 밖 조합을 시도하면 신선합니다.",
        emoji="💬",
        color="yellow_background"
    ))

    # Recipe 3
    blocks.append(create_heading_2("Recipe 3: Quantification Booster"))

    blocks.append(create_heading_3("📥 Input 준비사항"))
    blocks.append(create_bullet("주요 발견 (정성적 표현도 OK)"))
    blocks.append(create_bullet("사용한 통계 검정 결과 (p-value, effect size 등)"))

    blocks.append(create_heading_3("🤖 프롬프트 (ChatGPT 추천)"))

    prompt3 = """역할: 당신은 통계 보고의 명확성을 강조하는 Nature Methods 편집자입니다.

작업: 다음 발견을 3-Layer Quantification으로 재작성하세요.

[내 발견 붙여넣기]
[통계 결과: p-value = ___, effect size = ___, 샘플 크기 = ___]

3-Layer Quantification 구조:

Layer 1: Raw Numbers
- 정확한 수치 + 단위 + 방향
- 예: "8% increase", "2.5-fold reduction"

Layer 2: Statistical Strength
- Effect size (Cohen's d, η², OR 등)
- p-value (정확한 값, 단 p < 0.001은 그대로)
- 예: "Cohen's d = 1.2, p < 0.001"

Layer 3: Real-World Anchor
- 일상적 비유 또는 임상적 의미
- 예: "equivalent to reversing 2 years of age-related decline"
- 예: "comparable to the effect of 6 months of standard therapy"

최종 출력을 하나의 문장으로 통합하세요."""

    blocks.append(create_code(prompt3, language="plain text"))

    blocks.append(create_callout(
        "Success Tip: Real-world anchor는 '임상적 의미 + 시간적 비유'가 가장 강력합니다. 예: '3개월 치료 효과에 해당'",
        emoji="💬",
        color="yellow_background"
    ))

    # Workflow
    blocks.append(create_heading_3("🎯 Recipe 사용 Workflow"))
    workflow = """Step 1: 내 초록 현재 버전 준비
       ↓
Step 2: Recipe 1로 4가지 Opening 생성
       ↓ (가장 강한 패턴 선택)
Step 3: Recipe 2로 Significance 확장
       ↓ (3방향 중 2개 선택해 통합)
Step 4: Recipe 3으로 Results 정량화
       ↓
Step 5: 전체 초록 재조립 후 자기평가

목표 시간: 30분 이내"""
    blocks.append(create_code(workflow, language="plain text"))

    return blocks

# ========================================
# Part 3: 평가 기준표 블록
# ========================================
def get_part3_blocks():
    """Part 3: 평가 기준표 섹션 블록"""
    blocks = []

    blocks.append(create_divider())
    blocks.append(create_heading_1("📋 평가 기준표: Top-Tier Abstract Checklist"))

    blocks.append(create_callout(
        "이 체크리스트로 동료 피드백 & 자기 평가",
        emoji="🎯"
    ))

    # Section 1: Opening
    blocks.append(create_heading_2("Section 1: Opening (20점)"))
    blocks.append(create_bullet("☐ 4가지 패턴 중 하나 명확히 사용 (5점)"))
    blocks.append(create_bullet('☐ 긴급성/중요성 전달 ("remains unsolved", "unprecedented") (5점)'))
    blocks.append(create_bullet("☐ 영향 받는 인구/규모 제시 (숫자 포함) (5점)"))
    blocks.append(create_bullet('☐ 첫 문장부터 "이 연구는 중요하다"는 인상 (5점)'))

    # Section 2: Significance
    blocks.append(create_heading_2("Section 2: Significance (30점)"))
    blocks.append(create_bullet("☐ Broad significance: 최소 2개 분야 언급 (10점)"))
    blocks.append(create_bullet("☐ Vertical expansion: 개별 → 보편적 원리 (5점)"))
    blocks.append(create_bullet("☐ Horizontal expansion: 다학제 연결 (Clinical + AI + Policy 등) (10점)"))
    blocks.append(create_bullet("☐ Temporal expansion: 미래 응용 제시 (5점)"))

    # Section 3: Gap
    blocks.append(create_heading_2("Section 3: Gap (20점)"))
    blocks.append(create_bullet('☐ "We lack understanding of..." 명시적 진술 (10점)'))
    blocks.append(create_bullet("☐ 기존 지식 vs 미지의 영역 명확히 대비 (5점)"))
    blocks.append(create_bullet("☐ Real-world relevance 연결 (5점)"))

    # Section 4: Results
    blocks.append(create_heading_2("Section 4: Results (30점)"))
    blocks.append(create_bullet("☐ Layer 1: Raw numbers + 단위 + 방향 (10점)"))
    blocks.append(create_bullet("☐ Layer 2: Effect size + p-value (10점)"))
    blocks.append(create_bullet("☐ Layer 3: Real-world anchor (일상적 비유 또는 임상적 의미) (10점)"))

    blocks.append(create_divider())

    # Quick Test
    blocks.append(create_heading_2("🌟 Top-Tier 판별 Quick Test (30초)"))
    blocks.append(create_paragraph("다음 3가지 질문에 모두 \"Yes\"면 top-tier급:", bold=True))

    blocks.append(create_paragraph('1. Opening Test: 첫 문장을 읽고 "이 연구는 중요하다"는 인상을 받는가?', bold=True))
    blocks.append(create_bullet("☐ Yes → Top-tier"))
    blocks.append(create_bullet("☐ No → 일반 저널"))

    blocks.append(create_paragraph("2. Significance Test: Significance가 2개 이상 분야를 커버하는가?", bold=True))
    blocks.append(create_bullet("☐ Yes (Clinical + AI) → Top-tier"))
    blocks.append(create_bullet("☐ No (Clinical만) → 일반 저널"))

    blocks.append(create_paragraph('3. Quantification Test: 결과가 "숫자 + effect size + 현실적 비유" 3가지 모두 포함하는가?', bold=True))
    blocks.append(create_bullet("☐ Yes → Top-tier"))
    blocks.append(create_bullet("☐ No → 일반 저널"))

    blocks.append(create_divider())

    # 2 Stars & 1 Wish 템플릿
    blocks.append(create_heading_2("📝 2 Stars & 1 Wish 피드백 템플릿"))

    blocks.append(create_paragraph("⭐ Star 1 (이 부분이 강력함):", bold=True))
    blocks.append(create_callout(
        '예: "Opening이 Problem-driven 패턴을 명확히 사용했고, \'10년간 해결 안 됨\' + \'5% 아동 영향\'으로 긴급성과 규모를 동시에 전달함"',
        emoji="⭐"
    ))

    blocks.append(create_paragraph("⭐ Star 2 (이 부분도 좋음):", bold=True))
    blocks.append(create_callout(
        '예: "Significance를 Clinical (ADHD 치료) + Education (맞춤형 학습) + AI (주의 알고리즘)로 3방향 확장해 학제간 영향력 보여줌"',
        emoji="⭐"
    ))

    blocks.append(create_paragraph("💭 Wish (이렇게 하면 더 좋을 것 같음):", bold=True))
    blocks.append(create_callout(
        '예: "Results에 Real-world anchor 추가하면 좋겠음. 예: \'8% 증가\'를 \'2년치 노화 효과 역전에 해당\'처럼 일상적 비유로 연결"',
        emoji="💭",
        color="yellow_background"
    ))

    return blocks

# ========================================
# Part 4: 좋은/나쁜 예시 블록
# ========================================
def get_part4_blocks():
    """Part 4: 좋은/나쁜 예시 섹션 블록"""
    blocks = []

    blocks.append(create_divider())
    blocks.append(create_heading_1("📚 좋은 예시 vs 나쁜 예시"))

    # Example 1: Opening
    blocks.append(create_heading_2("Example 1: Opening 비교"))

    blocks.append(create_heading_3("❌ 일반 저널 Opening"))
    blocks.append(create_callout(
        '"Attention-deficit/hyperactivity disorder (ADHD) is a common neurodevelopmental disorder. Previous studies have shown alterations in brain function. However, the mechanisms are not fully understood."',
        emoji="❌",
        color="red_background"
    ))

    blocks.append(create_paragraph("문제점:", bold=True))
    blocks.append(create_bullet('긴급성 없음 ("common"은 약한 표현)'))
    blocks.append(create_bullet('모호함 ("mechanisms are not fully understood"는 너무 일반적)'))
    blocks.append(create_bullet("영향력 없음 (숫자 없음)"))

    blocks.append(create_heading_3("✅ Nature/Science급 Opening"))
    blocks.append(create_callout(
        '"Despite decades of research, the neurobiological mechanisms underlying attention deficits in ADHD remain poorly understood, affecting 5-10% of children worldwide and imposing annual societal costs exceeding $140 billion."',
        emoji="✅",
        color="green_background"
    ))

    blocks.append(create_paragraph("강점:", bold=True))
    blocks.append(create_bullet("Problem-driven 패턴 명확"))
    blocks.append(create_bullet('시간적 긴급성 ("decades")'))
    blocks.append(create_bullet('영향 받는 인구 ("5-10% of children")'))
    blocks.append(create_bullet('경제적 임팩트 ("$140 billion")'))

    # Example 2: Significance
    blocks.append(create_heading_2("Example 2: Significance 비교"))

    blocks.append(create_heading_3("❌ 일반 저널 Significance"))
    blocks.append(create_callout(
        '"Our findings provide important insights into ADHD treatment and may help develop better interventions."',
        emoji="❌",
        color="red_background"
    ))

    blocks.append(create_paragraph("문제점:", bold=True))
    blocks.append(create_bullet('모호함 ("important insights"는 공허한 표현)'))
    blocks.append(create_bullet("단일 분야 (Clinical만)"))
    blocks.append(create_bullet('미래 응용이 불명확 ("may help"는 약함)'))

    blocks.append(create_heading_3("✅ Nature/Science급 Significance"))
    blocks.append(create_callout(
        'These findings have implications for clinical psychology (personalized ADHD treatment), education (adaptive learning systems), AI development (attention-based neural architectures), and public health policy (early screening programs), bridging neuroscience with real-world applications across multiple sectors.',
        emoji="✅",
        color="green_background"
    ))

    blocks.append(create_paragraph("강점:", bold=True))
    blocks.append(create_bullet("Horizontal expansion: 4개 분야 명시적 연결"))
    blocks.append(create_bullet('구체적 응용 ("adaptive learning systems", "attention-based architectures")'))
    blocks.append(create_bullet('"Bridging"으로 학제간 기여 강조'))

    # Example 3: Results
    blocks.append(create_heading_2("Example 3: Results 비교"))

    blocks.append(create_heading_3("❌ 일반 저널 Results"))
    blocks.append(create_callout(
        '"We found that meditation training significantly improved attention (p < 0.05)."',
        emoji="❌",
        color="red_background"
    ))

    blocks.append(create_paragraph("문제점:", bold=True))
    blocks.append(create_bullet("Raw numbers 없음 (얼마나 개선?)"))
    blocks.append(create_bullet("Effect size 없음 (실질적 크기?)"))
    blocks.append(create_bullet("Real-world anchor 없음 (임상적 의미?)"))

    blocks.append(create_heading_3("✅ Nature/Science급 Results"))
    blocks.append(create_callout(
        '"Eight weeks of meditation training increased prefrontal cortex thickness by 8% (Cohen\'s d = 1.2, p < 0.001), equivalent to reversing approximately 2 years of age-related cortical thinning—an effect comparable to 6 months of standard pharmacological treatment."',
        emoji="✅",
        color="green_background"
    ))

    blocks.append(create_paragraph("강점:", bold=True))
    blocks.append(create_bullet("Layer 1: 8% increase (구체적)"))
    blocks.append(create_bullet("Layer 2: Cohen's d = 1.2 (large effect)"))
    blocks.append(create_bullet('Layer 3: "2 years reversal" + "6 months treatment" (두 가지 anchor)'))

    # Why Not Both 전략
    blocks.append(create_divider())
    blocks.append(create_heading_2('💡 "Why Not Both?" 전략'))

    blocks.append(create_paragraph('많은 학생들이 "Broad significance vs Honest limitations" 사이에서 고민합니다.'))

    blocks.append(create_heading_3('해결책: "Why Not Both?" 구조'))

    why_not_both = """[Broad significance 문장]
+
"While our findings are limited to [specific context], the underlying mechanism likely generalizes to [broader context], warranting future investigation across [diverse populations/settings].\""""

    blocks.append(create_code(why_not_both))

    blocks.append(create_paragraph("예시:", bold=True))
    blocks.append(create_callout(
        'These findings have implications for clinical psychology, education, and AI development. While our study focused on young adults, the attentional mechanism likely generalizes across age groups, warranting investigation in children and older adults where attention deficits are most clinically significant.',
        emoji="💡",
        color="gray_background"
    ))

    blocks.append(create_paragraph("효과:", bold=True))
    blocks.append(create_bullet("Broad significance 유지"))
    blocks.append(create_bullet("정직하게 limitations 인정"))
    blocks.append(create_bullet("미래 연구 방향 제시"))
    blocks.append(create_bullet('"Likely generalizes"로 과학적 합리성 유지'))

    return blocks


# ========================================
# Main Execution
# ========================================
def main():
    print("🚀 Week 2 Notion 페이지 콘텐츠 자동 추가 시작...\n")

    # Check environment
    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    print(f"📄 Target Page: Week 2: Nature/Science급 초록 작성")
    print(f"🆔 Page ID: {WEEK2_PAGE_ID}\n")

    # 모든 블록 수집
    all_blocks = []

    print("📦 Part 1: 강의 자료 블록 생성 중...")
    all_blocks.extend(get_part1_blocks())
    print(f"   ✅ {len(all_blocks)} blocks")

    print("📦 Part 2: AI 프롬프트 레시피 블록 생성 중...")
    part2_start = len(all_blocks)
    all_blocks.extend(get_part2_blocks())
    print(f"   ✅ {len(all_blocks) - part2_start} blocks")

    print("📦 Part 3: 평가 기준표 블록 생성 중...")
    part3_start = len(all_blocks)
    all_blocks.extend(get_part3_blocks())
    print(f"   ✅ {len(all_blocks) - part3_start} blocks")

    print("📦 Part 4: 좋은/나쁜 예시 블록 생성 중...")
    part4_start = len(all_blocks)
    all_blocks.extend(get_part4_blocks())
    print(f"   ✅ {len(all_blocks) - part4_start} blocks")

    print(f"\n📊 총 {len(all_blocks)}개 블록 생성 완료")

    # API 호출로 블록 추가
    print("\n🌐 Notion API를 통해 블록 추가 중...\n")

    success = add_blocks(WEEK2_PAGE_ID, all_blocks)

    if success:
        print("\n✅ 성공! Week 2 페이지에 모든 콘텐츠가 추가되었습니다.")
        print(f"🔗 확인: https://www.notion.so/Week-2-Nature-Science-29f41454561d8172a4e9d63c7eee0f0a")
    else:
        print("\n❌ 오류가 발생했습니다. 위의 에러 메시지를 확인하세요.")

if __name__ == '__main__':
    main()
