from typing import Any, Dict, List, Optional

from root.agents.agent import Agent


class SecretaryAgent(Agent):
    """Secretary Agent as the single user-facing interface."""

    def __init__(
        self,
        agent_id: str = "SEC-001",
        role: str = "secretary",
        name: str = "SecretaryAgent",
        capability: Optional[List[str]] = None,
        permission: Optional[List[str]] = None,
        allowed_channels: Optional[List[str]] = None,
        blocked_channels: Optional[List[str]] = None,
        state_reference: Optional[str] = "project_state",
        trace_id: Optional[str] = None,
    ):
        super().__init__(
            agent_id=agent_id,
            role=role,
            name=name,
            capability=capability or [
                "receive_user_request",
                "clarify_intent",
                "route_request_to_orchestrator",
                "report_result_to_user",
                "manage_approval_request",
            ],
            permission=permission or [
                "user_interface",
                "orchestrator_channel",
                "approval_channel",
                "user_report_channel",
            ],
            allowed_channels=allowed_channels or ["user", "orchestrator"],
            blocked_channels=blocked_channels or ["specialist", "developer", "tester"],
            input_schema={
                "user_request": "string",
                "goal": "string",
                "constraints": "list[string]",
                "priority": "low|normal|high|urgent",
            },
            output_schema={
                "message_type": "REQUEST|REPORT|APPROVAL_REQUEST|STATUS",
                "receiver": "orchestrator|user",
                "payload": "dict",
            },
            state_reference=state_reference,
            trace_id=trace_id,
        )

    def receive_user_request(self, user_request: str, constraints: Optional[List[str]] = None,
                             goal: Optional[str] = None, priority: str = "normal") -> Dict[str, Any]:
        """Receive a user request and normalize it into the Secretary contract."""
        input_payload = {
            "user_request": user_request,
            "goal": goal or user_request,
            "constraints": constraints or [],
            "priority": priority,
        }
        return self.receive(input_payload)

    def forward_to_orchestrator(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send a normalized request from the user to the Orchestrator."""
        return self.send_message("orchestrator", "REQUEST", request)

    def report_to_user(self, report: Dict[str, Any]) -> Dict[str, Any]:
        """Return a final user-facing report framed by the Secretary contract."""
        return self.send_message("user", "REPORT", report)

    def request_approval(self, action: str, reason: str, risk: str,
                         affected_resources: Optional[List[str]] = None,
                         recommendation: Optional[str] = None) -> Dict[str, Any]:
        """Create an approval request for actions that need user decision-making."""
        payload = {
            "action": action,
            "reason": reason,
            "risk": risk,
            "affected_resources": affected_resources or [],
            "recommendation": recommendation or "pending_user_decision",
            "expected_consequence": "user approval required",
            "rollback_available": False,
        }
        return self.send_message("user", "APPROVAL_REQUEST", payload)
