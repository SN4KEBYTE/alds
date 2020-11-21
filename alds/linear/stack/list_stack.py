from typing import Any, Optional

from alds.linear.stack.base_stack import ANY_SIZE, BaseStack


# todo: implement all methods
class LinkedListStack(BaseStack):
    def __init__(self, max_size: int = ANY_SIZE):
        super().__init__(max_size)
        self.__size: int = 0
        self.__data: Any = None
        self.__next: Optional[LinkedListStack] = None

    def push(self, elem) -> None:
        pass

    def pop(self) -> Any:
        pass

    def peek(self) -> Any:
        pass

    def is_empty(self) -> bool:
        pass
