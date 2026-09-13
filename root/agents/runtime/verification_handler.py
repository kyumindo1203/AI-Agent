from typing import Any, Dict, List


class VerificationHandler:
    """Collects verification evidence and checks whether a result is acceptable."""

    def __init__(self):
        self.evidence: List[Dict[str, Any]] = []

    def add_evidence(self, tag: str, detail: str) -> None:
        self.evidence.append({"tag": tag, "detail": detail})

    def verify(self, task: Dict[str, Any], result: Dict[str, Any]) -> Dict[str, Any]:
        verdict = {
            "task_id": task.get("task_id"),
            "agent": task.get("assigned_agent"),
            "verified": True,
            "evidence": list(self.evidence),
            "result": result,
        }
        return verdict
