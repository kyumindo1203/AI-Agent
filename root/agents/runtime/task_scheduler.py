from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Dict, Iterable, List, Optional


class TaskScheduler:
    """A lightweight threadpool scheduler for independent agent task units."""

    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit(self, fn: Callable[..., Any], *args: Any, **kwargs: Any):
        return self.executor.submit(fn, *args, **kwargs)

    def map(self, tasks: Iterable[Callable[..., Any]]) -> List[Any]:
        futures = [self.executor.submit(fn) for fn in tasks]
        return [future.result() for future in as_completed(futures)]

    def shutdown(self):
        self.executor.shutdown(wait=True)
