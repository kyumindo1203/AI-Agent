from typing import List, Optional
from root.agents.agent import Agent


class DocumenterAgent(Agent):
    """Documenter specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "DOC-001",
        role: str = "documenter",
        name: str = "DocumenterAgent",
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
            capability=capability or ["write_docs", "update_readme", "record_changes"],
            permission=permission or ["documentation_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"task": "dict", "artifact": "dict"},
            output_schema={"documentation": "dict", "artifacts": "list[string]"},
            state_reference="project_state",
            trace_id=trace_id,
        )
