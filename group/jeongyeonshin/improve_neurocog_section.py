#!/usr/bin/env python3
"""
Improve Neurocognitive functions section by splitting into 4 domains
"""

import sys
import os
import re

sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')

from multi_agent_orchestrator import MultiAgentOrchestrator

# Read Methods file
with open("/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/2-methods-en.tex", 'r') as f:
    content = f.read()

# Extract Neurocognitive functions section
match = re.search(r'(\\subsubsection\{Neurocognitive functions\}.*?)(?=\\subsubsection\{Covariates\})', content, re.DOTALL)
if not match:
    print("❌ Could not find Neurocognitive functions section")
    sys.exit(1)

neurocog_content = match.group(1)

# Split by \\textbf{domain}
domains = ["Reward processing", "Emotion processing", "Working memory", "Impulsivity"]
sections = []

for i, domain in enumerate(domains):
    # Find this domain section
    if i < len(domains) - 1:
        next_domain = domains[i + 1]
        pattern = rf'(\\textbf\{{{domain}\}}.*?)(?=\\textbf\{{{next_domain}\}})'
    else:
        pattern = rf'(\\textbf\{{{domain}\}}.*?)(?=\\subsubsection|$)'

    match = re.search(pattern, neurocog_content, re.DOTALL)
    if match:
        sections.append((domain, match.group(1).strip()))

print("=" * 80)
print("NEUROCOGNITIVE FUNCTIONS IMPROVEMENT")
print("=" * 80)
print()
print(f"📑 Split into {len(sections)} domains:")
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
    "research_field": "Developmental Psychology, Cognitive Neuroscience",
    "parent_section": "Measurement - Neurocognitive Functions"
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
            print(f"⚠️  No revision, keeping original")
    except Exception as e:
        print(f"⚠️  Error: {e}")
        all_revised.append((title, text))

# Save
import json
with open("/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/neurocog_improvement_result.json", 'w') as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False, default=str)

with open("/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/neurocog_revised.txt", 'w') as f:
    f.write("\n\n".join([c for _, c in all_revised]))

print()
print("=" * 80)
print("SUMMARIES")
print("=" * 80)

for title, result in all_results.items():
    print(f"\n📌 {title}")
    if 'executive_summary' in result:
        s = result['executive_summary']
        assessment = s.get('overall_assessment', 'N/A')
        if isinstance(assessment, str):
            print(f"   {assessment[:150]}...")
        for issue in s.get('critical_issues', [])[:2]:
            print(f"   ⚠️  {issue}")

print()
print("✅ Saved: neurocog_revised.txt, neurocog_improvement_result.json")
