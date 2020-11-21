from typing import Any, List

from alds.linear.stack.base_stack import ANY_SIZE, BaseStack
from alds.linear.stack._exceptions import StackError


class ArrayStack(BaseStack):
    def __init__(self, max_size: int = ANY_SIZE) -> None:
        super().__init__(max_size)
        self.__data: List[Any] = []

    def push(self, elem: Any) -> None:
        if self.__max_size == ANY_SIZE:
            self.__data.append(elem)
        else:
            raise StackError('stack is full, unable to push')

    def pop(self) -> Any:
        try:
            elem: Any = self.peek()
            self.__data.pop(-1)

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
