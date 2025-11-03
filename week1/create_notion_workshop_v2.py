#!/usr/bin/env python3
"""
Week 1 Workshop - Notion 페이지 자동 생성 스크립트 (간단 버전)

Notion API 제약사항을 고려한 안정적인 버전
"""

import os
import argparse
from notion_client import Client

def create_workshop(page_id: str, token: str = None):
    """Notion 페이지에 Week 1 워크샵 구조 생성"""

    if token is None:
        token = os.getenv('NOTION_TOKEN')

    if not token:
        raise ValueError("NOTION_TOKEN이 필요합니다.")

    notion = Client(auth=token)
    print("🚀 Week 1 Workshop 생성 시작...")

    # ============================================================
    # 1. 메인 타이틀 + 원칙 참조
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {
                    "rich_text": [{"type": "text", "text": {"content": "📚 Week 1: Human-Centered Writing Workshop"}}]
                }
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{"type": "text", "text": {"content": "10명 학생용 실시간 협업 워크샵 | 50분 | Bad Sentences → Bad Paragraphs → Smart Revising"}}],
                    "icon": {"emoji": "⏱️"},
                    "color": "blue_background"
                }
            },
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },
            # Week 1 원칙 (3컬럼 레이아웃)
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "📚 Week 1 원칙 참조"}}],
                    "color": "blue_background"
                }
            },
            {
                "object": "block",
                "type": "column_list",
                "column_list": {
                    "children": [
                        # Lesson 1
                        {
                            "object": "block",
                            "type": "column",
                            "column": {
                                "children": [
                                    {
                                        "object": "block",
                                        "type": "heading_3",
                                        "heading_3": {"rich_text": [{"type": "text", "text": {"content": "Lesson 1: 주어-동사"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "동작을 동사에 담기"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "주체를 주어에 두기"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "주어-동사 가깝게"}}]}
                                    }
                                ]
                            }
                        },
                        # Lesson 2
                        {
                            "object": "block",
                            "type": "column",
                            "column": {
                                "children": [
                                    {
                                        "object": "block",
                                        "type": "heading_3",
                                        "heading_3": {"rich_text": [{"type": "text", "text": {"content": "Lesson 2: 응집성"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Old → New 흐름"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "전략적 수동태"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "문단 응집성"}}]}
                                    }
                                ]
                            }
                        },
                        # Lesson 3
                        {
                            "object": "block",
                            "type": "column",
                            "column": {
                                "children": [
                                    {
                                        "object": "block",
                                        "type": "heading_3",
                                        "heading_3": {"rich_text": [{"type": "text", "text": {"content": "Lesson 3: 간결성"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "불필요한 단어 제거"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "간단한 언어"}}]}
                                    },
                                    {
                                        "object": "block",
                                        "type": "bulleted_list_item",
                                        "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "수식어 제한"}}]}
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            }
        ]
    )
    print("✅ 메인 타이틀 + 원칙 생성 완료")

    # ============================================================
    # 2. STAGE 1A Header
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "🔬 STAGE 1A: Bad Sentences 수술실 (15분)"}}],
                    "color": "yellow_background"
                }
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{"type": "text", "text": {"content": "필수 3개(#1, #5, #9) + 선택 2개 | 7분 개인 → 5분 페어 → 3분 모범 답안"}}],
                    "icon": {"emoji": "⏱️"}
                }
            }
        ]
    )

    # Bad Sentences Database
    bad_sentences_db = notion.databases.create(
        parent={"type": "page_id", "page_id": page_id},
        title=[{"type": "text", "text": {"content": "Bad Sentences 작업 현황"}}],
        properties={
            "문장": {"title": {}},
            "학생": {
                "select": {
                    "options": [
                        {"name": f"학생{chr(65+i)}", "color": ["default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red"][i]}
                        for i in range(10)
                    ]
                }
            },
            "문제점": {"rich_text": {}},
            "수정안": {"rich_text": {}},
            "상태": {
                "select": {
                    "options": [
                        {"name": "⏳ 대기", "color": "gray"},
                        {"name": "🔄 작업중", "color": "yellow"},
                        {"name": "✅ 완료", "color": "green"}
                    ]
                }
            }
        }
    )
    print(f"DEBUG: Database ID: {bad_sentences_db['id']}")
    import json
    # Query the database to get properties
    db_retrieved = notion.databases.retrieve(bad_sentences_db['id'])
    with open('/tmp/notion_db_retrieved.json', 'w') as f:
        json.dump(db_retrieved, f, indent=2, ensure_ascii=False)
    print(f"DEBUG: Retrieved database saved to /tmp/notion_db_retrieved.json")
    if 'properties' in db_retrieved:
        print(f"DEBUG: Properties in retrieved DB: {list(db_retrieved['properties'].keys())}")

    # 필수 3개 문장
    sentences = [
        ("#1: Nominalization", "The ABC database has been subject to different improvements, modifications, and extensions in structure and content over the years."),
        ("#5: Old→New 흐름", "Detecting positive Darwinian selection at the DNA sequence level has been a subject of considerable interest."),
        ("#9: 복잡한 주어", "To identify RNAs associated with each putative RBP, C-terminal tandem affinity purification (TAP)-tagged proteins were affinity purified and associated RNAs were identified.")
    ]

    for title, original in sentences:
        notion.pages.create(
            parent={"type": "database_id", "database_id": bad_sentences_db["id"]},
            properties={
                "문장": {"title": [{"text": {"content": title}}]},
                "상태": {"select": {"name": "⏳ 대기"}}
            },
            children=[
                {
                    "object": "block",
                    "type": "quote",
                    "quote": {"rich_text": [{"type": "text", "text": {"content": f"원문: {original}"}}], "color": "gray_background"}
                }
            ]
        )

    print("✅ STAGE 1A Database 생성 완료 (3개 문장)")

    # ============================================================
    # 3. STAGE 1B Header
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "📄 STAGE 1B: Bad Paragraphs from Real Papers (15분)"}}],
                    "color": "orange_background"
                }
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{"type": "text", "text": {"content": "PLOS ONE 2019 실제 논문 | 4개 문단 중 2개 선택 | 8분 개인 → 5분 피어 → 2분 모범 답안"}}],
                    "icon": {"emoji": "📰"}
                }
            }
        ]
    )

    # Bad Paragraphs Database
    bad_paragraphs_db = notion.databases.create(
        parent={"type": "page_id", "page_id": page_id},
        title=[{"type": "text", "text": {"content": "Bad Paragraphs 작업 현황"}}],
        properties={
            "문단": {"title": {}},
            "학생": {
                "select": {
                    "options": [
                        {"name": f"학생{chr(65+i)}", "color": ["default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red"][i]}
                        for i in range(10)
                    ]
                }
            },
            "문제점": {"rich_text": {}},
            "개선안": {"rich_text": {}},
            "상태": {
                "select": {
                    "options": [
                        {"name": "⏳ 대기", "color": "gray"},
                        {"name": "🔄 작업중", "color": "yellow"},
                        {"name": "✅ 완료", "color": "green"}
                    ]
                }
            },
            "원문 단어수": {"number": {}},
            "개선 단어수": {"number": {}}
        }
    )

    paragraphs = [
        ("P1: Abstract - 수동태 + Nominalization", 44),
        ("P2: Introduction - 주어-동사 거리", 52),
        ("P3: Introduction - Old→New 흐름", 58),
        ("P4: Introduction - 간결성", 65)
    ]

    for title, words in paragraphs:
        notion.pages.create(
            parent={"type": "database_id", "database_id": bad_paragraphs_db["id"]},
            properties={
                "문단": {"title": [{"text": {"content": title}}]},
                "상태": {"select": {"name": "⏳ 대기"}},
                "원문 단어수": {"number": words}
            }
        )

    print("✅ STAGE 1B Database 생성 완료 (4개 문단)")

    # ============================================================
    # 4. STAGE 2 Header
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {
                    "rich_text": [{"type": "text", "text": {"content": "✅ STAGE 2: Smart Revising (20분)"}}],
                    "color": "green_background"
                }
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{"type": "text", "text": {"content": "본인 초록 7단계 체크리스트 | 10분 개인 → 8분 페어 → 2분 정리"}}],
                    "icon": {"emoji": "📋"}
                }
            }
        ]
    )

    # Smart Revising Database
    smart_revising_db = notion.databases.create(
        parent={"type": "page_id", "page_id": page_id},
        title=[{"type": "text", "text": {"content": "Smart Revising 작업 현황"}}],
        properties={
            "학생": {"title": {}},
            "페어": {"select": {"options": [{"name": f"학생{chr(65+i)}"} for i in range(10)]}},
            "Step 1: Nominalization": {"checkbox": {}},
            "Step 2: 주어 확인": {"checkbox": {}},
            "Step 3: Old→New": {"checkbox": {}},
            "Step 4: 문단 응집성": {"checkbox": {}},
            "Step 5: 소리내어": {"checkbox": {}},
            "Step 6: 동료 피드백": {"checkbox": {}},
            "Step 7: 불필요한 단어": {"checkbox": {}},
            "상태": {
                "select": {
                    "options": [
                        {"name": "⏳ 시작 전", "color": "gray"},
                        {"name": "🔄 진행중", "color": "yellow"},
                        {"name": "📝 피드백 대기", "color": "blue"},
                        {"name": "✅ 완료", "color": "green"}
                    ]
                }
            }
        }
    )

    # 10명 학생 페어
    students = [
        ("학생A", "학생B"), ("학생B", "학생A"),
        ("학생C", "학생D"), ("학생D", "학생C"),
        ("학생E", "학생F"), ("학생F", "학생E"),
        ("학생G", "학생H"), ("학생H", "학생G"),
        ("학생I", "학생J"), ("학생J", "학생I")
    ]

    for student, pair in students:
        notion.pages.create(
            parent={"type": "database_id", "database_id": smart_revising_db["id"]},
            properties={
                "학생": {"title": [{"text": {"content": student}}]},
                "페어": {"select": {"name": pair}},
                "상태": {"select": {"name": "⏳ 시작 전"}}
            },
            children=[
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": "📄 내 초록 (원문)"}}]}
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": "[여기에 초록을 붙여넣으세요]"}}], "color": "gray_background"}
                },
                {
                    "object": "block",
                    "type": "divider",
                    "divider": {}
                },
                {
                    "object": "block",
                    "type": "toggle",
                    "toggle": {
                        "rich_text": [{"type": "text", "text": {"content": "▶ Step 1: Nominalization 찾기"}}],
                        "children": [
                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "발견한 Nominalization (-tion, -ment, -ance, -ence):"}}]}}
                        ]
                    }
                },
                {
                    "object": "block",
                    "type": "toggle",
                    "toggle": {
                        "rich_text": [{"type": "text", "text": {"content": "▶ Step 2: 주어 확인"}}],
                        "children": [
                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "주제 vs 주어 일치 여부:"}}]}}
                        ]
                    }
                },
                {
                    "object": "block",
                    "type": "toggle",
                    "toggle": {
                        "rich_text": [{"type": "text", "text": {"content": "▶ Step 3-7: 나머지 단계"}}],
                        "children": [
                            {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "Old→New, 문단 응집성, 소리내어, 동료 피드백, 불필요한 단어"}}]}}
                        ]
                    }
                },
                {
                    "object": "block",
                    "type": "divider",
                    "divider": {}
                },
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": f"💬 Peer Feedback (from {pair})"}}]}
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": f"[{pair}님이 댓글로 피드백을 남깁니다]"}}], "color": "blue_background"}
                },
                {
                    "object": "block",
                    "type": "divider",
                    "divider": {}
                },
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {"rich_text": [{"type": "text", "text": {"content": "📝 최종 수정 버전"}}]}
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"type": "text", "text": {"content": "[7단계를 모두 적용한 최종 버전]"}}], "color": "green_background"}
                }
            ]
        )

    print("✅ STAGE 2 Database 생성 완료 (10명 학생)")

    # ============================================================
    # 5. 마무리
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "divider",
                "divider": {}
            },
            {
                "object": "block",
                "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": "🎉 워크샵 완료!"}}]}
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [{"type": "text", "text": {"content": "과제: 전체 초록을 7-Step Checklist로 재점검 + Week 2용 초록 준비 (AI로 Nature/Science급 개선)"}}],
                    "icon": {"emoji": "📚"},
                    "color": "blue_background"
                }
            }
        ]
    )

    print("✅ 마무리 섹션 완료")
    print("\n🎉 Week 1 Workshop 생성 완료!")
    print(f"📌 Notion 페이지: https://notion.so/{page_id}")

def main():
    parser = argparse.ArgumentParser(description='Week 1 Workshop Notion 페이지 자동 생성')
    parser.add_argument('--page-id', required=True, help='Notion 페이지 ID')
    parser.add_argument('--token', help='Notion Integration Token')
    args = parser.parse_args()

    try:
        create_workshop(page_id=args.page_id, token=args.token)
    except Exception as e:
        print(f"❌ 오류: {e}")
        return 1

    return 0

if __name__ == '__main__':
    exit(main())
