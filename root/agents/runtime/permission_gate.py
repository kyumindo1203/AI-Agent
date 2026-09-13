from pathlib import Path
from typing import Iterable, Sequence


class PermissionGate:
    """Enforces repository-scoped authorizations for agent actions."""

    def __init__(self, allowed_prefixes: Sequence[str] | None = None):
        self.allowed_prefixes = list(allowed_prefixes or [
            "root/agents/",
            "root/protocol/",
            "root/state/",
            "root/workflow/",
            "root/logs/",
            "root/artifacts/",
        ])

    def _normalize_path(self, path: str) -> str:
        # Convert repository-relative path into a consistent prefix-safe form.
        parsed = Path(path).as_posix().strip()
        if parsed.startswith("/"):
            parsed = parsed.lstrip("/")
        if parsed.endswith("/"):
            parsed = parsed.rstrip("/")
        return parsed

    def allow(self, role: str, path: str, action: str) -> bool:
        normalized = self._normalize_path(path)

        # very conservative policy: only allow writing inside known project directories
        if action == "process_user_request":
            return any(normalized.startswith(prefix.rstrip("/")) for prefix in self.allowed_prefixes)

        if role == "developer" and action in {"write_file", "modify_file"}:
            return any(normalized.startswith(prefix.rstrip("/")) for prefix in self.allowed_prefixes)

        if role == "documenter" and action == "write_doc":
            return any(normalized.startswith(prefix.rstrip("/")) for prefix in self.allowed_prefixes)

        if role == "security" and action == "review_security":
            return any(normalized.startswith(prefix.rstrip("/")) for prefix in self.allowed_prefixes)

        if role == "tester" and action == "run_tests":
            return any(normalized.startswith(prefix.rstrip("/")) for prefix in self.allowed_prefixes)

        return any(normalized.startswith(prefix.rstrip("/")) for prefix in self.allowed_prefixes)

    def require(self, role: str, path: str, action: str) -> None:
        if not self.allow(role, path, action):
            raise PermissionError(f"Role '{role}' is not permitted to '{action}' on '{path}'.")
