"""
Multi-Agent Orchestrator for Academic Writing System

This module provides the main orchestrator that coordinates all agents
and executes predefined workflows.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional, List
from agent_base import (
    WriterAgent,
    LiteratureValidatorAgent,
    QualityCheckerAgent,
    LogicAuditorAgent,
    StatisticsReviewerAgent,
    CoordinatorAgent
)


class MultiAgentOrchestrator:
    """
    Main orchestrator for the multi-agent writing system.

    Coordinates agent workflows and manages LLM clients.
    """

    def __init__(
        self,
        provider: str = "openai",
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        agents_dir: Optional[str] = None
    ):
        """
        Initialize orchestrator.

        Args:
            provider: LLM provider ("openai" or "anthropic")
            api_key: API key (if None, reads from environment)
            model: Model name (if None, uses default for provider)
            agents_dir: Directory containing agent prompt files
        """
        self.provider = provider.lower()
        self.api_key = api_key or self._get_api_key()
        self.model = model or self._get_default_model()

        # Initialize LLM client
        self.llm_client = self._init_llm_client()

        # Set agents directory
        if agents_dir is None:
            # Default: ../agents/ relative to this file
            current_dir = Path(__file__).parent
            self.agents_dir = current_dir.parent / "agents"
        else:
            self.agents_dir = Path(agents_dir)

        # Initialize all agents
        self.agents = self._init_agents()

        # Define workflows
        self.workflows = self._define_workflows()

    def _get_api_key(self) -> str:
        """Get API key from environment."""
        if self.provider == "openai":
            key = os.getenv("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY environment variable not set")
            return key
        elif self.provider == "anthropic":
            key = os.getenv("ANTHROPIC_API_KEY")
            if not key:
                raise ValueError("ANTHROPIC_API_KEY environment variable not set")
            return key
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _get_default_model(self) -> str:
        """Get default model for provider."""
        if self.provider == "openai":
            return "gpt-4"
        elif self.provider == "anthropic":
            return "claude-sonnet-4-20250514"
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _init_llm_client(self):
        """Initialize LLM client based on provider."""
        if self.provider == "openai":
            import openai
            return openai.OpenAI(api_key=self.api_key)
        elif self.provider == "anthropic":
            import anthropic
            return anthropic.Anthropic(api_key=self.api_key)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _init_agents(self) -> Dict[str, Any]:
        """Initialize all agents."""
        agents = {}

        # Writer Agent
        agents['writer'] = WriterAgent(
            name="writer",
            system_prompt_path=str(self.agents_dir / "01_writer_agent.md"),
            llm_client=self.llm_client,
            model=self.model,
            temperature=0.7
        )

        # Literature Validator Agent
        agents['literature_validator'] = LiteratureValidatorAgent(
            name="literature_validator",
            system_prompt_path=str(self.agents_dir / "02_literature_validator.md"),
            llm_client=self.llm_client,
            model=self.model,
            temperature=0.3  # Lower temperature for factual validation
        )

        # Quality Checker Agent
        agents['quality_checker'] = QualityCheckerAgent(
            name="quality_checker",
            system_prompt_path=str(self.agents_dir / "03_quality_checker.md"),
            llm_client=self.llm_client,
            model=self.model,
            temperature=0.3  # Lower temperature for systematic checking
        )

        # Logic Auditor Agent
        agents['logic_auditor'] = LogicAuditorAgent(
            name="logic_auditor",
            system_prompt_path=str(self.agents_dir / "04_logic_auditor.md"),
            llm_client=self.llm_client,
            model=self.model,
            temperature=0.3  # Lower temperature for logical analysis
        )

        # Statistics Reviewer Agent
        agents['statistics_reviewer'] = StatisticsReviewerAgent(
            name="statistics_reviewer",
            system_prompt_path=str(self.agents_dir / "05_statistics_reviewer.md"),
            llm_client=self.llm_client,
            model=self.model,
            temperature=0.2  # Lowest temperature for statistical rigor
        )

        # Coordinator Agent
        agents['coordinator'] = CoordinatorAgent(
            name="coordinator",
            system_prompt_path=str(self.agents_dir / "06_coordinator_agent.md"),
            llm_client=self.llm_client,
            model=self.model,
            temperature=0.5  # Medium temperature for integration
        )

        return agents

    def _define_workflows(self) -> Dict[str, List[tuple]]:
        """Define predefined workflows."""
        return {
            "abstract_revision": [
                ("writer", {"section": "abstract", "revision_focus": ["opening_pattern", "quantitative_results", "broad_significance"]}),
                ("quality_checker", {"section": "abstract", "evaluation_focus": ["clarity", "concision", "coherence"]}),
                ("logic_auditor", {"section": "abstract", "analysis_focus": ["ccc_structure", "logical_flow"]}),
            ],
            "gap_discovery": [
                ("literature_validator", {"section": "introduction", "validation_focus": ["gap_validity", "gap_type"]}),
                ("logic_auditor", {"section": "introduction", "analysis_focus": ["argument_structure"]}),
                ("writer", {"section": "introduction", "revision_focus": ["strengthen_gap"]}),
            ],
            "methods_bulletproofing": [
                ("writer", {"section": "methods", "revision_focus": ["reproducibility_detail"]}),
                ("statistics_reviewer", {"section": "methods", "review_focus": ["reproducibility", "controls"]}),
                ("logic_auditor", {"section": "methods", "analysis_focus": ["logical_flow"]}),
                ("quality_checker", {"section": "methods", "evaluation_focus": ["clarity"]}),
            ],
            "results_validation": [
                ("statistics_reviewer", {"section": "results", "review_focus": ["overclaiming", "multiple_comparisons", "effect_sizes"]}),
                ("logic_auditor", {"section": "results", "analysis_focus": ["argument_structure"]}),
                ("quality_checker", {"section": "results", "evaluation_focus": ["clarity"]}),
            ],
            "discussion_enhancement": [
                ("writer", {"section": "discussion", "revision_focus": ["gap_filling", "implications"]}),
                ("logic_auditor", {"section": "discussion", "analysis_focus": ["argument_structure", "ccc_structure"]}),
                ("quality_checker", {"section": "discussion", "evaluation_focus": ["clarity", "coherence"]}),
            ],
        }

    def run_workflow(
        self,
        workflow_name: str,
        input_text: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Run a predefined workflow.

        Args:
            workflow_name: Name of workflow (e.g., "abstract_revision")
            input_text: Input text to process
            context: Additional context (paper_title, target_journal, etc.)

        Returns:
            Integrated output from Coordinator agent
        """
        if workflow_name not in self.workflows:
            raise ValueError(f"Unknown workflow: {workflow_name}. Available: {list(self.workflows.keys())}")

        context = context or {}
        workflow = self.workflows[workflow_name]

        print(f"Running workflow: {workflow_name}")
        print(f"Pipeline: {' → '.join([agent_name for agent_name, _ in workflow])} → coordinator")
        print()

        # Execute agents in sequence
        agent_outputs = {}
        current_text = input_text

        for agent_name, agent_params in workflow:
            print(f"[{agent_name}] Processing...")

            agent = self.agents[agent_name]
            agent_context = {**context, **agent_params}
            output = agent.process(current_text, agent_context)

            agent_outputs[agent_name] = output

            # If Writer agent, use revised text as input for next agent
            if agent_name == "writer" and "revised_text" in output:
                current_text = output["revised_text"]

            print(f"[{agent_name}] Done.")
            print()

        # Run Coordinator to integrate feedback
        print("[coordinator] Integrating feedback...")
        coordinator = self.agents['coordinator']
        coordinator_context = {
            **context,
            "workflow_type": workflow_name
        }

        # Pass both original text and agent outputs
        integrated_output = coordinator.process(
            input_text=input_text,
            agent_outputs=agent_outputs,
            context=coordinator_context
        )

        print("[coordinator] Done.")
        print()
        print("=== WORKFLOW COMPLETE ===")

        return integrated_output

    def run_custom_workflow(
        self,
        agent_sequence: List[tuple],
        input_text: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Run a custom workflow with user-specified agent sequence.

        Args:
            agent_sequence: List of (agent_name, params) tuples
            input_text: Input text
            context: Additional context

        Returns:
            Integrated output from Coordinator
        """
        context = context or {}

        print("Running custom workflow")
        print(f"Pipeline: {' → '.join([agent_name for agent_name, _ in agent_sequence])} → coordinator")
        print()

        # Execute agents
        agent_outputs = {}
        current_text = input_text

        for agent_name, agent_params in agent_sequence:
            if agent_name not in self.agents:
                raise ValueError(f"Unknown agent: {agent_name}. Available: {list(self.agents.keys())}")

            print(f"[{agent_name}] Processing...")

            agent = self.agents[agent_name]
            agent_context = {**context, **agent_params}
            output = agent.process(current_text, agent_context)

            agent_outputs[agent_name] = output

            # If Writer agent, use revised text
            if agent_name == "writer" and "revised_text" in output:
                current_text = output["revised_text"]

            print(f"[{agent_name}] Done.")
            print()

        # Coordinator integration
        print("[coordinator] Integrating feedback...")
        coordinator = self.agents['coordinator']
        coordinator_context = {
            **context,
            "workflow_type": "custom"
        }

        integrated_output = coordinator.process(
            input_text=input_text,
            agent_outputs=agent_outputs,
            context=coordinator_context
        )

        print("[coordinator] Done.")
        print()
        print("=== WORKFLOW COMPLETE ===")

        return integrated_output

    def run_single_agent(
        self,
        agent_name: str,
        input_text: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Run a single agent without coordinator.

        Useful for testing individual agents.

        Args:
            agent_name: Name of agent to run
            input_text: Input text
            context: Additional context

        Returns:
            Agent output
        """
        if agent_name not in self.agents:
            raise ValueError(f"Unknown agent: {agent_name}. Available: {list(self.agents.keys())}")

        print(f"Running single agent: {agent_name}")
        print()

        agent = self.agents[agent_name]
        output = agent.process(input_text, context or {})

        print(f"[{agent_name}] Done.")
        return output


# Example usage
if __name__ == "__main__":
    # Example: Run abstract revision workflow

    orchestrator = MultiAgentOrchestrator(provider="openai")

    input_text = """
    The understanding of how the brain processes information during sleep has been a topic of considerable interest. Previous studies have shown that memory consolidation occurs during sleep. However, the exact mechanisms are not fully understood. In this study, we investigated the role of sleep spindles in memory consolidation using EEG recordings from 30 participants. We found that spindle density was related to memory performance. These findings suggest that sleep spindles play an important role in memory consolidation.
    """

    result = orchestrator.run_workflow(
        workflow_name="abstract_revision",
        input_text=input_text,
        context={
            "paper_title": "Sleep spindles coordinate hippocampal-cortical communication during memory consolidation",
            "central_claim": "Spindle-slow wave coupling is necessary for memory consolidation",
            "target_journal": "Nature Neuroscience"
        }
    )

    print("=== FINAL REVISED ABSTRACT ===")
    print(result['integrated_revision']['revised_text'])
    print()
    print("=== QUALITY IMPROVEMENT ===")
    print(f"Before: {result['quality_improvement_metrics']['before']['overall']}/10")
    print(f"After: {result['quality_improvement_metrics']['after']['overall']}/10")
    print(f"Improvement: {result['quality_improvement_metrics']['improvement']}")
