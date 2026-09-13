from typing import List, Optional
from root.agents.agent import Agent


class ReviewerAgent(Agent):
    """Reviewer specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "REV-001",
        role: str = "reviewer",
        name: str = "ReviewerAgent",
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
            capability=capability or ["review_solution", "review_requirements", "review_quality"],
            permission=permission or ["review_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"task": "dict", "result": "dict"},
            output_schema={"verdict": "string", "criteria": "list[dict]", "issues": "list[string]"},
            state_reference="project_state",
            trace_id=trace_id,
        )
