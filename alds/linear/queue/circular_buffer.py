from typing import Any, List

from alds.linear.queue.base_queue import BaseQueue
from alds.linear.queue._exceptions import QueueError


class CircularBuffer(BaseQueue):
    def __init__(self, max_size: int):
        super().__init__(max_size + 1)
        self.__data: List[Any] = [None] * max_size
        self.__front: int = 0
        self.__rear: int = -1

    def push(self, elem) -> None:
        if self.is_full():
            raise QueueError('circular buffer is full, unable to push')

        if self.__rear == self._max_size - 1:
            self.__rear = -1

        self.__rear += 1
        self.__data[self.__rear] = elem

    def pop(self) -> Any:
        if self.is_empty():
            raise QueueError('circular buffer is empty, unable to pop')

        tmp: Any = self.__data[self.__front]
        self.__front += 1

        if self.__front == self._max_size:
            self.__front = 0

        return tmp

    def peek(self) -> Any:
        if self.is_empty():
            raise QueueError('circular buffer is empty, unable to peek')

        return self.__data[self.__front]

    def is_empty(self) -> bool:
        return self.__rear + 1 == self.__front or self.__front + self._max_size - 1 == self.__rear

    def is_full(self) -> bool:
        return self.__rear + 2 == self.__front or self.__front + self._max_size - 2 == self.__rear
