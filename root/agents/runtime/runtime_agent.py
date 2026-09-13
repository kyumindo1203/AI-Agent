from typing import Any, Dict, Iterable, List, Optional

from root.agents.runtime.capability_gate import CapabilityGate
from root.agents.runtime.permission_gate import PermissionGate
from root.agents.runtime.workspace_handler import WorkspaceHandler
from root.agents.runtime.verification_handler import VerificationHandler
from root.agents.runtime.model_adapter import LocalModelAdapter


class RuntimeAgent:
    """A guarded runtime orchestration object for executing approved agent actions."""

    def __init__(
        self,
        role: str,
        capability_gate: Optional[CapabilityGate] = None,
        permission_gate: Optional[PermissionGate] = None,
        workspace_handler: Optional[WorkspaceHandler] = None,
        verification_handler: Optional[VerificationHandler] = None,
        model_adapter: Optional[LocalModelAdapter] = None,
    ):
        self.role = role
        self.capability_gate = capability_gate or CapabilityGate()
        self.permission_gate = permission_gate or PermissionGate()
        self.workspace_handler = workspace_handler or WorkspaceHandler()
        self.verification_handler = verification_handler or VerificationHandler()
        self.model_adapter = model_adapter or LocalModelAdapter()

    def execute(self, action: str, path: str, payload: Dict[str, Any], task: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a guarded action after capability and permission checks."""
        self.capability_gate.require(self.role, action)
        self.permission_gate.require(self.role, path, action)

        if action == "write_file":
            result_path = self.workspace_handler.write_file(path, payload.get("content", ""))
            evidence = {"tag": "write_file", "detail": result_path}
            self.verification_handler.add_evidence("write_file", result_path)
            return {
                "status": "executed",
                "path": result_path,
                "evidence": [evidence],
            }

        if action == "read_file":
            result = self.workspace_handler.read_file(path)
            return {
                "status": "read",
                "path": path,
                "content": result,
            }

        if action == "process_user_request":
            request = str(payload.get("request", ""))
            self.capability_gate.require(self.role, "receive_user_request")
            self.permission_gate.require(self.role, path, "process_user_request")
            response = self.model_adapter.generate(request)
            plan = [
                "clarify_intent",
                "decompose_task",
                "route_to_orchestrator",
                "verify_artifacts",
            ]
            self.verification_handler.add_evidence("model_process", response)
            return {
                "status": "processed",
                "role": self.role,
                "action": action,
                "path": path,
                "plan": plan,
                "response": response,
                "evidence": [
                    {"tag": "model_process", "detail": response}
                ],
            }

        if action == "verify":
            if task is None:
                raise ValueError("task must be supplied for verification")
            return self.verification_handler.verify(task, payload)

        return {
            "status": "accepted",
            "role": self.role,
            "action": action,
            "path": path,
        }
