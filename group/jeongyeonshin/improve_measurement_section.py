#!/usr/bin/env python3
"""
Improve Measurement Section (the longest section) by splitting into subsubsections
"""

import sys
import os
import re

sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')

from multi_agent_orchestrator import MultiAgentOrchestrator

# Read Methods LaTeX file
methods_path = "/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/2-methods-en.tex"
with open(methods_path, 'r') as f:
    full_content = f.read()

# Extract Measurement section
match = re.search(r'(\\subsection\{Measurement\}.*?)(?=\\subsection\{|\\end\{document\})', full_content, re.DOTALL)
if not match:
    print("❌ Could not find Measurement section")
    sys.exit(1)

measurement_content = match.group(1)

# Split by subsubsection
def split_by_subsubsection(text):
    pattern = r'(\\subsubsection\{[^}]+\})'
    parts = re.split(pattern, text)

    sections = []
    current_section = ""
    current_title = "Measurement Intro"

    for part in parts:
        if part.startswith('\\subsubsection{'):
            if current_section.strip():
                sections.append((current_title, current_section.strip()))
            match = re.search(r'\\subsubsection\{([^}]+)\}', part)
            current_title = match.group(1) if match else "Unknown"
            current_section = part
        else:
            current_section += part

    if current_section.strip():
        sections.append((current_title, current_section.strip()))

    return sections

sections = split_by_subsubsection(measurement_content)

print("=" * 80)
print("MEASUREMENT SECTION IMPROVEMENT")
print("=" * 80)
print()
print(f"📑 Found {len(sections)} subsubsections:")
for title, content in sections:
    word_count = len(content.split())
    print(f"   • {title} ({word_count} words)")
print()

# Setup API
provider = None
model = None

if os.getenv("GEMINI_API_KEY"):
    provider = "gemini"
    model = "gemini-2.0-flash"
    print("✅ Using Gemini API")
elif os.getenv("GROQ_API_KEY"):
    provider = "groq"
    model = "llama-3.3-70b-versatile"
    print("✅ Using Groq API")
else:
    print("❌ No API key found")
    sys.exit(1)

print()
print("🔧 Initializing Multi-Agent Orchestrator...")

try:
    orchestrator = MultiAgentOrchestrator(provider=provider, model=model)
    print("✅ Orchestrator initialized!")
    print()

    context = {
        "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
        "research_field": "Developmental Psychology, Neuroscience",
        "target_journal": "Developmental Psychology",
        "parent_section": "Measurement"
    }

    all_results = {}
    all_revised = []

    for i, (title, content) in enumerate(sections):
        if len(content.split()) < 30:
            print(f"⏭️  Skipping '{title}' (too short)")
            all_revised.append((title, content))
            continue

        print()
        print("=" * 80)
        print(f"📝 Processing {i+1}/{len(sections)}: {title}")
        print("=" * 80)
        print()

        try:
            result = orchestrator.run_workflow(
                workflow_name="methods_bulletproofing",
                input_text=content,
                context={**context, "current_section": title}
            )

            all_results[title] = result

            if 'integrated_revision' in result and 'revised_text' in result['integrated_revision']:
                revised = result['integrated_revision']['revised_text']
                all_revised.append((title, revised))
                print(f"✅ '{title}' processed!")
            else:
                all_revised.append((title, content))
                print(f"⚠️  No revision for '{title}'")

        except Exception as e:
            print(f"⚠️  Error: {e}")
            all_revised.append((title, content))

    # Save results
    output_dir = "/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin"

    import json
    with open(f"{output_dir}/measurement_improvement_result.json", 'w') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)

    combined = "\n\n".join([content for _, content in all_revised])
    with open(f"{output_dir}/measurement_revised.txt", 'w') as f:
        f.write(combined)

    print()
    print("=" * 80)
    print("SECTION SUMMARIES")
    print("=" * 80)

    for title, result in all_results.items():
        print()
        print(f"📌 {title}")
        print("-" * 40)
        if 'executive_summary' in result:
            summary = result['executive_summary']
            print(f"   Assessment: {summary.get('overall_assessment', 'N/A')[:100]}...")

            issues = summary.get('critical_issues', [])
            if issues:
                print("   Issues:")
                for issue in issues[:2]:
                    print(f"     ⚠️  {issue}")

    print()
    print("=" * 80)
    print("✅ DONE!")
    print("  - measurement_revised.txt")
    print("  - measurement_improvement_result.json")
    print("=" * 80)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
