"""Records every operation so we can `replay` later. (Half-done.)"""
from collections import deque


class History:
    def __init__(self, max_size: int = 100):
        self._ops: deque = deque(maxlen=max_size)

    def record(self, op: str, a: float, b: float, result: float) -> None:
        self._ops.append((op, a, b, result))

    def last(self) -> tuple | None:
        return self._ops[-1] if self._ops else None

    def replay(self) -> list[tuple]:
        return list(self._ops)
