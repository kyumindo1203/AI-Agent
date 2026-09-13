from typing import List, Optional
from root.agents.agent import Agent


class ResearcherAgent(Agent):
    """Researcher specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "RES-001",
        role: str = "researcher",
        name: str = "ResearcherAgent",
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
            capability=capability or ["read_docs", "compare_sources", "collect_evidence"],
            permission=permission or ["research_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"question": "string", "project_state": "dict"},
            output_schema={"findings": "list[dict]", "evidence": "list[dict]"},
            state_reference="project_state",
            trace_id=trace_id,
        )
