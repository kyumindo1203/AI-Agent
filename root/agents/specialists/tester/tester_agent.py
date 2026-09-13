from typing import List, Optional
from root.agents.agent import Agent


class TesterAgent(Agent):
    """Tester specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "TST-001",
        role: str = "tester",
        name: str = "TesterAgent",
        capability: Optional[List[str]] = None,
        permission: Optional[List[str]] = None,
        allowed_channels: Optional[List[str]] = None,
        blocked_channels: Optional[List[str]] = None,
        trace_id: Optional[str] = None,
    ):
        super().__init__(
            agent_id=agent_id,
            role=role,
            name=name,
            capability=capability or ["run_tests", "reproduce_failure", "check_acceptance_criteria"],
            permission=permission or ["test_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"task": "dict", "artifact": "dict"},
            output_schema={"tests": "list[dict]", "verdict": "string", "evidence": "list[dict]"},
            state_reference="project_state",
            trace_id=trace_id,
        )
