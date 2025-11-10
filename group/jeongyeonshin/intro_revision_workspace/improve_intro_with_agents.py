#!/usr/bin/env python3
"""
Improve Introduction using Multi-Agent System with Gemini API
"""

import sys
import os

# Add orchestrator to path
sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')

from multi_agent_orchestrator import MultiAgentOrchestrator

# Read Introduction text
intro_path = "/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/intro_extracted.txt"
with open(intro_path, 'r') as f:
    intro_text = f.read()

print("=" * 80)
print("MULTI-AGENT INTRODUCTION IMPROVEMENT")
print("=" * 80)
print()
print(f"Input text: {len(intro_text)} characters, {len(intro_text.split())} words")
print()

# Check if API key is set
if not os.getenv("GEMINI_API_KEY"):
    print("⚠️  GEMINI_API_KEY environment variable not set!")
    print()
    print("Please set it:")
    print("  export GEMINI_API_KEY='your-api-key-here'")
    print()
    api_key = input("Or enter your Gemini API key now: ").strip()
    if api_key:
        os.environ["GEMINI_API_KEY"] = api_key
    else:
        print("❌ No API key provided. Exiting.")
        sys.exit(1)

print("🔧 Initializing Multi-Agent Orchestrator with Gemini...")
print()

try:
    orchestrator = MultiAgentOrchestrator(
        provider="gemini",
        model="gemini-2.0-flash-exp"  # Fast and powerful
    )

    print("✅ Orchestrator initialized successfully!")
    print()

    # Run gap_discovery workflow (best for Introduction)
    print("🚀 Running 'gap_discovery' workflow...")
    print()
    print("Pipeline:")
    print("  1. Literature Validator → validates gap claim")
    print("  2. Logic Auditor → checks argument structure")
    print("  3. Writer Agent → strengthens gap statement")
    print("  4. Coordinator → integrates all feedback")
    print()
    print("-" * 80)
    print()

    result = orchestrator.run_workflow(
        workflow_name="gap_discovery",
        input_text=intro_text,
        context={
            "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
            "central_claim": "Threat and deprivation have distinct effects on neurocognitive functions that can be measured with task-based fMRI",
            "research_field": "Developmental Psychology, Neuroscience",
            "target_journal": "Developmental Psychology or similar"
        }
    )

    print()
    print("=" * 80)
    print("RESULTS")
    print("=" * 80)
    print()

    # Save results
    output_dir = "/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin"

    # 1. Save full result as JSON
    import json
    with open(f"{output_dir}/intro_improvement_full_result.json", 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("📄 Full result saved to: intro_improvement_full_result.json")

    # 2. Save revised introduction
    if 'integrated_revision' in result and 'revised_text' in result['integrated_revision']:
        revised_intro = result['integrated_revision']['revised_text']
        with open(f"{output_dir}/intro_revised.txt", 'w') as f:
            f.write(revised_intro)
        print("📝 Revised introduction saved to: intro_revised.txt")
        print()
        print("=" * 80)
        print("REVISED INTRODUCTION (Preview)")
        print("=" * 80)
        print()
        # Show first 1000 characters
        preview = revised_intro[:1000] + "..." if len(revised_intro) > 1000 else revised_intro
        print(preview)

    # 3. Save executive summary
    print()
    print("=" * 80)
    print("EXECUTIVE SUMMARY")
    print("=" * 80)
    print()

    if 'executive_summary' in result:
        summary = result['executive_summary']
        print(f"Overall Assessment: {summary.get('overall_assessment', 'N/A')}")
        print()
        print("Major Strengths:")
        for strength in summary.get('major_strengths', []):
            print(f"  ✅ {strength}")
        print()
        print("Critical Issues:")
        for issue in summary.get('critical_issues', []):
            print(f"  ⚠️  {issue}")
        print()
        print(f"Revision Effort: {summary.get('estimated_revision_effort', 'N/A')}")

    # 4. Show priority actions
    print()
    print("=" * 80)
    print("PRIORITY ACTIONS")
    print("=" * 80)
    print()

    if 'integrated_feedback' in result:
        feedback = result['integrated_feedback']

        for priority, items in [
            ("CRITICAL", feedback.get('priority_1_critical', [])),
            ("HIGH", feedback.get('priority_2_high', [])),
            ("MEDIUM", feedback.get('priority_3_medium', []))
        ]:
            if items:
                print(f"[{priority}]")
                for i, item in enumerate(items, 1):
                    print(f"  {i}. {item.get('issue', 'N/A')}")
                    print(f"     Action: {item.get('action', 'N/A')}")
                    print(f"     Impact: {item.get('impact', 'N/A')}")
                    print()

    # 5. Quality improvement metrics
    if 'quality_improvement_metrics' in result:
        metrics = result['quality_improvement_metrics']
        print("=" * 80)
        print("QUALITY IMPROVEMENT")
        print("=" * 80)
        print()
        before = metrics.get('before', {})
        after = metrics.get('after', {})
        print(f"Before: {before.get('overall', 'N/A')}/10")
        print(f"After:  {after.get('overall', 'N/A')}/10")
        print(f"Improvement: {metrics.get('improvement', 'N/A')}")

    print()
    print("=" * 80)
    print("✅ DONE! Check the output files:")
    print("  - intro_revised.txt (revised introduction)")
    print("  - intro_improvement_full_result.json (detailed feedback)")
    print("=" * 80)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
