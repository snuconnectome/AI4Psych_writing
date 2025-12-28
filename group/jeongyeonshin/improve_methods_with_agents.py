#!/usr/bin/env python3
"""
Improve Methods Section using Multi-Agent System

This script processes Methods in sections to avoid token limits.
Uses the methods_bulletproofing workflow:
  Writer → Statistics Reviewer → Logic Auditor → Quality Checker → Coordinator
"""

import sys
import os
import re

# Add orchestrator to path
sys.path.insert(0, '/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/orchestrator')

from multi_agent_orchestrator import MultiAgentOrchestrator

def split_methods_by_subsection(latex_text):
    """Split Methods into subsections for processing."""
    # Find all subsections
    pattern = r'(\\subsection\{[^}]+\})'
    parts = re.split(pattern, latex_text)

    sections = []
    current_section = ""
    current_title = "Preamble"

    for i, part in enumerate(parts):
        if part.startswith('\\subsection{'):
            # Save previous section if exists
            if current_section.strip():
                sections.append((current_title, current_section.strip()))
            # Start new section
            match = re.search(r'\\subsection\{([^}]+)\}', part)
            current_title = match.group(1) if match else f"Section {len(sections)+1}"
            current_section = part
        else:
            current_section += part

    # Don't forget the last section
    if current_section.strip():
        sections.append((current_title, current_section.strip()))

    return sections

# Read Methods LaTeX file
methods_path = "/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin/2-methods-en.tex"
with open(methods_path, 'r') as f:
    methods_text = f.read()

print("=" * 80)
print("MULTI-AGENT METHODS IMPROVEMENT")
print("=" * 80)
print()
print(f"Input file: {methods_path}")
print(f"Input size: {len(methods_text)} characters, {len(methods_text.split())} words")
print()

# Split into sections
sections = split_methods_by_subsection(methods_text)
print(f"📑 Found {len(sections)} subsections:")
for title, content in sections:
    word_count = len(content.split())
    print(f"   • {title} ({word_count} words)")
print()

# Check if API key is set (try multiple providers - Gemini first)
provider = None
model = None

if os.getenv("GEMINI_API_KEY"):
    provider = "gemini"
    model = "gemini-2.0-flash"  # Stable and fast
    print("✅ Using Gemini API (gemini-2.0-flash)")
elif os.getenv("GROQ_API_KEY"):
    provider = "groq"
    model = "llama-3.3-70b-versatile"
    print("✅ Using Groq API (free & fast)")
elif os.getenv("ANTHROPIC_API_KEY"):
    provider = "anthropic"
    model = "claude-sonnet-4-20250514"
    print("✅ Using Anthropic API")
elif os.getenv("OPENAI_API_KEY"):
    provider = "openai"
    model = "gpt-4"
    print("✅ Using OpenAI API")
else:
    print("⚠️  No API key found!")
    print()
    print("Please set one of the following environment variables:")
    print("  export GEMINI_API_KEY='your-key'")
    print("  export ANTHROPIC_API_KEY='your-key'")
    print("  export OPENAI_API_KEY='your-key'")
    print("  export GROQ_API_KEY='your-key'")
    print()
    api_key = input("Or enter your Groq API key now: ").strip()
    if api_key:
        os.environ["GROQ_API_KEY"] = api_key
        provider = "groq"
        model = "llama-3.3-70b-versatile"
    else:
        print("❌ No API key provided. Exiting.")
        sys.exit(1)

print()
print("🔧 Initializing Multi-Agent Orchestrator...")
print()

try:
    orchestrator = MultiAgentOrchestrator(
        provider=provider,
        model=model
    )

    print("✅ Orchestrator initialized successfully!")
    print()

    # Process each section separately
    all_results = {}
    all_revised_sections = []

    context = {
        "paper_title": "Distinct impacts of threat and deprivation on neurocognitive functions",
        "central_claim": "Threat and deprivation have distinct effects on neurocognitive functions measured through task-based fMRI",
        "research_field": "Developmental Psychology, Neuroscience",
        "target_journal": "Developmental Psychology or similar APA journal",
        "dataset": "ABCD Study (Adolescent Brain Cognitive Development)",
        "analysis_methods": "GLM, LASSO regression, fMRI task-based analysis"
    }

    for i, (title, content) in enumerate(sections):
        # Skip preamble (LaTeX setup)
        if title == "Preamble" or len(content.split()) < 50:
            print(f"⏭️  Skipping '{title}' (too short or preamble)")
            all_revised_sections.append((title, content))
            continue

        print()
        print("=" * 80)
        print(f"📝 Processing Section {i+1}/{len(sections)}: {title}")
        print("=" * 80)
        print()

        try:
            result = orchestrator.run_workflow(
                workflow_name="methods_bulletproofing",
                input_text=content,
                context={**context, "current_section": title}
            )

            all_results[title] = result

            # Get revised text
            if 'integrated_revision' in result and 'revised_text' in result['integrated_revision']:
                revised = result['integrated_revision']['revised_text']
                all_revised_sections.append((title, revised))
                print(f"✅ Section '{title}' processed successfully!")
            else:
                all_revised_sections.append((title, content))
                print(f"⚠️  No revision generated for '{title}', keeping original")

        except Exception as e:
            print(f"⚠️  Error processing '{title}': {e}")
            print("   Keeping original content for this section")
            all_revised_sections.append((title, content))
            continue

    print()
    print("=" * 80)
    print("SAVING RESULTS")
    print("=" * 80)
    print()

    # Save results
    output_dir = "/Users/jeongyeon/AI4Psych_writing/group/jeongyeonshin"

    # 1. Save full result as JSON
    import json
    with open(f"{output_dir}/methods_improvement_full_result.json", 'w') as f:
        # Convert to serializable format
        serializable_results = {}
        for title, result in all_results.items():
            serializable_results[title] = result
        json.dump(serializable_results, f, indent=2, ensure_ascii=False, default=str)
    print("📄 Full result saved to: methods_improvement_full_result.json")

    # 2. Save combined revised methods
    combined_revised = "\n\n".join([content for title, content in all_revised_sections])
    with open(f"{output_dir}/methods_revised.txt", 'w') as f:
        f.write(combined_revised)
    print("📝 Revised methods saved to: methods_revised.txt")

    # 3. Print summary for each processed section
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
            print(f"   Assessment: {summary.get('overall_assessment', 'N/A')}")

            strengths = summary.get('major_strengths', [])
            if strengths:
                print("   Strengths:")
                for s in strengths[:2]:  # Show top 2
                    print(f"     ✅ {s}")

            issues = summary.get('critical_issues', [])
            if issues:
                print("   Issues:")
                for issue in issues[:2]:  # Show top 2
                    print(f"     ⚠️  {issue}")

    print()
    print("=" * 80)
    print("✅ DONE! Check the output files:")
    print("  - methods_revised.txt (revised methods section)")
    print("  - methods_improvement_full_result.json (detailed feedback)")
    print("=" * 80)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
