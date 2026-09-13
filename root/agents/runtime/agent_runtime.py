from typing import Any, Dict, Optional

from root.agents.runtime.capability_gate import CapabilityGate
from root.agents.runtime.permission_gate import PermissionGate
from root.agents.runtime.workspace_handler import WorkspaceHandler
from root.agents.runtime.verification_handler import VerificationHandler
from root.agents.runtime.model_adapter import LocalModelAdapter
from root.agents.runtime.message_bus import MessageBus
from root.agents.runtime.task_scheduler import TaskScheduler
from root.agents.runtime.workflow_state import WorkflowState


class AgentRuntime:
    """Complete runtime skeleton that couples the gates, model adapter, queue, scheduler, and workflow state."""

    def __init__(
        self,
        role: str = "orchestrator",
        capability_gate: Optional[CapabilityGate] = None,
        permission_gate: Optional[PermissionGate] = None,
        workspace_handler: Optional[WorkspaceHandler] = None,
        verification_handler: Optional[VerificationHandler] = None,
        model_adapter: Optional[LocalModelAdapter] = None,
        message_bus: Optional[MessageBus] = None,
        task_scheduler: Optional[TaskScheduler] = None,
        workflow_state: Optional[WorkflowState] = None,
    ):
        self.role = role
        self.capability_gate = capability_gate or CapabilityGate()
        self.permission_gate = permission_gate or PermissionGate()
        self.workspace_handler = workspace_handler or WorkspaceHandler()
        self.verification_handler = verification_handler or VerificationHandler()
        self.model_adapter = model_adapter or LocalModelAdapter()
        self.message_bus = message_bus or MessageBus()
        self.task_scheduler = task_scheduler or TaskScheduler(max_workers=2)
        self.workflow_state = workflow_state or WorkflowState(workflow_id="wf-local")

    def process(self, request: str, path: str = "root/agents/", action: str = "process_user_request") -> Dict[str, Any]:
        """A complete request processing path with gates, model answer, workflow state, and asynchronous-friendly dispatch hooks."""
        self.capability_gate.require(self.role, "receive_user_request")
        self.permission_gate.require(self.role, path, action)

        prompt = f"User request: {request}"
        response = self.model_adapter.generate(prompt)

        self.workflow_state.status = "running"
        self.workflow_state.add_message({"topic": "request", "payload": request})
        self.workflow_state.add_message({"topic": "response", "payload": response})

        self.message_bus.publish("runtime.process", {
            "role": self.role,
            "request": request,
            "response": response,
            "trace_id": self.workflow_state.workflow_id,
        })

        self.verification_handler.add_evidence("model_process", response)

        return {
            "status": "processed",
            "workflow_id": self.workflow_state.workflow_id,
            "role": self.role,
            "action": action,
            "path": path,
            "plan": [
                "clarify_intent",
                "decompose_task",
                "route_to_orchestrator",
                "verify_artifacts",
                "report_result",
            ],
            "response": response,
            "evidence": [{"tag": "model_process", "detail": response}],
        }
