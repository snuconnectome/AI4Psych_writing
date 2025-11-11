#!/usr/bin/env python3
"""
Notion 페이지 제목 변경

사용법:
    python update_page_title.py <page_id> <new_title>
"""

import os
import sys
from notion_client import Client

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')


def update_page_title(page_id: str, new_title: str):
    """Notion 페이지 제목 변경"""

    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    notion = Client(auth=NOTION_TOKEN)

    try:
        # 페이지 제목 업데이트
        notion.pages.update(
            page_id=page_id,
            properties={
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": new_title
                            }
                        }
                    ]
                }
            }
        )

        print(f"✅ 페이지 제목이 '{new_title}'로 변경되었습니다!")
        print(f"🔗 https://notion.so/{page_id.replace('-', '')}")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    if len(sys.argv) < 3:
        print("사용법: python update_page_title.py <page_id> <new_title>")
        print("예시: python update_page_title.py 2a141454561d8010b79af877915af316 'v2'")
        return

    page_id = sys.argv[1].strip()
    new_title = sys.argv[2].strip()

    # URL에서 ID 추출
    if 'notion.so/' in page_id:
        page_id = page_id.split('notion.so/')[-1].split('?')[0]

    # 하이픈 없는 ID를 하이픈 있는 형식으로 변환
    if '-' not in page_id and len(page_id) == 32:
        page_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"

    update_page_title(page_id, new_title)


if __name__ == '__main__':
    main()
