"""Simple application-entry facade for the layered Secretary Agent runtime.

English Agent Input:
    a very small FastAPI-like wiring example that composes the client,
    controller, service, repository, and database adapter without
    external AI service imports.

Korean note:
    비서 에이전트가 입력을 받는 요청 흐름을 클라이언트-컨트롤러-서비스-
    저장소-DB 어댑터 순으로 최소 형태로 연결합니다.
"""

from app.client.secretary_client import SecretaryClient
from app.controllers.secretary_controller import SecretaryController
from app.services.secretary_service import SecretaryService
from app.repositories.request_repository import RequestRepository
from app.db.database import Database


class AppFactory:
    """Concise composition root that wires all repository-scoped layers together."""

    def __init__(self):
        self.database = Database()
        self.repository = RequestRepository()
        self.service = SecretaryService()
        self.controller = SecretaryController(self.service)
        self.client = SecretaryClient(self.controller)

    def handle_request(self, request: str, context: dict | None = None):
        """Entry point used by the smoke test or sample UI wiring."""
        result = self.client.submit_request(request, context or {})
        self.repository.add_request({
            "user_request": request,
            "result": result,
            "context": context or {},
        })
        return result


app = AppFactory()


if __name__ == "__main__":
    print(app.handle_request("Create a Python CLI project", {"priority": "normal"}))
