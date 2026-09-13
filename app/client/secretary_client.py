"""Client-side request facade for the Secretary Agent.

English Agent Input:
    secretariat request entrypoint that normalizes user payloads into the
    agent runtime request contract.

Korean note:
    사용자 입력을 자연어로 받는 클라이언트 진입점입니다. 내부적으로는
    비서 에이전트의 표준 입력 형식으로 정규화합니다.
"""

from typing import Any, Dict, Optional


class SecretaryClient:
    """Thin client object that accepts a natural language request and normalizes it."""

    def __init__(self, controller=None):
        self.controller = controller

    def submit_request(self, request: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Submit a user request to the controller/service chain."""
        payload = {
            "user_request": request,
            "goal": context.get("goal") if context else None,
            "constraints": context.get("constraints", []) if context else [],
            "priority": context.get("priority", "normal") if context else "normal",
        }
        if self.controller is None:
            return {
                "status": "accepted",
                "route": "secretary",
                "payload": payload,
            }
        return self.controller.handle_request(payload)
