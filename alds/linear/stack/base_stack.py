from abc import ABC, abstractmethod
from typing import Any

ANY_SIZE: int = -1


class BaseStack(ABC):
    def __init__(self, max_size: int = ANY_SIZE):
        self.__max_size: int = max_size

    @abstractmethod
    def push(self, elem) -> None:
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass
