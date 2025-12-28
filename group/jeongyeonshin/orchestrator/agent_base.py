"""
Base Agent Class for Multi-Agent Writing System

This module provides the base class that all specialized agents inherit from.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from abc import ABC, abstractmethod


class AgentBase(ABC):
    """
    Base class for all agents in the multi-agent writing system.

    Each agent must implement the process() method.
    """

    def __init__(
        self,
        name: str,
        system_prompt_path: str,
        llm_client: Any,
        model: str = "gpt-4",
        temperature: float = 0.7
    ):
        """
        Initialize an agent.

        Args:
            name: Agent name (e.g., "writer", "quality_checker")
            system_prompt_path: Path to markdown file with system prompt
            llm_client: LLM client (OpenAI or Anthropic)
            model: Model to use (gpt-4, claude-sonnet-4, etc.)
            temperature: Sampling temperature (0-1)
        """
        self.name = name
        self.system_prompt = self.load_prompt(system_prompt_path)
        self.llm_client = llm_client
        self.model = model
        self.temperature = temperature

    def load_prompt(self, prompt_path: str) -> str:
        """
        Load system prompt from markdown file.

        Args:
            prompt_path: Path to markdown file

        Returns:
            System prompt as string
        """
        path = Path(prompt_path)
        if not path.exists():
            raise FileNotFoundError(f"System prompt not found: {prompt_path}")

        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    @abstractmethod
    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process input text and return agent-specific output.

        This method must be implemented by each specialized agent.

        Args:
            input_text: Text to process
            context: Additional context (section type, focus areas, etc.)

        Returns:
            Agent output as dictionary
        """
        pass

    def call_llm(self, user_prompt: str) -> str:
        """
        Call LLM with system prompt + user prompt.

        Args:
            user_prompt: User/input prompt

        Returns:
            LLM response as string
        """
        # Detect which LLM client is being used
        client_type = type(self.llm_client).__name__

        if hasattr(self.llm_client, 'chat') and hasattr(self.llm_client.chat, 'completions'):
            # OpenAI or Groq client (both use same API)
            response = self.llm_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=self.temperature
            )
            return response.choices[0].message.content

        elif hasattr(self.llm_client, 'messages'):
            # Anthropic client
            response = self.llm_client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=self.temperature,
                system=self.system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            return response.content[0].text

        elif hasattr(self.llm_client, 'generate_content'):
            # Google Gemini client
            full_prompt = f"{self.system_prompt}\n\n---\n\n{user_prompt}"
            response = self.llm_client.generate_content(
                full_prompt,
                generation_config={
                    "temperature": self.temperature,
                    "max_output_tokens": 8192,
                }
            )
            return response.text

        else:
            raise ValueError(f"Unknown LLM client type: {type(self.llm_client)}")

    def parse_json_output(self, llm_output: str) -> Dict[str, Any]:
        """
        Parse JSON output from LLM response.

        Handles markdown code blocks if present.

        Args:
            llm_output: Raw LLM output

        Returns:
            Parsed JSON as dictionary
        """
        # Remove markdown code blocks if present
        if "```json" in llm_output:
            llm_output = llm_output.split("```json")[1].split("```")[0].strip()
        elif "```" in llm_output:
            llm_output = llm_output.split("```")[1].split("```")[0].strip()

        try:
            return json.loads(llm_output)
        except json.JSONDecodeError as e:
            # Try to fix common JSON issues (control characters in strings)
            try:
                # Replace literal newlines in JSON strings with escaped newlines
                import re
                fixed_output = re.sub(r'(?<!\\)"([^"]*)\n', r'"\1\\n', llm_output)
                fixed_output = re.sub(r'\n([^"]*)"', r'\\n\1"', fixed_output)
                return json.loads(fixed_output)
            except:
                raise ValueError(f"Failed to parse JSON from LLM output: {e}\n\nOutput: {llm_output[:500]}...")


class WriterAgent(AgentBase):
    """
    Writer Agent: Generates and revises text.
    """

    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process input text and generate revision.

        Args:
            input_text: Text to revise
            context: Section type, revision focus, etc.

        Returns:
            Revision output with revised_text, changes, rationale
        """
        context = context or {}

        user_prompt = f"""
Section: {context.get('section', 'unknown')}
Revision Focus: {context.get('revision_focus', [])}

Input Text:
{input_text}

Context:
- Paper Title: {context.get('paper_title', 'N/A')}
- Central Claim: {context.get('central_claim', 'N/A')}
- Target Journal: {context.get('target_journal', 'N/A')}

Please provide your output in JSON format as specified in your system prompt.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)


class LiteratureValidatorAgent(AgentBase):
    """
    Literature Validator Agent: Validates citations and gaps.
    """

    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process input text and validate literature/gaps.

        Args:
            input_text: Text to validate
            context: Validation focus, etc.

        Returns:
            Validation output with gap analysis, citation checks
        """
        context = context or {}

        user_prompt = f"""
Section: {context.get('section', 'introduction')}
Validation Focus: {context.get('validation_focus', ['gap_validity', 'citation_accuracy'])}

Input Text:
{input_text}

Context:
- Paper Title: {context.get('paper_title', 'N/A')}
- Research Field: {context.get('research_field', 'N/A')}

Please provide your output in JSON format as specified in your system prompt.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)


class QualityCheckerAgent(AgentBase):
    """
    Quality Checker Agent: Evaluates writing quality.
    """

    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process input text and evaluate quality.

        Args:
            input_text: Text to check
            context: Evaluation focus, etc.

        Returns:
            Quality evaluation with issues, scores, suggestions
        """
        context = context or {}

        user_prompt = f"""
Section: {context.get('section', 'any')}
Evaluation Focus: {context.get('evaluation_focus', ['clarity', 'concision', 'coherence', 'style'])}

Input Text:
{input_text}

Please provide your output in JSON format as specified in your system prompt.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)


class LogicAuditorAgent(AgentBase):
    """
    Logic Auditor Agent: Analyzes logical structure and argument flow.
    """

    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process input text and analyze logic.

        Args:
            input_text: Text to analyze
            context: Analysis focus, etc.

        Returns:
            Logic analysis with CCC structure, flow, fallacies
        """
        context = context or {}

        user_prompt = f"""
Section: {context.get('section', 'any')}
Analysis Focus: {context.get('analysis_focus', ['logical_flow', 'argument_structure', 'fallacies'])}

Input Text:
{input_text}

Context:
- Central Claim: {context.get('central_claim', 'N/A')}

Please provide your output in JSON format as specified in your system prompt.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)


class StatisticsReviewerAgent(AgentBase):
    """
    Statistics Reviewer Agent: Validates statistical rigor and reproducibility.
    """

    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process input text and validate statistics.

        Args:
            input_text: Text to review
            context: Review focus, study design, etc.

        Returns:
            Statistical review with reproducibility, controls, rigor checks
        """
        context = context or {}

        user_prompt = f"""
Section: {context.get('section', 'methods')}
Review Focus: {context.get('review_focus', ['reproducibility', 'controls', 'statistical_rigor'])}

Input Text:
{input_text}

Context:
- Study Design: {context.get('study_design', 'experimental')}
- Sample Size: {context.get('sample_size', 'N/A')}
- Main Analysis: {context.get('main_analysis', 'N/A')}

Please provide your output in JSON format as specified in your system prompt.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)


class CoordinatorAgent(AgentBase):
    """
    Coordinator Agent: Orchestrates workflow and integrates feedback.
    """

    def process(
        self,
        input_text: str,
        agent_outputs: Dict[str, Dict[str, Any]],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process input text and integrate feedback from all agents.

        Args:
            input_text: Original text
            agent_outputs: Outputs from all other agents
            context: Workflow type, section, etc.

        Returns:
            Integrated output with prioritized feedback, revisions, conflicts resolved
        """
        context = context or {}

        user_prompt = f"""
Workflow Type: {context.get('workflow_type', 'custom')}
Section: {context.get('section', 'unknown')}

Original Input Text:
{input_text}

Agent Outputs:
{json.dumps(agent_outputs, indent=2)}

Context:
- Paper Title: {context.get('paper_title', 'N/A')}
- Target Journal: {context.get('target_journal', 'N/A')}
- Author Focus: {context.get('author_focus', [])}

Please provide your integrated output in JSON format as specified in your system prompt.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)



class LaTeXConverterAgent(AgentBase):
    """
    LaTeX Converter Agent: Converts LaTeX to plain text.
    """

    def process(self, input_text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process LaTeX text and convert to plain text.

        Args:
            input_text: LaTeX text to convert
            context: Optional context (unused for now)

        Returns:
            Plain text version with structure info and warnings
        """
        context = context or {}

        user_prompt = f"""
Input LaTeX Text:
{input_text}

Please convert this LaTeX to clean plain text following the specifications in your system prompt.
Return your output in JSON format with: plain_text, structure, and warnings.
"""

        llm_output = self.call_llm(user_prompt)
        return self.parse_json_output(llm_output)

