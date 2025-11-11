#!/usr/bin/env python3
"""
lecture_notes.md를 Notion 페이지에 업로드

사용법:
    python upload_lecture_notes.py <page_id>
"""

import os
import sys
import re
from typing import List, Dict, Tuple
from notion_client import Client

# Notion API 설정
NOTION_TOKEN = os.getenv('NOTION_TOKEN')


def parse_inline_markdown(text: str) -> List[Dict]:
    """
    Markdown inline formatting을 Notion rich_text로 변환
    **bold**, *italic*, `code`, ~~strikethrough~~ 지원
    """
    if not text:
        return []

    rich_text = []

    # 정규식 패턴: **bold**, *italic*, `code`, ~~strikethrough~~
    # 우선순위: code > bold > italic > strikethrough
    pattern = r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*|~~[^~]+~~)'

    parts = re.split(pattern, text)

    for part in parts:
        if not part:
            continue

        annotations = {
            'bold': False,
            'italic': False,
            'code': False,
            'strikethrough': False
        }
        content = part

        # Code (highest priority)
        if part.startswith('`') and part.endswith('`'):
            content = part[1:-1]
            annotations['code'] = True
        # Bold
        elif part.startswith('**') and part.endswith('**'):
            content = part[2:-2]
            annotations['bold'] = True
        # Italic
        elif part.startswith('*') and part.endswith('*') and not part.startswith('**'):
            content = part[1:-1]
            annotations['italic'] = True
        # Strikethrough
        elif part.startswith('~~') and part.endswith('~~'):
            content = part[2:-2]
            annotations['strikethrough'] = True

        # Notion API는 빈 텍스트를 허용하지 않음
        if content:
            # 2000자 제한
            if len(content) > 2000:
                content = content[:2000]

            rich_text.append({
                'type': 'text',
                'text': {'content': content},
                'annotations': annotations
            })

    return rich_text if rich_text else [{'type': 'text', 'text': {'content': ''}}]


def parse_markdown_to_blocks(md_content: str, max_blocks: int = 100) -> List[List[Dict]]:
    """
    Markdown을 Notion blocks로 변환 (배치로 분할)
    Notion API는 한 번에 최대 100개 블록만 허용
    """
    lines = md_content.split('\n')
    all_blocks = []
    current_block = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Heading 1 (# )
        if line.startswith('# ') and not line.startswith('## '):
            text = line[2:].strip()
            all_blocks.append({
                'type': 'heading_1',
                'heading_1': {
                    'rich_text': parse_inline_markdown(text)
                }
            })

        # Heading 2 (## )
        elif line.startswith('## ') and not line.startswith('### '):
            text = line[3:].strip()
            all_blocks.append({
                'type': 'heading_2',
                'heading_2': {
                    'rich_text': parse_inline_markdown(text)
                }
            })

        # Heading 3 (### )
        elif line.startswith('### '):
            text = line[4:].strip()
            all_blocks.append({
                'type': 'heading_3',
                'heading_3': {
                    'rich_text': parse_inline_markdown(text)
                }
            })

        # Divider (---)
        elif line.strip() in ['---', '***', '___']:
            all_blocks.append({
                'type': 'divider',
                'divider': {}
            })

        # Code block (```)
        elif line.strip().startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1

            code_content = '\n'.join(code_lines)
            if code_content.strip():
                all_blocks.append({
                    'type': 'code',
                    'code': {
                        'rich_text': [{'type': 'text', 'text': {'content': code_content[:2000]}}],
                        'language': 'plain text'
                    }
                })

        # Bulleted list (- or *)
        elif line.strip().startswith(('- ', '* ')) and not line.strip().startswith('--'):
            text = line.strip()[2:].strip()
            if text:
                all_blocks.append({
                    'type': 'bulleted_list_item',
                    'bulleted_list_item': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })

        # Numbered list
        elif re.match(r'^\d+\.\s', line.strip()):
            text = re.sub(r'^\d+\.\s', '', line.strip())
            if text:
                all_blocks.append({
                    'type': 'numbered_list_item',
                    'numbered_list_item': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })

        # Quote (>)
        elif line.strip().startswith('>'):
            text = line.strip()[1:].strip()
            if text:
                all_blocks.append({
                    'type': 'quote',
                    'quote': {
                        'rich_text': parse_inline_markdown(text)
                    }
                })

        # Regular paragraph
        elif line.strip() and not line.startswith('#'):
            # Table 감지 (간단한 방법)
            if '|' in line and (i == 0 or '|' in lines[i-1] or (i < len(lines)-1 and '|' in lines[i+1])):
                # Table을 code block으로 처리
                table_lines = [line]
                j = i + 1
                while j < len(lines) and '|' in lines[j]:
                    table_lines.append(lines[j])
                    j += 1

                table_content = '\n'.join(table_lines)
                all_blocks.append({
                    'type': 'code',
                    'code': {
                        'rich_text': [{'type': 'text', 'text': {'content': table_content[:2000]}}],
                        'language': 'markdown'
                    }
                })
                i = j - 1
            else:
                all_blocks.append({
                    'type': 'paragraph',
                    'paragraph': {
                        'rich_text': parse_inline_markdown(line.strip())
                    }
                })

        i += 1

    # 100개씩 배치로 분할
    batches = []
    for i in range(0, len(all_blocks), max_blocks):
        batches.append(all_blocks[i:i+max_blocks])

    return batches


def upload_to_notion(page_id: str, md_file: str):
    """Markdown 파일을 Notion 페이지에 업로드"""

    if not NOTION_TOKEN:
        print("❌ Error: NOTION_TOKEN 환경 변수가 설정되지 않았습니다.")
        print("   export NOTION_TOKEN='your_token_here'")
        return

    # Notion 클라이언트 초기화
    notion = Client(auth=NOTION_TOKEN)

    # Markdown 파일 읽기
    print(f"📖 Reading {md_file}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"   File size: {len(content)} characters, {len(content.splitlines())} lines")

    # Markdown을 Notion blocks로 변환
    print("🔄 Converting markdown to Notion blocks...")
    block_batches = parse_markdown_to_blocks(content)
    print(f"   Created {sum(len(batch) for batch in block_batches)} blocks in {len(block_batches)} batches")

    # Notion 페이지에 업로드
    print(f"📤 Uploading to Notion page: {page_id}...")

    try:
        # 페이지 정보 가져오기
        page = notion.pages.retrieve(page_id=page_id)
        print(f"✅ Found page: {page.get('properties', {}).get('title', {})}")

        # 각 배치를 순차적으로 업로드
        for idx, blocks in enumerate(block_batches, 1):
            print(f"   Uploading batch {idx}/{len(block_batches)} ({len(blocks)} blocks)...")
            notion.blocks.children.append(block_id=page_id, children=blocks)
            print(f"   ✅ Batch {idx} uploaded successfully")

        print("\n" + "="*60)
        print("✅ 업로드 완료!")
        print("="*60)
        print(f"\nNotion 페이지: https://notion.so/{page_id.replace('-', '')}")
        print(f"총 {sum(len(batch) for batch in block_batches)} blocks 업로드됨")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


def main():
    print("="*60)
    print("Notion 업로드: lecture_notes.md")
    print("="*60)

    if len(sys.argv) > 1:
        page_id = sys.argv[1].strip()
    else:
        page_id = input("Notion 페이지 ID: ").strip()

    # URL에서 ID 추출
    if 'notion.so/' in page_id:
        page_id = page_id.split('notion.so/')[-1].split('?')[0]

    # 하이픈 없는 ID를 하이픈 있는 형식으로 변환
    if '-' not in page_id and len(page_id) == 32:
        page_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"

    if not page_id:
        print("❌ Error: Page ID 필요")
        return

    # lecture_notes.md 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_file = os.path.join(script_dir, 'lecture_notes.md')

    if not os.path.exists(md_file):
        print(f"❌ Error: {md_file} 파일을 찾을 수 없습니다.")
        return

    print(f"\n📍 Page ID: {page_id}")
    print(f"📄 File: {md_file}\n")

    upload_to_notion(page_id, md_file)


if __name__ == '__main__':
    main()
