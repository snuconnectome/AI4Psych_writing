#!/usr/bin/env python3
"""
Improve Part 2: Literature Review
"""

import sys
import os
sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')
from multi_agent_orchestrator import MultiAgentOrchestrator

# Read Part 2
with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part2_literature.txt', 'r') as f:
    part2_text = f.read()

print("="*80)
print("IMPROVING PART 2: LITERATURE REVIEW")
print("="*80)
print(f"Input: {len(part2_text.split())} words")
print()

# Initialize orchestrator
orchestrator = MultiAgentOrchestrator(provider="gemini")

# Custom workflow for literature review: Literature + Quality + Logic
result = orchestrator.run_custom_workflow(
    agent_sequence=[
        ("literature_validator", {"validation_focus": ["citation_accuracy", "completeness"]}),
        ("quality_checker", {"evaluation_focus": ["clarity", "coherence"]}),
        ("logic_auditor", {"analysis_focus": ["logical_flow", "ccc_structure"]}),
    ],
    input_text=part2_text,
    context={
        "section": "literature_review",
        "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
        "research_field": "Developmental Psychology"
    }
)

# Save result
import json
with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part2_result.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

if 'integrated_revision' in result and 'revised_text' in result['integrated_revision']:
    revised = result['integrated_revision']['revised_text']
    with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part2_revised.txt', 'w') as f:
        f.write(revised)
    print("✅ Part 2 revised and saved!")
else:
    print("⚠️ No revised text found, using original")
    with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part2_revised.txt', 'w') as f:
        f.write(part2_text)

print("Done!")
