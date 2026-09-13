from typing import List, Optional
from root.agents.agent import Agent


class SecurityAgent(Agent):
    """Security specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "SEC-002",
        role: str = "security",
        name: str = "SecurityAgent",
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
            capability=capability or ["review_security", "check_secrets", "check_permissions"],
            permission=permission or ["security_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"task": "dict", "artifact": "dict"},
            output_schema={"risks": "list[dict]", "secrets": "list[string]", "verdict": "string"},
            state_reference="project_state",
            trace_id=trace_id,
        )
