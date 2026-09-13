from typing import List, Optional
from root.agents.agent import Agent


class PlannerAgent(Agent):
    """Planner specialist skeleton."""

    def __init__(
        self,
        agent_id: str = "PLN-001",
        role: str = "planner",
        name: str = "PlannerAgent",
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
            capability=capability or ["analyze_requirements", "decompose_tasks", "plan_sequence"],
            permission=permission or ["planning_scope"],
            allowed_channels=allowed_channels or ["orchestrator"],
            blocked_channels=blocked_channels or ["user", "secretary"],
            input_schema={"requirements": "string", "constraints": "list[string]"},
            output_schema={"plan": "dict", "tasks": "list[dict]"},
            state_reference="project_state",
            trace_id=trace_id,
        )
