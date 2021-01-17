from bisect import bisect, insort
from typing import Any, List, Union, Sequence


class OrdArray:
    def __init__(self) -> None:
        self.__data: List[Any] = []

    def find(self, value) -> int:
        if len(self.__data) == 0:
            raise ValueError('trying to find value in empty array')

        i: int = bisect(self.__data, value)

        if i != len(self.__data) + 1 and self.__data[i - 1] == value:
            return i - 1
        else:
            raise ValueError('not found')

    def insert(self, value) -> None:
        insort(self.__data, value)

    def delete(self, value) -> None:
        try:
            i = self.find(value)

            del self.__data[i]
        except ValueError as err:
            raise ValueError from err

    def __len__(self) -> int:
        return len(self.__data)

    def __getitem__(self, key: int) -> Union[Any, Sequence[Any]]:
        if not isinstance(key, int):
            raise TypeError(f'unsupported key type: {type(key)}, expected int instead')

        try:
            return self.__data[key]
        except IndexError as err:
            raise IndexError from err

    def __setitem__(self, key: int, value: Any) -> None:
        if not isinstance(key, int):
            raise TypeError(f'unsupported key type: {type(key)}, expected int instead')

        try:
            self.__data[key] = value
        except IndexError as err:
            raise IndexError from err

    def __contains__(self, item: Any) -> bool:
        try:
            self.find(item)

            return True
        except ValueError:
            return False

    def __repr__(self) -> str:
        return f'OrdArray([{", ".join([str(elem) for elem in self.__data])}])'
