#!/usr/bin/env python3
"""
Week 1 Workshop - Notion 페이지 자동 생성 스크립트

사용 방법:
1. Notion Integration Token 발급: https://www.notion.so/my-integrations
2. 환경변수 설정: export NOTION_TOKEN="your_token"
3. 실행: python create_notion_workshop.py --page-id 29a41454561d809f871eef8102006369

또는:
python create_notion_workshop.py --page-id 29a41454561d809f871eef8102006369 --token "your_token"
"""

import os
import argparse
from notion_client import Client

def create_workshop(page_id: str, token: str = None):
    """
    Notion 페이지에 Week 1 워크샵 구조 생성

    Args:
        page_id: Notion 페이지 ID (29a41454561d809f871eef8102006369)
        token: Notion Integration Token (환경변수 NOTION_TOKEN 또는 직접 전달)
    """

    # Token 설정
    if token is None:
        token = os.getenv('NOTION_TOKEN')

    if not token:
        raise ValueError(
            "Notion Token이 필요합니다.\n"
            "방법 1: export NOTION_TOKEN='your_token'\n"
            "방법 2: --token 'your_token' 옵션 사용"
        )

    # Notion Client 초기화
    notion = Client(auth=token)

    print("🚀 Week 1 Workshop 생성 시작...")

    # ============================================================
    # 1. 메인 타이틀
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
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {"type": "text", "text": {"content": "10명 학생용 실시간 협업 워크샵 | 50분"}}
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
    print("✅ 메인 타이틀 생성 완료")

    # ============================================================
    # 2. Week 1 원칙 참조 (Synced Block)
    # ============================================================
    synced_block = notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "synced_block",
                "synced_block": {
                    "synced_from": None,  # Original synced block
                    "children": [
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
                                    # Column 1: Lesson 1
                                    {
                                        "object": "block",
                                        "type": "column",
                                        "column": {
                                            "children": [
                                                {
                                                    "object": "block",
                                                    "type": "heading_3",
                                                    "heading_3": {
                                                        "rich_text": [{"type": "text", "text": {"content": "Lesson 1: 주어-동사"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "동작을 동사에 담기"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "주체를 주어에 두기"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "주어-동사 가깝게 (10 words 이내)"}}]
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                    # Column 2: Lesson 2
                                    {
                                        "object": "block",
                                        "type": "column",
                                        "column": {
                                            "children": [
                                                {
                                                    "object": "block",
                                                    "type": "heading_3",
                                                    "heading_3": {
                                                        "rich_text": [{"type": "text", "text": {"content": "Lesson 2: 응집성"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "Old → New 정보 흐름"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "전략적 수동태"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "문단 응집성"}}]
                                                    }
                                                }
                                            ]
                                        }
                                    },
                                    # Column 3: Lesson 3
                                    {
                                        "object": "block",
                                        "type": "column",
                                        "column": {
                                            "children": [
                                                {
                                                    "object": "block",
                                                    "type": "heading_3",
                                                    "heading_3": {
                                                        "rich_text": [{"type": "text", "text": {"content": "Lesson 3: 간결성"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "불필요한 단어 제거"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "간단한 언어"}}]
                                                    }
                                                },
                                                {
                                                    "object": "block",
                                                    "type": "bulleted_list_item",
                                                    "bulleted_list_item": {
                                                        "rich_text": [{"type": "text", "text": {"content": "수식어 제한"}}]
                                                    }
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    )
    print("✅ Week 1 원칙 참조 생성 완료")

    # ============================================================
    # 3. STAGE 1A: Bad Sentences Database
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
                    "rich_text": [
                        {"type": "text", "text": {"content": "진행: 필수 3개(#1, #5, #9) + 선택 2개 | 7분 개인 작업 → 5분 페어 비교 → 3분 모범 답안"}}
                    ],
                    "icon": {"emoji": "⏱️"},
                    "color": "gray_background"
                }
            }
        ]
    )

    # Database for Bad Sentences
    bad_sentences_db = notion.databases.create(
        parent={"page_id": page_id},
        title=[{"type": "text", "text": {"content": "Bad Sentences 작업 현황"}}],
        properties={
            "문장": {"title": {}},
            "학생": {"select": {}},
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
            },
            "Peer Feedback": {"rich_text": {}}
        }
    )

    # 필수 3개 문장 추가
    sentences = [
        {
            "title": "#1: Nominalization",
            "original": "The ABC database has been subject to different improvements, modifications, and extensions..."
        },
        {
            "title": "#5: Old→New 흐름",
            "original": "Detecting positive Darwinian selection at the DNA sequence level has been a subject of considerable interest."
        },
        {
            "title": "#9: 복잡한 주어",
            "original": "To identify RNAs associated with each putative RBP, C-terminal tandem affinity purification (TAP)-tagged proteins..."
        }
    ]

    for sentence in sentences:
        notion.pages.create(
            parent={"database_id": bad_sentences_db["id"]},
            properties={
                "문장": {"title": [{"text": {"content": sentence["title"]}}]},
                "상태": {"select": {"name": "⏳ 대기"}}
            },
            children=[
                {
                    "object": "block",
                    "type": "quote",
                    "quote": {
                        "rich_text": [{"type": "text", "text": {"content": sentence["original"]}}],
                        "color": "gray_background"
                    }
                }
            ]
        )

    print("✅ STAGE 1A Database 생성 완료 (3개 필수 문장)")

    # ============================================================
    # 4. STAGE 1B: Bad Paragraphs Database
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
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
                    "rich_text": [
                        {"type": "text", "text": {"content": "PLOS ONE 2024 실제 논문 | 4개 문단 중 2개 선택 | 8분 개인 → 5분 피어 리뷰 → 2분 모범 답안"}}
                    ],
                    "icon": {"emoji": "📰"},
                    "color": "gray_background"
                }
            }
        ]
    )

    bad_paragraphs_db = notion.databases.create(
        parent={"page_id": page_id},
        title=[{"type": "text", "text": {"content": "Bad Paragraphs 작업 현황"}}],
        properties={
            "문단": {"title": {}},
            "학생": {"select": {}},
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
            "단어수 개선": {"number": {}}
        }
    )

    paragraphs = [
        {"title": "P1: Abstract - 수동태 + Nominalization", "words": 44},
        {"title": "P2: Introduction - 주어-동사 거리", "words": 52},
        {"title": "P3: Introduction - Old→New 흐름", "words": 58},
        {"title": "P4: Introduction - 간결성", "words": 65}
    ]

    for para in paragraphs:
        notion.pages.create(
            parent={"database_id": bad_paragraphs_db["id"]},
            properties={
                "문단": {"title": [{"text": {"content": para["title"]}}]},
                "상태": {"select": {"name": "⏳ 대기"}},
                "단어수 개선": {"number": para["words"]}
            }
        )

    print("✅ STAGE 1B Database 생성 완료 (4개 문단)")

    # ============================================================
    # 5. STAGE 2: Smart Revising Database (10명 학생)
    # ============================================================
    notion.blocks.children.append(
        block_id=page_id,
        children=[
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
                    "rich_text": [
                        {"type": "text", "text": {"content": "본인 초록 7단계 체크리스트 | 10분 개인 → 8분 페어 피드백 → 2분 정리"}}
                    ],
                    "icon": {"emoji": "📋"},
                    "color": "gray_background"
                }
            }
        ]
    )

    smart_revising_db = notion.databases.create(
        parent={"page_id": page_id},
        title=[{"type": "text", "text": {"content": "Smart Revising 작업 현황"}}],
        properties={
            "학생": {"title": {}},
            "페어": {"select": {}},
            "Step 1": {"checkbox": {}},
            "Step 2": {"checkbox": {}},
            "Step 3": {"checkbox": {}},
            "Step 4": {"checkbox": {}},
            "Step 5": {"checkbox": {}},
            "Step 6": {"checkbox": {}},
            "Step 7": {"checkbox": {}},
            "진행률": {"number": {}},
            "단어수 개선": {"rich_text": {}},
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

    # 10명 학생 초기 설정
    students = [
        ("학생A", "학생B"),
        ("학생B", "학생A"),
        ("학생C", "학생D"),
        ("학생D", "학생C"),
        ("학생E", "학생F"),
        ("학생F", "학생E"),
        ("학생G", "학생H"),
        ("학생H", "학생G"),
        ("학생I", "학생J"),
        ("학생J", "학생I")
    ]

    for student, pair in students:
        student_page = notion.pages.create(
            parent={"database_id": smart_revising_db["id"]},
            properties={
                "학생": {"title": [{"text": {"content": student}}]},
                "페어": {"select": {"name": pair}},
                "진행률": {"number": 0},
                "상태": {"select": {"name": "⏳ 시작 전"}}
            },
            children=[
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [{"type": "text", "text": {"content": "📄 내 초록 (원문)"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": "[여기에 초록을 붙여넣으세요]"}}],
                        "color": "gray_background"
                    }
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
                        "rich_text": [{"type": "text", "text": {"content": "✅ Step 1: Nominalization 찾기"}}],
                        "children": [
                            {
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": [{"type": "text", "text": {"content": "발견한 Nominalization:"}}]
                                }
                            }
                        ]
                    }
                },
                {
                    "object": "block",
                    "type": "toggle",
                    "toggle": {
                        "rich_text": [{"type": "text", "text": {"content": "✅ Step 2: 주어 확인"}}],
                        "children": [
                            {
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": [{"type": "text", "text": {"content": "주제 vs 주어 일치 여부:"}}]
                                }
                            }
                        ]
                    }
                },
                {
                    "object": "block",
                    "type": "toggle",
                    "toggle": {
                        "rich_text": [{"type": "text", "text": {"content": "✅ Step 3-7"}}],
                        "children": [
                            {
                                "object": "block",
                                "type": "paragraph",
                                "paragraph": {
                                    "rich_text": [{"type": "text", "text": {"content": "나머지 단계 진행..."}}]
                                }
                            }
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
                    "heading_3": {
                        "rich_text": [{"type": "text", "text": {"content": f"💬 Peer Feedback (from {pair})"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": f"[{pair}님이 댓글로 피드백을 남깁니다]"}}],
                        "color": "blue_background"
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
                    "heading_3": {
                        "rich_text": [{"type": "text", "text": {"content": "📝 최종 수정 버전"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"type": "text", "text": {"content": "[7단계를 모두 적용한 최종 버전]"}}],
                        "color": "green_background"
                    }
                }
            ]
        )

    print("✅ STAGE 2 Database 생성 완료 (10명 학생)")

    # ============================================================
    # 6. 마무리 및 과제 안내
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
                    "rich_text": [{"type": "text", "text": {"content": "🎉 워크샵 완료!"}}]
                }
            },
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [
                        {"type": "text", "text": {"content": "다음 주 과제: 전체 초록을 7-Step Checklist로 재점검 + Week 2용 초록 준비 (AI로 Nature/Science급 개선 예정)"}}
                    ],
                    "icon": {"emoji": "📚"},
                    "color": "blue_background"
                }
            }
        ]
    )

    print("✅ 마무리 섹션 생성 완료")
    print("\n🎉 Week 1 Workshop 생성 완료!")
    print(f"📌 Notion 페이지를 확인하세요: https://notion.so/{page_id}")


def main():
    parser = argparse.ArgumentParser(
        description='Week 1 Workshop Notion 페이지 자동 생성',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python create_notion_workshop.py --page-id 29a41454561d809f871eef8102006369
  python create_notion_workshop.py --page-id 29a41454561d809f871eef8102006369 --token "secret_xxx"

환경변수:
  NOTION_TOKEN    Notion Integration Token
        """
    )

    parser.add_argument(
        '--page-id',
        required=True,
        help='Notion 페이지 ID (예: 29a41454561d809f871eef8102006369)'
    )

    parser.add_argument(
        '--token',
        help='Notion Integration Token (또는 환경변수 NOTION_TOKEN 사용)'
    )

    args = parser.parse_args()

    try:
        create_workshop(page_id=args.page_id, token=args.token)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        print("\n문제 해결:")
        print("1. Notion Integration Token이 설정되었는지 확인")
        print("2. Integration이 페이지에 연결되었는지 확인 (페이지 우측 상단 ⋯ → Add connections)")
        print("3. 페이지 ID가 정확한지 확인")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
