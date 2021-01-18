from typing import Any, List

from alds.linear.stack.base_stack import ANY_SIZE, BaseStack
from alds.linear.stack._exceptions import StackError


class ArrayStack(BaseStack):
    def __init__(self, max_size: int = ANY_SIZE) -> None:
        super().__init__(max_size)
        self.__data: List[Any] = []

    def push(self, elem: Any) -> None:
        if self._max_size == ANY_SIZE or len(self.__data) < self._max_size:
            self.__data.append(elem)
        else:
            raise StackError('stack is full, unable to push')

    def pop(self) -> Any:
        try:
            elem: Any = self.peek()
            self.__data.pop()

            return elem
        except IndexError:
            raise StackError('stack is empty, unable to pop')

    def peek(self) -> Any:
        try:
            return self.__data[-1]
        except IndexError:
            raise StackError('stack is empty, unable to peek')

    def is_empty(self) -> bool:
        return len(self.__data) == 0

    def is_full(self) -> bool:
        return len(self.__data) == self._max_size

    def __len__(self):
        return len(self.__data)

    def __repr__(self) -> str:
        return f'ArrayStack([{", ".join([str(elem) for elem in self.__data])}])'
