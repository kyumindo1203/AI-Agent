"""Repository layer for persisting request and artifact metadata in memory.

English Agent Input:
    repository interface that stores workflow evidence and request metadata.

Korean note:
    요청 메타데이터와 검증 근거를 메모리 기반으로 저장하는 저장소 계층입니다.
"""

from typing import Any, Dict, List


class RequestRepository:
    """Minimal in-memory repository that mirrors the workflow and artifact storage footprint."""

    def __init__(self):
        self.requests: List[Dict[str, Any]] = []
        self.artifacts: List[Dict[str, Any]] = []

    def add_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Persist a normalized incoming request payload."""
        self.requests.append(payload)
        return payload

    def add_artifact(self, artifact: Dict[str, Any]) -> Dict[str, Any]:
        """Persist an artifact or evidence record created after routing."""
        self.artifacts.append(artifact)
        return artifact

    def list_requests(self) -> List[Dict[str, Any]]:
        """Return all stored user requests."""
        return list(self.requests)

    def list_artifacts(self) -> List[Dict[str, Any]]:
        """Return all stored artifacts and evidence records."""
        return list(self.artifacts)
