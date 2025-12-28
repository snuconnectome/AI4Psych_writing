#!/usr/bin/env python3
"""
Improve Early Life Stress section by splitting into Threat and Deprivation
"""

import sys
import os
import re

sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')

from multi_agent_orchestrator import MultiAgentOrchestrator

# Read Methods file
with open("/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/2-methods-en.tex", 'r') as f:
    content = f.read()

# Extract ELS section (from \\subsubsection{Early life stress} to next \\subsubsection)
match = re.search(r'(\\subsubsection\{Early life stress\}.*?)(?=\\subsubsection\{|\\clearpage)', content, re.DOTALL)
if not match:
    print("❌ Could not find ELS section")
    sys.exit(1)

els_content = match.group(1)

# Split by \\textbf{Threat} and \\textbf{Deprivation}
threat_match = re.search(r'(\\textbf\{Threat\}.*?)(?=\\textbf\{Deprivation\})', els_content, re.DOTALL)
deprivation_match = re.search(r'(\\textbf\{Deprivation\}.*?)(?=For a detailed|$)', els_content, re.DOTALL)

sections = []
if threat_match:
    sections.append(("ELS - Threat", threat_match.group(1).strip()))
if deprivation_match:
    sections.append(("ELS - Deprivation", deprivation_match.group(1).strip()))

print("=" * 80)
print("EARLY LIFE STRESS SECTION IMPROVEMENT")
print("=" * 80)
print()
print(f"📑 Split into {len(sections)} parts:")
for title, c in sections:
    print(f"   • {title} ({len(c.split())} words)")
print()

# Setup
if os.getenv("GEMINI_API_KEY"):
    provider, model = "gemini", "gemini-2.0-flash"
    print("✅ Using Gemini API")
elif os.getenv("GROQ_API_KEY"):
    provider, model = "groq", "llama-3.3-70b-versatile"
    print("✅ Using Groq API")
else:
    print("❌ No API key"); sys.exit(1)

orchestrator = MultiAgentOrchestrator(provider=provider, model=model)
print("✅ Orchestrator ready!")

context = {
    "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
    "research_field": "Developmental Psychology",
    "parent_section": "Measurement - Early Life Stress"
}

all_results = {}
all_revised = []

for i, (title, text) in enumerate(sections):
    print()
    print(f"📝 Processing {i+1}/{len(sections)}: {title}")
    print("-" * 40)

    try:
        result = orchestrator.run_workflow(
            workflow_name="methods_bulletproofing",
            input_text=text,
            context={**context, "current_section": title}
        )
        all_results[title] = result

        if 'integrated_revision' in result and 'revised_text' in result['integrated_revision']:
            all_revised.append((title, result['integrated_revision']['revised_text']))
            print(f"✅ Done!")
        else:
            all_revised.append((title, text))
    except Exception as e:
        print(f"⚠️  Error: {e}")
        all_revised.append((title, text))

# Save
import json
with open("/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/els_improvement_result.json", 'w') as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)

with open("/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/els_revised.txt", 'w') as f:
    f.write("\n\n".join([c for _, c in all_revised]))

print()
print("=" * 80)
print("SUMMARIES")
print("=" * 80)

for title, result in all_results.items():
    print(f"\n📌 {title}")
    if 'executive_summary' in result:
        s = result['executive_summary']
        print(f"   {s.get('overall_assessment', 'N/A')[:150]}...")
        for issue in s.get('critical_issues', [])[:2]:
            print(f"   ⚠️  {issue}")

print()
print("✅ Saved: els_revised.txt, els_improvement_result.json")
