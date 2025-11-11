#!/usr/bin/env python3
"""
Notion 페이지를 Markdown으로 다운로드

사용법:
    python download_notion_to_md.py <page_id> [output_file]
"""

import os
import sys
from typing import List, Dict, Any
from notion_client import Client

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')


def notion_blocks_to_markdown(blocks: List[Dict[str, Any]]) -> str:
    """Notion blocks를 Markdown으로 변환"""
    markdown_lines = []

    for block in blocks:
        block_type = block['type']

        # Heading 1
        if block_type == 'heading_1':
            text = extract_text(block['heading_1']['rich_text'])
            markdown_lines.append(f"# {text}\n")

        # Heading 2
        elif block_type == 'heading_2':
            text = extract_text(block['heading_2']['rich_text'])
            markdown_lines.append(f"## {text}\n")

        # Heading 3
        elif block_type == 'heading_3':
            text = extract_text(block['heading_3']['rich_text'])
            markdown_lines.append(f"### {text}\n")

        # Paragraph
        elif block_type == 'paragraph':
            text = extract_text(block['paragraph']['rich_text'])
            if text:
                markdown_lines.append(f"{text}\n")

        # Bulleted list item
        elif block_type == 'bulleted_list_item':
            text = extract_text(block['bulleted_list_item']['rich_text'])
            markdown_lines.append(f"- {text}\n")

        # Numbered list item
        elif block_type == 'numbered_list_item':
            text = extract_text(block['numbered_list_item']['rich_text'])
            markdown_lines.append(f"1. {text}\n")

        # Quote
        elif block_type == 'quote':
            text = extract_text(block['quote']['rich_text'])
            markdown_lines.append(f"> {text}\n")

        # Code
        elif block_type == 'code':
            text = extract_text(block['code']['rich_text'])
            language = block['code'].get('language', 'plain text')
            markdown_lines.append(f"```{language}\n{text}\n```\n")

        # Divider
        elif block_type == 'divider':
            markdown_lines.append("---\n")

        # Callout
        elif block_type == 'callout':
            icon = block['callout'].get('icon', {})
            if icon.get('type') == 'emoji':
                emoji = icon.get('emoji', '')
                text = extract_text(block['callout']['rich_text'])
                markdown_lines.append(f"> {emoji} {text}\n")
            else:
                text = extract_text(block['callout']['rich_text'])
                markdown_lines.append(f"> {text}\n")

        # Table (stored as code block in our upload, but may be different on download)
        elif block_type == 'table':
            # Tables need special handling - for now, mark as table
            markdown_lines.append("\n<!-- Table block detected - manual conversion may be needed -->\n")

        # Child blocks (nested content)
        if block.get('has_children'):
            # Recursively get child blocks
            child_blocks = get_block_children(block['id'])
            child_markdown = notion_blocks_to_markdown(child_blocks)
            # Indent child content
            indented = '\n'.join('  ' + line if line.strip() else line
                                for line in child_markdown.split('\n'))
            markdown_lines.append(indented)

    return '\n'.join(markdown_lines)


def extract_text(rich_text_array: List[Dict[str, Any]]) -> str:
    """Rich text 배열에서 plain text 추출"""
    if not rich_text_array:
        return ""

    text_parts = []
    for text_obj in rich_text_array:
        if text_obj['type'] == 'text':
            content = text_obj['text']['content']

            # Handle formatting
            annotations = text_obj.get('annotations', {})
            if annotations.get('bold'):
                content = f"**{content}**"
            if annotations.get('italic'):
                content = f"*{content}*"
            if annotations.get('code'):
                content = f"`{content}`"
            if annotations.get('strikethrough'):
                content = f"~~{content}~~"

            text_parts.append(content)

    return ''.join(text_parts)


def get_block_children(block_id: str) -> List[Dict[str, Any]]:
    """블록의 자식 블록들을 가져옴"""
    notion = Client(auth=NOTION_TOKEN)

    all_children = []
    has_more = True
    start_cursor = None

    while has_more:
        response = notion.blocks.children.list(
            block_id=block_id,
            start_cursor=start_cursor
        )
        all_children.extend(response['results'])
        has_more = response['has_more']
        start_cursor = response.get('next_cursor')

    return all_children


def download_from_notion(page_id: str, output_file: str = None):
    """Notion 페이지를 Markdown 파일로 다운로드"""

    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    # Notion 클라이언트 초기화
    notion = Client(auth=NOTION_TOKEN)

    print("="*60)
    print("Notion → Markdown 다운로드")
    print("="*60)

    try:
        # 페이지 정보 가져오기
        print(f"📖 Fetching page: {page_id}...")
        page = notion.pages.retrieve(page_id=page_id)

        # 페이지 타이틀 추출
        title_property = page.get('properties', {}).get('title', {})
        if title_property:
            title_array = title_property.get('title', [])
            if title_array:
                page_title = title_array[0].get('plain_text', 'Untitled')
            else:
                page_title = 'Untitled'
        else:
            page_title = 'Untitled'

        print(f"✅ Found page: {page_title}")

        # 모든 블록 가져오기
        print(f"🔄 Fetching all blocks...")
        all_blocks = []
        has_more = True
        start_cursor = None

        while has_more:
            response = notion.blocks.children.list(
                block_id=page_id,
                start_cursor=start_cursor,
                page_size=100
            )
            all_blocks.extend(response['results'])
            has_more = response['has_more']
            start_cursor = response.get('next_cursor')
            print(f"   Fetched {len(all_blocks)} blocks so far...")

        print(f"✅ Total blocks fetched: {len(all_blocks)}")

        # Markdown으로 변환
        print(f"🔄 Converting to Markdown...")
        markdown_content = notion_blocks_to_markdown(all_blocks)

        # 출력 파일명 결정
        if not output_file:
            # Default to lecture_notes.md in current directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            output_file = os.path.join(script_dir, 'lecture_notes.md')

        # 파일에 쓰기
        print(f"💾 Writing to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print("\n" + "="*60)
        print("✅ 다운로드 완료!")
        print("="*60)
        print(f"\n파일 저장됨: {output_file}")
        print(f"총 {len(all_blocks)} blocks 변환됨")
        print(f"파일 크기: {len(markdown_content)} characters")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    print("="*60)
    print("Notion 다운로드: Notion → Markdown")
    print("="*60)

    if len(sys.argv) < 2:
        print("\n사용법: python download_notion_to_md.py <page_id> [output_file]")
        print("\n예시:")
        print("  python download_notion_to_md.py 2a141454561d8077b956df19394fcf24")
        print("  python download_notion_to_md.py 2a141454561d8077b956df19394fcf24 my_notes.md")
        return

    page_id = sys.argv[1].strip()
    output_file = sys.argv[2].strip() if len(sys.argv) > 2 else None

    # URL에서 ID 추출
    if 'notion.so/' in page_id:
        page_id = page_id.split('notion.so/')[-1].split('?')[0]

    # 하이픈 없는 ID를 하이픈 있는 형식으로 변환
    if '-' not in page_id and len(page_id) == 32:
        page_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"

    print(f"\n📍 Page ID: {page_id}")
    if output_file:
        print(f"📄 Output: {output_file}")
    else:
        print(f"📄 Output: lecture_notes.md (default)")
    print()

    download_from_notion(page_id, output_file)


if __name__ == '__main__':
    main()
