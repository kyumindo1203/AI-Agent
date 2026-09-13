from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class WorkflowState:
    """A small state object to represent task, artifact, and message lifecycle state."""

    workflow_id: str
    status: str = "created"
    tasks: List[Dict[str, Any]] = field(default_factory=list)
    artifacts: List[str] = field(default_factory=list)
    messages: List[Dict[str, Any]] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def add_task(self, task: Dict[str, Any]) -> None:
        self.tasks.append(task)

    def add_artifact(self, artifact: str) -> None:
        self.artifacts.append(artifact)

    def add_message(self, message: Dict[str, Any]) -> None:
        self.messages.append(message)

    def mark_done(self) -> None:
        self.status = "done"

    def mark_failed(self, error: str) -> None:
        self.status = "failed"
        self.errors.append(error)
