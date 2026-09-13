from typing import Iterable, Mapping, Sequence


class CapabilityGate:
    """Enforces technical capability checks for an agent role before execution."""

    CAPABILITIES = {
        "secretary": {
            "receive_user_request",
            "clarify_intent",
            "route_request_to_orchestrator",
            "report_result_to_user",
            "manage_approval_request",
            "process_user_request",
        },
        "orchestrator": {
            "analyze_goal",
            "decompose_task",
            "assign_task",
            "collect_result",
            "verify_result",
            "plan_retry",
        },
        "planner": {
            "analyze_requirements",
            "decompose_tasks",
            "plan_sequence",
        },
        "researcher": {
            "read_docs",
            "compare_sources",
            "collect_evidence",
        },
        "developer": {
            "read_code",
            "write_code",
            "run_tests",
        },
        "tester": {
            "run_tests",
            "reproduce_failure",
            "check_acceptance_criteria",
        },
        "reviewer": {
            "review_solution",
            "review_requirements",
            "review_quality",
        },
        "security": {
            "review_security",
            "check_secrets",
            "check_permissions",
        },
        "documenter": {
            "write_docs",
            "update_readme",
            "record_changes",
        },
    }

    def __init__(self, capability_map: Mapping[str, Iterable[str]] | None = None):
        self.capability_map = dict(self.CAPABILITIES)
        if capability_map:
            self.capability_map.update(capability_map)

    def can(self, role: str, action: str) -> bool:
        return action in self.capability_map.get(role, set())

    def require(self, role: str, action: str) -> None:
        if not self.can(role, action):
            raise PermissionError(f"Role '{role}' lacks capability '{action}'.")
