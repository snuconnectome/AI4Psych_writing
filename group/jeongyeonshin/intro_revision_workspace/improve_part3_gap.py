#!/usr/bin/env python3
"""
Improve Part 3: Research Gap and Objectives
"""

import sys
import os
sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')
from multi_agent_orchestrator import MultiAgentOrchestrator

# Read Part 3
with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part3_gap.txt', 'r') as f:
    part3_text = f.read()

print("="*80)
print("IMPROVING PART 3: RESEARCH GAP & OBJECTIVES")
print("="*80)
print(f"Input: {len(part3_text.split())} words")
print()

# Initialize orchestrator
orchestrator = MultiAgentOrchestrator(provider="gemini")

# Use gap_discovery workflow (perfect for this section!)
result = orchestrator.run_workflow(
    workflow_name="gap_discovery",
    input_text=part3_text,
    context={
        "section": "introduction",
        "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
        "central_claim": "Threat and deprivation have distinct neural effects measurable with task-fMRI",
        "research_field": "Developmental Psychology",
        "target_journal": "Developmental Psychology"
    }
)

# Save result
import json
with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part3_result.json', 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

if 'integrated_revision' in result and 'revised_text' in result['integrated_revision']:
    revised = result['integrated_revision']['revised_text']
    with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part3_revised.txt', 'w') as f:
        f.write(revised)
    print("✅ Part 3 revised and saved!")
else:
    print("⚠️  No revised text found, using original")
    with open('/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_part3_revised.txt', 'w') as f:
        f.write(part3_text)

print("Done!")
