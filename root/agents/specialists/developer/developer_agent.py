from typing import List, Optional
from root.agents.agent import Agent


class DeveloperAgent(Agent):
    """Developer specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "DEV-001",
        role: str = "developer",
        name: str = "DeveloperAgent",
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
            capability=capability or ["read_code", "write_code", "run_tests"],
            permission=permission or ["code_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"task": "dict", "requirements": "dict"},
            output_schema={"summary": "string", "changes": "list[string]", "verification": "dict"},
            state_reference="project_state",
            trace_id=trace_id,
        )
