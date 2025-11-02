#!/usr/bin/env python3
"""
Notion Workshop 자동 생성 스크립트 (Week 2-6)

사용법:
    python create_notion_workshop_week2_6.py <parent_page_id>
    또는
    python create_notion_workshop_week2_6.py (interactive mode)

환경 변수:
    NOTION_TOKEN: Notion Integration Token
"""

import os
import sys
import requests
import json
from typing import Dict, List, Any

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_API_URL = 'https://api.notion.com/v1'
HEADERS = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

# 색상 정의
COLORS = {
    'blue': 'blue',
    'green': 'green',
    'yellow': 'yellow',
    'red': 'red',
    'purple': 'purple',
    'gray': 'gray'
}


def create_page(parent_id: str, title: str, icon: str = None) -> Dict:
    """새 페이지 생성"""
    payload = {
        'parent': {'page_id': parent_id},
        'properties': {
            'title': {
                'title': [{'text': {'content': title}}]
            }
        }
    }

    if icon:
        payload['icon'] = {'type': 'emoji', 'emoji': icon}

    response = requests.post(
        f'{NOTION_API_URL}/pages',
        headers=HEADERS,
        json=payload
    )
    response.raise_for_status()
    return response.json()


def create_database(parent_id: str, title: str, properties: Dict) -> Dict:
    """새 데이터베이스 생성"""
    payload = {
        'parent': {'page_id': parent_id},
        'title': [{'text': {'content': title}}],
        'properties': properties
    }

    response = requests.post(
        f'{NOTION_API_URL}/databases',
        headers=HEADERS,
        json=payload
    )

    if not response.ok:
        print(f"❌ Database creation failed. Status: {response.status_code}")
        print(f"Response: {response.text}")

    response.raise_for_status()
    return response.json()


def add_blocks(page_id: str, blocks: List[Dict]) -> Dict:
    """페이지에 블록 추가"""
    payload = {'children': blocks}

    response = requests.patch(
        f'{NOTION_API_URL}/blocks/{page_id}/children',
        headers=HEADERS,
        json=payload
    )

    if not response.ok:
        print(f"❌ Block addition failed. Status: {response.status_code}")
        print(f"Response: {response.text}")
        print(f"Attempted to add {len(blocks)} blocks")

    response.raise_for_status()
    return response.json()


# ============================================
# Database 생성 함수
# ============================================

def create_student_submissions_db(parent_id: str) -> str:
    """Student Submissions Database 생성"""
    properties = {
        'Name': {
            'type': 'title',
            'title': {}
        },
        '학생': {
            'type': 'people',
            'people': {}
        },
        'Week': {
            'type': 'select',
            'select': {
                'options': [
                    {'name': 'Week 2', 'color': COLORS['blue']},
                    {'name': 'Week 3', 'color': COLORS['green']},
                    {'name': 'Week 4', 'color': COLORS['yellow']},
                    {'name': 'Week 5', 'color': COLORS['red']},
                    {'name': 'Week 6', 'color': COLORS['purple']}
                ]
            }
        },
        'Section': {
            'type': 'select',
            'select': {
                'options': [
                    {'name': 'Abstract', 'color': COLORS['blue']},
                    {'name': 'Introduction', 'color': COLORS['green']},
                    {'name': 'Methods', 'color': COLORS['yellow']},
                    {'name': 'Results', 'color': COLORS['red']},
                    {'name': 'Discussion', 'color': COLORS['purple']}
                ]
            }
        },
        'Status': {
            'type': 'select',
            'select': {
                'options': [
                    {'name': 'Not Started', 'color': COLORS['gray']},
                    {'name': 'In Progress', 'color': COLORS['blue']},
                    {'name': 'Submitted', 'color': COLORS['yellow']},
                    {'name': 'Peer Reviewed', 'color': COLORS['green']},
                    {'name': 'Revised', 'color': COLORS['purple']}
                ]
            }
        },
        '제출일': {
            'type': 'date',
            'date': {}
        },
        'Peer Reviewer': {
            'type': 'people',
            'people': {}
        },
        'Peer Score': {
            'type': 'number',
            'number': {'format': 'number'}
        },
        'Peer Feedback': {
            'type': 'rich_text',
            'rich_text': {}
        },
        'Instructor Feedback': {
            'type': 'rich_text',
            'rich_text': {}
        },
        'Version': {
            'type': 'number',
            'number': {'format': 'number'}
        }
    }

    db = create_database(parent_id, '📊 Student Submissions', properties)
    print(f"✅ Created Student Submissions Database: {db['id']}")
    return db['id']


def create_recipe_library_db(parent_id: str) -> str:
    """AI Recipe Library Database 생성"""
    properties = {
        'Recipe Name': {
            'type': 'title',
            'title': {}
        },
        'Week': {
            'type': 'select',
            'select': {
                'options': [
                    {'name': 'Week 2', 'color': COLORS['blue']},
                    {'name': 'Week 3', 'color': COLORS['green']},
                    {'name': 'Week 4', 'color': COLORS['yellow']},
                    {'name': 'Week 5', 'color': COLORS['red']},
                    {'name': 'Week 6', 'color': COLORS['purple']}
                ]
            }
        },
        'Category': {
            'type': 'select',
            'select': {
                'options': [
                    {'name': 'Opening', 'color': COLORS['blue']},
                    {'name': 'Gap Discovery', 'color': COLORS['green']},
                    {'name': 'Methods', 'color': COLORS['yellow']},
                    {'name': 'Results', 'color': COLORS['red']},
                    {'name': 'Discussion', 'color': COLORS['purple']}
                ]
            }
        },
        'Purpose': {
            'type': 'rich_text',
            'rich_text': {}
        },
        'Prompt Template': {
            'type': 'rich_text',
            'rich_text': {}
        },
        'Success Rate': {
            'type': 'number',
            'number': {'format': 'number'}
        },
        'Submitted By': {
            'type': 'people',
            'people': {}
        },
        'Used Count': {
            'type': 'number',
            'number': {'format': 'number'}
        },
        'Example Output': {
            'type': 'rich_text',
            'rich_text': {}
        },
        'Tags': {
            'type': 'multi_select',
            'multi_select': {
                'options': [
                    {'name': 'Nature', 'color': COLORS['blue']},
                    {'name': 'Science', 'color': COLORS['green']},
                    {'name': 'Significance', 'color': COLORS['yellow']},
                    {'name': 'Gap', 'color': COLORS['red']},
                    {'name': 'Validation', 'color': COLORS['purple']}
                ]
            }
        }
    }

    db = create_database(parent_id, '🧪 AI Recipe Library', properties)
    print(f"✅ Created AI Recipe Library Database: {db['id']}")
    return db['id']


# ============================================
# Week 2 페이지 생성
# ============================================

def create_week2_page(parent_id: str, submissions_db_id: str) -> str:
    """Week 2: Nature/Science급 초록 작성 워크샵"""

    # 1. 페이지 생성
    page = create_page(parent_id, 'Week 2: Nature/Science급 초록 작성', '📅')
    page_id = page['id']

    # 2. 블록 추가
    blocks = [
        # 헤더
        {
            'type': 'heading_1',
            'heading_1': {
                'rich_text': [{'text': {'content': '📚 핵심 전략'}}],
                'color': 'blue_background'
            }
        },

        # 4가지 Opening Patterns
        {
            'type': 'heading_2',
            'heading_2': {
                'rich_text': [{'text': {'content': '4가지 Opening Patterns'}}]
            }
        },

        # Problem-Driven 토글
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'type': 'text', 'text': {'content': '1️⃣ Problem-Driven Opening'}, 'annotations': {'bold': True}}],
                'children': [
                    {
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [{'text': {'content': '"현재 문제를 명확히 제시"'}}]
                        }
                    },
                    {
                        'type': 'bulleted_list_item',
                        'bulleted_list_item': {
                            'rich_text': [{'text': {'content': 'Nature 예시: "Climate change threatens biodiversity..."'}}]
                        }
                    },
                    {
                        'type': 'bulleted_list_item',
                        'bulleted_list_item': {
                            'rich_text': [{'text': {'content': 'Science 예시: "Memory decline affects millions..."'}}]
                        }
                    }
                ]
            }
        },

        # Gap-Driven 토글
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'text': {'content': '2️⃣ Gap-Driven Opening', 'annotations': {'bold': True}}}],
                'children': [
                    {
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [{'text': {'content': '"알려지지 않은 것을 강조"'}}]
                        }
                    },
                    {
                        'type': 'bulleted_list_item',
                        'bulleted_list_item': {
                            'rich_text': [{'text': {'content': 'Nature 예시: "Despite advances, it remains unknown..."'}}]
                        }
                    }
                ]
            }
        },

        # Opportunity-Driven 토글
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'text': {'content': '3️⃣ Opportunity-Driven Opening', 'annotations': {'bold': True}}}],
                'children': [
                    {
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [{'text': {'content': '"가능성과 잠재력 제시"'}}]
                        }
                    },
                    {
                        'type': 'bulleted_list_item',
                        'bulleted_list_item': {
                            'rich_text': [{'text': {'content': 'Science 예시: "Recent breakthroughs enable..."'}}]
                        }
                    }
                ]
            }
        },

        # Challenge-Driven 토글
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'text': {'content': '4️⃣ Challenge-Driven Opening', 'annotations': {'bold': True}}}],
                'children': [
                    {
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [{'text': {'content': '"어려움을 해결하는 접근"'}}]
                        }
                    },
                    {
                        'type': 'bulleted_list_item',
                        'bulleted_list_item': {
                            'rich_text': [{'text': {'content': 'Nature 예시: "Overcoming the challenge of..."'}}]
                        }
                    }
                ]
            }
        },

        # 평가 기준
        {
            'type': 'heading_2',
            'heading_2': {
                'rich_text': [{'text': {'content': '🎯 평가 기준'}}]
            }
        },
        {
            'type': 'bulleted_list_item',
            'bulleted_list_item': {
                'rich_text': [{'text': {'content': 'Broad Significance (0-2점)'}}]
            }
        },
        {
            'type': 'bulleted_list_item',
            'bulleted_list_item': {
                'rich_text': [{'text': {'content': 'Opening Impact (0-2점)'}}]
            }
        },
        {
            'type': 'bulleted_list_item',
            'bulleted_list_item': {
                'rich_text': [{'text': {'content': 'Result Clarity (0-1점)'}}]
            }
        },
        {
            'type': 'paragraph',
            'paragraph': {
                'rich_text': [{'text': {'content': 'Total: 5점', 'annotations': {'bold': True}}}]
            }
        },

        # 예시 프롬프트
        {
            'type': 'heading_2',
            'heading_2': {
                'rich_text': [{'text': {'content': '💡 예시 프롬프트'}}]
            }
        },
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'text': {'content': 'Recipe 1: Problem-Driven Opening', 'annotations': {'bold': True}}}],
                'children': [
                    {
                        'type': 'paragraph',
                        'paragraph': {
                            'rich_text': [{'text': {'content': '목적: Nature급 Problem-driven 초록 작성', 'annotations': {'bold': True}}}]
                        }
                    },
                    {
                        'type': 'code',
                        'code': {
                            'rich_text': [{'text': {'content': '내 연구를 Nature 수준의 Problem-driven opening으로\n시작하는 초록을 작성해줘.\n\n연구 내용:\n[학생이 입력]\n\n요구사항:\n- 첫 문장에서 broad problem을 제시\n- 왜 이 문제가 중요한지 2-3 문장으로 설명\n- 정량적 수치로 문제의 심각성 표현'}}],
                            'language': 'plain text'
                        }
                    }
                ]
            }
        },

        # 구분선
        {
            'type': 'divider',
            'divider': {}
        },

        # AI 실험실
        {
            'type': 'heading_1',
            'heading_1': {
                'rich_text': [{'text': {'content': '🧪 AI 실험실'}}],
                'color': 'green_background'
            }
        },

        # Student Submissions Database (Linked)
        {
            'type': 'child_database',
            'child_database': {
                'title': 'Week 2 제출물',
                'database_id': submissions_db_id
            }
        },

        # 워크샵 가이드
        {
            'type': 'callout',
            'callout': {
                'rich_text': [{'text': {'content': '💬 Template Button은 수동으로 설정이 필요합니다 (아래 가이드 참조)', 'annotations': {'bold': True}}}],
                'icon': {'type': 'emoji', 'emoji': '⚠️'},
                'color': 'yellow_background'
            }
        }
    ]

    add_blocks(page_id, blocks)
    print(f"✅ Created Week 2 Workshop Page: {page_id}")
    return page_id


# ============================================
# Week 3-6 간략 버전 (동일 패턴)
# ============================================

def create_week3_page(parent_id: str, submissions_db_id: str) -> str:
    """Week 3: Gap Discovery"""
    page = create_page(parent_id, 'Week 3: 체계적 Research Gap 발견', '📅')
    page_id = page['id']

    blocks = [
        {
            'type': 'heading_1',
            'heading_1': {
                'rich_text': [{'text': {'content': '📚 Gap 유형 분류'}}],
                'color': 'blue_background'
            }
        },
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'text': {'content': '❌ Incremental Gap (탑티어 부적합)', 'annotations': {'bold': True}}}],
                'children': [
                    {'type': 'paragraph', 'paragraph': {'rich_text': [{'text': {'content': '"이 조건에서는 아직 실험 안 됨"'}}]}}
                ]
            }
        },
        {
            'type': 'toggle',
            'toggle': {
                'rich_text': [{'text': {'content': '✅ Conceptual Gap (탑티어 적합)', 'annotations': {'bold': True}}}],
                'children': [
                    {'type': 'paragraph', 'paragraph': {'rich_text': [{'text': {'content': '"이론으로 설명 안 됨"'}}]}}
                ]
            }
        },
        {
            'type': 'divider',
            'divider': {}
        },
        {
            'type': 'heading_1',
            'heading_1': {
                'rich_text': [{'text': {'content': '🧪 Gap Discovery Canvas'}}]
            }
        },
        {
            'type': 'child_database',
            'child_database': {
                'title': 'Week 3 제출물',
                'database_id': submissions_db_id
            }
        }
    ]

    add_blocks(page_id, blocks)
    print(f"✅ Created Week 3 Workshop Page: {page_id}")
    return page_id


def create_week4_page(parent_id: str, submissions_db_id: str) -> str:
    """Week 4: Methods/Results Bulletproofing"""
    page = create_page(parent_id, 'Week 4: Methods/Results Bulletproofing', '📅')
    page_id = page['id']

    blocks = [
        {'type': 'heading_1', 'heading_1': {'rich_text': [{'text': {'content': '🛡️ Bulletproofing Strategies'}}]}},
        {'type': 'callout', 'callout': {'rich_text': [{'text': {'content': 'Red Team/Blue Team 게임으로 약점 발견 및 보완'}}], 'icon': {'type': 'emoji', 'emoji': '⚔️'}}},
        {'type': 'divider', 'divider': {}},
        {'type': 'child_database', 'child_database': {'title': 'Week 4 제출물', 'database_id': submissions_db_id}}
    ]

    add_blocks(page_id, blocks)
    print(f"✅ Created Week 4 Workshop Page: {page_id}")
    return page_id


def create_week5_page(parent_id: str, submissions_db_id: str) -> str:
    """Week 5: Discussion Section"""
    page = create_page(parent_id, 'Week 5: Discussion Section', '📅')
    page_id = page['id']

    blocks = [
        {'type': 'heading_1', 'heading_1': {'rich_text': [{'text': {'content': '💬 Discussion Strategies'}}]}},
        {'type': 'callout', 'callout': {'rich_text': [{'text': {'content': 'AI Diagnostic Canvas + 3-Pass Revision'}}], 'icon': {'type': 'emoji', 'emoji': '🔍'}}},
        {'type': 'divider', 'divider': {}},
        {'type': 'child_database', 'child_database': {'title': 'Week 5 제출물', 'database_id': submissions_db_id}}
    ]

    add_blocks(page_id, blocks)
    print(f"✅ Created Week 5 Workshop Page: {page_id}")
    return page_id


def create_week6_page(parent_id: str, submissions_db_id: str) -> str:
    """Week 6: Final Polish"""
    page = create_page(parent_id, 'Week 6: Final Polish & Peer Review', '📅')
    page_id = page['id']

    blocks = [
        {'type': 'heading_1', 'heading_1': {'rich_text': [{'text': {'content': '✨ Final Polish Strategies'}}]}},
        {'type': 'callout', 'callout': {'rich_text': [{'text': {'content': 'Hook Generation + Impact Pyramid + Comprehensive Review'}}], 'icon': {'type': 'emoji', 'emoji': '🎯'}}},
        {'type': 'divider', 'divider': {}},
        {'type': 'child_database', 'child_database': {'title': 'Week 6 제출물', 'database_id': submissions_db_id}}
    ]

    add_blocks(page_id, blocks)
    print(f"✅ Created Week 6 Workshop Page: {page_id}")
    return page_id


# ============================================
# Main 함수
# ============================================

def main():
    """메인 실행 함수"""

    print("=" * 60)
    print("Notion Workshop 자동 생성 시작 (Week 2-6)")
    print("=" * 60)

    # 환경 변수 확인
    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    # Parent 페이지 ID (커맨드라인 인자 또는 interactive)
    if len(sys.argv) > 1:
        parent_page_id = sys.argv[1].strip()
        print(f"📍 Parent 페이지 ID: {parent_page_id}")
    else:
        parent_page_id = input("Parent 페이지 ID를 입력하세요 (예: 29841454-561d-8038-8b45-eb0124054ec8): ").strip()

    if not parent_page_id:
        print("❌ Error: Parent 페이지 ID가 필요합니다.")
        return

    try:
        # 1. Databases 생성
        print("\n📊 Step 1: Databases 생성 중...")
        submissions_db_id = create_student_submissions_db(parent_page_id)
        recipe_db_id = create_recipe_library_db(parent_page_id)

        # 2. Week 페이지들 생성
        print("\n📅 Step 2: Week 2-6 워크샵 페이지 생성 중...")
        create_week2_page(parent_page_id, submissions_db_id)
        create_week3_page(parent_page_id, submissions_db_id)
        create_week4_page(parent_page_id, submissions_db_id)
        create_week5_page(parent_page_id, submissions_db_id)
        create_week6_page(parent_page_id, submissions_db_id)

        # 완료
        print("\n" + "=" * 60)
        print("✅ 모든 Notion 워크샵 구조가 생성되었습니다!")
        print("=" * 60)
        print(f"\n📊 Student Submissions Database ID: {submissions_db_id}")
        print(f"🧪 AI Recipe Library Database ID: {recipe_db_id}")
        print("\n⚠️  다음 단계: Template Button 수동 설정 (25분)")
        print("   각 Week 페이지에서 '/template' 입력 후 '내 실험 영역 만들기' 버튼 추가")
        print("\n🎉 학생 초대 후 워크샵을 시작하세요!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
