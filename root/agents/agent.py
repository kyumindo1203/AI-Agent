from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional


@dataclass
class Agent:
    """Abstract base class for all agents in the multi-agent organization."""

    agent_id: str
    role: str
    name: str
    capability: List[str] = field(default_factory=list)
    permission: List[str] = field(default_factory=list)
    allowed_channels: List[str] = field(default_factory=list)
    blocked_channels: List[str] = field(default_factory=list)
    input_schema: Dict[str, Any] = field(default_factory=dict)
    output_schema: Dict[str, Any] = field(default_factory=dict)
    state_reference: Optional[str] = None
    trace_id: Optional[str] = None

    def receive(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize a received payload according to the shared object contract."""
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "name": self.name,
            "input": payload,
            "input_schema": self.input_schema,
            "permission": self.permission,
            "trace_id": self.trace_id,
        }

    def respond(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Emit a structured output object for the assigned task or report."""
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "name": self.name,
            "output": payload,
            "output_schema": self.output_schema,
            "trace_id": self.trace_id,
        }

    def send_message(self, receiver: str, message_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Create a message envelope for agent-to-agent communication."""
        if receiver not in self.allowed_channels:
            raise ValueError(f"Receiver '{receiver}' is not an allowed channel for agent '{self.name}'.")

        return {
            "sender": self.role,
            "receiver": receiver,
            "message_type": message_type,
            "payload": payload,
            "trace_id": self.trace_id,
        }

    def can_send_to(self, receiver: str) -> bool:
        return receiver in self.allowed_channels and receiver not in self.blocked_channels
