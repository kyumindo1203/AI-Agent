"""Service layer that coordinates the Secretary Agent and the local runtime.

English Agent Input:
    service class that validates route and creates a runtime workflow state.

Korean note:
    비서 에이전트와 로컬 런타임을 연결해 라우팅과 검증을 수행합니다.
"""

from typing import Any, Dict

from root.agents.runtime.agent_runtime import AgentRuntime
from root.agents.runtime.model_adapter import LocalModelAdapter


class SecretaryService:
    """Service object that turns a payload into an AgentRuntime execution result."""

    def __init__(self, role: str = "secretary", model_name: str = "distilgpt2"):
        self.role = role
        self.runtime = AgentRuntime(
            role=self.role,
            model_adapter=LocalModelAdapter(model_name=model_name),
        )

    def process_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Process a normalized user payload using the existing local runtime chain."""
        request_text = str(payload.get("user_request", ""))
        result = self.runtime.process(
            request=request_text,
            path="root/agents/",
            action="process_user_request",
        )
        result.update({
            "route": "secretary",
            "goal": payload.get("goal") or request_text,
            "constraints": payload.get("constraints", []),
            "priority": payload.get("priority", "normal"),
        })
        return result
