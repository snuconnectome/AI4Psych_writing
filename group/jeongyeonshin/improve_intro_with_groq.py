#!/usr/bin/env python3
"""
Improve LaTeX Introduction with Groq (Free & Fast!)
Uses Groq's fast, free API to improve introduction
"""

import sys
import os
import json
import re
sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')

# Read the LaTeX file
latex_file = '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/1-intro-en.tex'
with open(latex_file, 'r') as f:
    full_content = f.read()

print("="*80)
print("IMPROVING LATEX INTRODUCTION WITH GROQ (FREE & FAST!)")
print("="*80)
print(f"📄 Input file: {latex_file}")
print()

# Extract main text (text only, no tables)
# Tables are too large for single API call
intro_start = full_content.find(r'\section{Introduction}')
first_table = full_content.find(r'\begin{landscape}')
main_text = full_content[intro_start:first_table].strip()

print(f"📝 Main text: {len(main_text.split())} words (tables will be extracted separately)")
print()

# Check if GROQ_API_KEY is set
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    print("❌ GROQ_API_KEY not set!")
    print()
    print("📝 To get a free Groq API key:")
    print("   1. Visit https://console.groq.com/keys")
    print("   2. Sign up (free, no credit card needed)")
    print("   3. Create an API key")
    print("   4. Run: export GROQ_API_KEY='your-key-here'")
    print()
    sys.exit(1)

# Initialize orchestrator with Groq
from multi_agent_orchestrator import MultiAgentOrchestrator

print("🚀 Initializing Groq orchestrator...")
orchestrator = MultiAgentOrchestrator(provider="groq")
print(f"✅ Using model: {orchestrator.model}")
print()

results = {}

# ========================================
# STEP 1: Process Full Intro (no tables)
# ========================================
print("="*80)
print("STEP 1: IMPROVING INTRODUCTION TEXT")
print("="*80)
print("🔄 Processing with gap_discovery workflow...")
print("   (Literature Validator → Logic Auditor → Writer → Coordinator)")
print()

results['intro'] = orchestrator.run_workflow(
    workflow_name="gap_discovery",
    input_text=main_text,
    context={
        "section": "introduction",
        "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
        "target_journal": "Developmental Psychology"
    }
)

if results['intro'] and 'error' not in results['intro']:
    print("✅ Introduction completed!")

    # Save immediately
    with open('intro_improved_result.json', 'w') as f:
        json.dump(results['intro'], f, indent=2, ensure_ascii=False)

    # Extract revised text
    if 'integrated_revision' in results['intro']:
        revised_text = results['intro']['integrated_revision'].get('revised_text', '')
        with open('intro_revised.txt', 'w') as f:
            f.write(revised_text)
        print(f"💾 Saved: intro_revised.txt ({len(revised_text.split())} words)")
else:
    print("❌ Introduction failed")

# ========================================
# Extract and save tables
# ========================================
print("\n" + "="*80)
print("STEP 2: EXTRACTING TABLES")
print("="*80)

table_pattern = r'(\\begin\{landscape\}.*?\\end\{landscape\})'
tables = re.findall(table_pattern, full_content, re.DOTALL)

print(f"📊 Found {len(tables)} tables")

tables_content = "\n\n".join([f"TABLE {i+1}:\n{table}\n" for i, table in enumerate(tables)])
with open('intro_tables_extracted.txt', 'w') as f:
    f.write(tables_content)

print(f"💾 Saved: intro_tables_extracted.txt")

# ========================================
# Summary
# ========================================
print("\n" + "="*80)
print("DONE!")
print("="*80)

if 'intro' in results and 'error' not in results['intro']:
    print("\n✅ Successfully improved introduction!")
    print("\n📄 Output files:")
    print("   - intro_revised.txt (revised text)")
    print("   - intro_improved_result.json (detailed feedback)")
    print("   - intro_tables_extracted.txt (original tables)")

    if 'executive_summary' in results['intro']:
        summary = results['intro']['executive_summary']
        print(f"\n📋 Overall Assessment:")
        print(f"   {summary.get('overall_assessment', 'N/A')}")

        critical = summary.get('critical_issues', [])
        if critical:
            print(f"\n⚠️  Critical Issues ({len(critical)}):")
            for issue in critical[:3]:
                print(f"   • {issue}")
else:
    print("\n❌ Failed to improve introduction")
