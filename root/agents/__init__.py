"""Agent abstraction package.

This package intentionally contains only object-level abstractions for the
current approved work scope.
"""

from .agent import Agent
from .secretary.secretary_agent import SecretaryAgent
from .orchestrator.orchestrator_agent import OrchestratorAgent

__all__ = ["Agent", "SecretaryAgent", "OrchestratorAgent"]
