from collections import defaultdict, deque
from threading import Thread
from typing import Any, Callable, Deque, Dict, List, Optional, Set
import time


class MessageBus:
    """A minimal in-process asynchronous message bus for agent events."""

    def __init__(self):
        self.queues: Dict[str, Deque[Dict[str, Any]]] = defaultdict(deque)
        self.subscribers: Dict[str, Set[str]] = defaultdict(set)
        self.handlers: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {}

    def subscribe(self, topic: str, agent_id: str):
        self.subscribers[topic].add(agent_id)

    def register_handler(self, topic: str, handler: Callable[[Dict[str, Any]], Dict[str, Any]]):
        self.handlers[topic] = handler

    def publish(self, topic: str, message: Dict[str, Any]) -> None:
        self.queues[topic].append(message)

    def drain(self, topic: str) -> List[Dict[str, Any]]:
        messages = list(self.queues[topic])
        self.queues[topic].clear()
        return messages

    def dispatch(self, topic: str) -> List[Dict[str, Any]]:
        results = []
        for message in list(self.queues[topic]):
            handler = self.handlers.get(topic)
            if handler:
                result = handler(message)
                results.append(result)
        self.queues[topic].clear()
        return results

    def start_async(self, topic: str, handler: Callable[[Dict[str, Any]], Dict[str, Any]]) -> Thread:
        self.register_handler(topic, handler)

        def worker():
            while True:
                if not self.queues[topic]:
                    time.sleep(0.01)
                    continue
                self.dispatch(topic)

        thread = Thread(target=worker, daemon=True)
        thread.start()
        return thread
