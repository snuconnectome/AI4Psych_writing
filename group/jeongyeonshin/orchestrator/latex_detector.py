"""
LaTeX Detection Utility

Detects whether input text is LaTeX or plain text.
"""

import re
from typing import Tuple


def is_latex(text: str, threshold: int = 3) -> Tuple[bool, str]:
    """
    Detect if text is written in LaTeX.

    Args:
        text: Input text to check
        threshold: Minimum number of LaTeX indicators to consider it LaTeX

    Returns:
        Tuple of (is_latex: bool, reason: str)
    """
    indicators = []

    # Check for LaTeX commands
    latex_commands = [
        r'\\section',
        r'\\subsection',
        r'\\subsubsection',
        r'\\begin{',
        r'\\end{',
        r'\\textbf{',
        r'\\textit{',
        r'\\emph{',
        r'\\cite',
        r'\\ref{',
        r'\\label{',
        r'\\item',
        r'\\usepackage',
        r'\\documentclass',
        r'\\title{',
        r'\\author{',
        r'\\maketitle'
    ]

    command_count = 0
    for cmd in latex_commands:
        if re.search(cmd, text):
            command_count += 1
            indicators.append(f"Found command: {cmd}")

    # Check for math environments
    math_patterns = [
        r'\$.*?\$',  # Inline math
        r'\\\[.*?\\\]',  # Display math
        r'\\begin{equation}',
        r'\\begin{align}',
        r'\\begin{gather}'
    ]

    math_count = 0
    for pattern in math_patterns:
        if re.search(pattern, text, re.DOTALL):
            math_count += 1
            indicators.append(f"Found math: {pattern}")

    # Check for citation patterns
    citation_patterns = [
        r'\\cite\{',
        r'\\citep\{',
        r'\\citet\{',
        r'\\citealt\{'
    ]

    citation_count = 0
    for pattern in citation_patterns:
        if re.search(pattern, text):
            citation_count += 1
            indicators.append(f"Found citation: {pattern}")

    # Check for environment blocks
    env_pattern = r'\\begin\{(\w+)\}.*?\\end\{\1\}'
    env_matches = re.findall(env_pattern, text, re.DOTALL)
    if env_matches:
        indicators.append(f"Found environments: {', '.join(set(env_matches))}")

    # Calculate total LaTeX indicators
    total_indicators = command_count + math_count + citation_count + len(env_matches)

    # Decision
    is_latex_text = total_indicators >= threshold

    if is_latex_text:
        reason = f"Detected {total_indicators} LaTeX indicators (threshold: {threshold}): " + \
                 "; ".join(indicators[:5])  # Show first 5 indicators
    else:
        reason = f"Only {total_indicators} LaTeX indicators found (threshold: {threshold}). " + \
                 "Treating as plain text."

    return is_latex_text, reason


def auto_convert_if_latex(text: str, converter_agent=None) -> Tuple[str, dict]:
    """
    Automatically detect and convert LaTeX if needed.

    Args:
        text: Input text
        converter_agent: LaTeXConverterAgent instance (optional)

    Returns:
        Tuple of (processed_text: str, metadata: dict)
    """
    is_latex_text, reason = is_latex(text)

    metadata = {
        "is_latex": is_latex_text,
        "detection_reason": reason,
        "converted": False
    }

    if not is_latex_text:
        # Plain text, return as-is
        return text, metadata

    if converter_agent is None:
        # No converter provided, return LaTeX as-is with warning
        metadata["warning"] = "LaTeX detected but no converter provided"
        return text, metadata

    # Convert LaTeX to plain text
    try:
        result = converter_agent.process(text)
        plain_text = result.get('plain_text', text)
        metadata["converted"] = True
        metadata["conversion_warnings"] = result.get('warnings', [])
        metadata["structure"] = result.get('structure', {})
        return plain_text, metadata
    except Exception as e:
        # Conversion failed, return original
        metadata["warning"] = f"Conversion failed: {str(e)}"
        return text, metadata


# Quick test
if __name__ == "__main__":
    # Test cases
    latex_sample = r"""
    \section{Introduction}
    ELS has been investigated \citep{carr2013}.
    The \textbf{DMAP} model posits that $\beta = -0.45$.
    """

    plain_sample = """
    Introduction

    ELS has been investigated (Carr et al., 2013).
    The DMAP model posits that β = -0.45.
    """

    print("Testing LaTeX detection:")
    print("-" * 60)

    is_ltx, reason = is_latex(latex_sample)
    print(f"LaTeX sample: {is_ltx}")
    print(f"  Reason: {reason}\n")

    is_ltx, reason = is_latex(plain_sample)
    print(f"Plain sample: {is_ltx}")
    print(f"  Reason: {reason}\n")
