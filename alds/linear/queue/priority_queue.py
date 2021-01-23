from typing import Any, List, Tuple, Optional

from alds.linear.queue._exceptions import QueueError
from alds.linear.queue.base_queue import ANY_SIZE, BaseQueue


class PriorityQueue(BaseQueue):
    def __init__(self, max_size: int = ANY_SIZE) -> None:
        super().__init__(max_size)
        self.__data: List[Any] = []

    def push(self, elem: Tuple[Any, Any]) -> None:
        if self.is_empty():
            self.__data.append(elem)
        else:
            i: int = len(self) - 1

            while i >= 0:
                if elem[0] > self.__data[i][0]:
                    self.__data[i + 1] = self.__data[i]
                else:
                    break

                i -= 1

            self.__data[i + 1] = elem

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            raise QueueError('priority queue is empty, unable to pop')

        elem: Any = self.__data[-1]
        self.__data.pop()

        return elem

    def peek(self) -> Optional[Any]:
        if self.is_empty():
            raise QueueError('priority queue is empty, unable to peek')

        return self.__data[-1]

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        return len(self) == self._max_size and self._max_size != ANY_SIZE

    def __len__(self) -> int:
        return len(self.__data)
