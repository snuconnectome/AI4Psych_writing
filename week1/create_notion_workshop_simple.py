#!/usr/bin/env python3
"""
Notion Workshop 간단 버전 자동 생성 스크립트 (Week 2-6)
핵심 구조만 생성 후 Notion에서 콘텐츠 추가

사용법:
    python create_notion_workshop_simple.py <parent_page_id>
"""

import os
import sys
import requests
from typing import Dict, List

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_API_URL = 'https://api.notion.com/v1'
HEADERS = {
    'Authorization': f'Bearer {NOTION_TOKEN}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}


def create_page(parent_id: str, title: str, icon: str = None) -> Dict:
    """새 페이지 생성"""
    payload = {
        'parent': {'page_id': parent_id},
        'properties': {
            'title': {'title': [{'text': {'content': title}}]}
        }
    }
    if icon:
        payload['icon'] = {'type': 'emoji', 'emoji': icon}

    response = requests.post(f'{NOTION_API_URL}/pages', headers=HEADERS, json=payload)
    if not response.ok:
        print(f"Error: {response.text}")
    response.raise_for_status()
    return response.json()


def create_database(parent_id: str, title: str, properties: Dict) -> Dict:
    """새 데이터베이스 생성"""
    payload = {
        'parent': {'page_id': parent_id},
        'title': [{'text': {'content': title}}],
        'properties': properties
    }

    response = requests.post(f'{NOTION_API_URL}/databases', headers=HEADERS, json=payload)
    if not response.ok:
        print(f"Database Error: {response.text}")
    response.raise_for_status()
    return response.json()


def add_simple_blocks(page_id: str, blocks: List[Dict]) -> Dict:
    """간단한 블록 추가"""
    payload = {'children': blocks}
    response = requests.patch(f'{NOTION_API_URL}/blocks/{page_id}/children', headers=HEADERS, json=payload)
    if not response.ok:
        print(f"Blocks Error: {response.text}")
    response.raise_for_status()
    return response.json()


def create_student_db(parent_id: str) -> str:
    """Student Submissions Database"""
    properties = {
        'Name': {'type': 'title', 'title': {}},
        '학생': {'type': 'people', 'people': {}},
        'Week': {'type': 'select', 'select': {'options': [
            {'name': 'Week 2', 'color': 'blue'},
            {'name': 'Week 3', 'color': 'green'},
            {'name': 'Week 4', 'color': 'yellow'},
            {'name': 'Week 5', 'color': 'red'},
            {'name': 'Week 6', 'color': 'purple'}
        ]}},
        'Section': {'type': 'select', 'select': {'options': [
            {'name': 'Abstract', 'color': 'blue'},
            {'name': 'Introduction', 'color': 'green'},
            {'name': 'Methods', 'color': 'yellow'},
            {'name': 'Results', 'color': 'red'},
            {'name': 'Discussion', 'color': 'purple'}
        ]}},
        'Status': {'type': 'select', 'select': {'options': [
            {'name': 'Not Started', 'color': 'gray'},
            {'name': 'In Progress', 'color': 'blue'},
            {'name': 'Submitted', 'color': 'yellow'},
            {'name': 'Peer Reviewed', 'color': 'green'},
            {'name': 'Revised', 'color': 'purple'}
        ]}},
        'Peer Score': {'type': 'number', 'number': {}},
        'Peer Feedback': {'type': 'rich_text', 'rich_text': {}}
    }

    db = create_database(parent_id, '📊 Student Submissions', properties)
    print(f"✅ Created Student Submissions DB: {db['id']}")
    return db['id']


def create_recipe_db(parent_id: str) -> str:
    """AI Recipe Library Database"""
    properties = {
        'Recipe Name': {'type': 'title', 'title': {}},
        'Week': {'type': 'select', 'select': {'options': [
            {'name': 'Week 2', 'color': 'blue'},
            {'name': 'Week 3', 'color': 'green'},
            {'name': 'Week 4', 'color': 'yellow'},
            {'name': 'Week 5', 'color': 'red'},
            {'name': 'Week 6', 'color': 'purple'}
        ]}},
        'Category': {'type': 'select', 'select': {'options': [
            {'name': 'Opening', 'color': 'blue'},
            {'name': 'Gap', 'color': 'green'},
            {'name': 'Methods', 'color': 'yellow'},
            {'name': 'Results', 'color': 'red'},
            {'name': 'Discussion', 'color': 'purple'}
        ]}},
        'Prompt': {'type': 'rich_text', 'rich_text': {}},
        'Success Rate': {'type': 'number', 'number': {}},
        'Submitted By': {'type': 'people', 'people': {}}
    }

    db = create_database(parent_id, '🧪 AI Recipe Library', properties)
    print(f"✅ Created AI Recipe Library DB: {db['id']}")
    return db['id']


def create_week_page(parent_id: str, week_num: int, title: str, submissions_db_id: str) -> str:
    """Week 페이지 생성 (간단 버전)"""
    page = create_page(parent_id, f'Week {week_num}: {title}', '📅')
    page_id = page['id']

    # 간단한 블록만 추가
    blocks = [
        {
            'type': 'heading_1',
            'heading_1': {
                'rich_text': [{'type': 'text', 'text': {'content': f'📚 Week {week_num} 워크샵'}}],
                'color': 'blue_background'
            }
        },
        {
            'type': 'paragraph',
            'paragraph': {
                'rich_text': [{'type': 'text', 'text': {'content': f'{title} 전략과 AI 프롬프트 레시피'}}]
            }
        },
        {
            'type': 'divider',
            'divider': {}
        },
        {
            'type': 'heading_2',
            'heading_2': {
                'rich_text': [{'type': 'text', 'text': {'content': '🧪 학생 제출물'}}]
            }
        },
        {
            'type': 'paragraph',
            'paragraph': {
                'rich_text': [{'type': 'text', 'text': {'content': 'Database를 수동으로 링크하세요: /database → Student Submissions 선택'}}]
            }
        }
    ]

    add_simple_blocks(page_id, blocks)
    print(f"✅ Created Week {week_num} Page: {page_id}")
    return page_id


def main():
    print("="*60)
    print("Notion Workshop 간단 버전 생성 (Week 2-6)")
    print("="*60)

    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수 필요")
        return

    if len(sys.argv) > 1:
        parent_id = sys.argv[1].strip()
    else:
        parent_id = input("Parent 페이지 ID: ").strip()

    if not parent_id:
        print("❌ Error: Parent ID 필요")
        return

    try:
        print(f"\n📍 Parent: {parent_id}\n")

        # Step 1: Databases
        print("📊 Step 1: Databases 생성...")
        submissions_db = create_student_db(parent_id)
        recipe_db = create_recipe_db(parent_id)

        # Step 2: Week Pages
        print("\n📅 Step 2: Week 페이지 생성...")
        create_week_page(parent_id, 2, 'Nature/Science급 초록 작성', submissions_db)
        create_week_page(parent_id, 3, '체계적 Research Gap 발견', submissions_db)
        create_week_page(parent_id, 4, 'Methods/Results Bulletproofing', submissions_db)
        create_week_page(parent_id, 5, 'Discussion Section', submissions_db)
        create_week_page(parent_id, 6, 'Final Polish & Peer Review', submissions_db)

        print("\n"+"="*60)
        print("✅ 기본 구조 생성 완료!")
        print("="*60)
        print(f"\n📊 Student Submissions DB: {submissions_db}")
        print(f"🧪 AI Recipe Library DB: {recipe_db}")
        print("\n⚠️  다음 단계:")
        print("1. 각 Week 페이지에서 강의 자료 추가")
        print("2. Template Button 설정")
        print("3. Database 링크 연결")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
