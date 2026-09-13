from pathlib import Path
from typing import Optional


class WorkspaceHandler:
    """Workspace boundary for read/write operations under a checked scope."""

    def __init__(self, workspace_root: str = "/workspaces/AI-Agent"):
        self.workspace_root = Path(workspace_root)

    def resolve(self, relative_path: str) -> Path:
        target = (self.workspace_root / relative_path).resolve()
        root = self.workspace_root.resolve()
        if root not in target.parents and target != root:
            raise PermissionError(f"Workspace path escapes the repository root: {relative_path}")
        return target

    def read_file(self, relative_path: str) -> str:
        path = self.resolve(relative_path)
        if not path.exists():
            raise FileNotFoundError(relative_path)
        return path.read_text(encoding="utf-8")

    def write_file(self, relative_path: str, content: str) -> str:
        path = self.resolve(relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return str(path)

    def append_file(self, relative_path: str, content: str) -> str:
        path = self.resolve(relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(content)
        return str(path)

    def delete_file(self, relative_path: str) -> bool:
        path = self.resolve(relative_path)
        if path.exists() and path.is_file():
            path.unlink()
            return True
        return False
