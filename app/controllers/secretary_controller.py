"""Controller layer for user request handling through the Secretary Agent route.

English Agent Input:
    thin HTTP/controller class that receives normalized payloads and forwards
    them to the service layer.

Korean note:
    비서 에이전트 경로로 요청을 전달하는 얇은 컨트롤러 계층입니다.
"""

from typing import Any, Dict


class SecretaryController:
    """Controller that translates API/client requests into service calls."""

    def __init__(self, service):
        self.service = service

    def handle_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Receive a normalized request payload and delegate to the service."""
        return self.service.process_request(payload)
