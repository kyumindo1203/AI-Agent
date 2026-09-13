"""A lightweight database abstraction without importing SQLAlchemy.

English Agent Input:
    local DB adapter with an in-memory session model and future repository hooks.

Korean note:
    추가 의존성 없이 메모리 기반 데이터 저장소를 제공하는 DB 추상화입니다.
"""

from typing import Any, Dict, List


class Database:
    """In-memory database abstraction for application-layer persistence."""

    def __init__(self):
        self.tables: Dict[str, List[Dict[str, Any]]] = {
            "requests": [],
            "artifacts": [],
            "users": [],
        }

    def insert(self, table: str, row: Dict[str, Any]) -> Dict[str, Any]:
        """Insert a row into an in-memory table."""
        if table not in self.tables:
            self.tables[table] = []
        self.tables[table].append(row)
        return row

    def select_all(self, table: str) -> List[Dict[str, Any]]:
        """Return all rows from a table."""
        return list(self.tables.get(table, []))
