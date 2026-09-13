from typing import List, Optional
from root.agents.agent import Agent


class OrchestratorAgent(Agent):
    """Orchestrator agent skeleton for project orchestration and delegation."""

    def __init__(
        self,
        agent_id: str = "ORC-001",
        role: str = "orchestrator",
        name: str = "OrchestratorAgent",
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
            capability=capability or [
                "analyze_goal",
                "decompose_task",
                "assign_task",
                "collect_result",
                "verify_result",
                "plan_retry",
            ],
            permission=permission or [
                "workflow_control",
                "project_state_access",
                "task_assignment",
                "verification_request",
            ],
            allowed_channels=allowed_channels or ["secretary", "planner", "researcher", "developer", "tester", "reviewer", "security", "documenter"],
            blocked_channels=blocked_channels or ["user"],
            input_schema={
                "goal": "string",
                "project_state": "dict",
                "constraints": "list[string]",
            },
            output_schema={
                "task": "dict",
                "verification_request": "dict",
                "report": "dict",
            },
            state_reference="project_state",
            trace_id=trace_id,
        )
