import numbers
import reprlib
from bisect import bisect, insort
from typing import Any, List, Union, Sequence, Iterable, Optional, Iterator


class OrdArray:
    def __init__(self, data: Optional[Iterable[Any]] = None) -> None:
        self.__data: List[Any] = [] if data is None else sorted(list(data))

    def find(self, value: Any) -> int:
        if len(self.__data) == 0:
            raise ValueError('trying to find value in empty array')

        i: int = bisect(self.__data, value)

        if i != len(self.__data) + 1 and self.__data[i - 1] == value:
            return i - 1
        else:
            raise ValueError('not found')

    def insert(self, value: Any) -> None:
        insort(self.__data, value)

    def delete(self, value: Any) -> None:
        try:
            i: int = self.find(value)

            del self.__data[i]
        except ValueError as err:
            raise ValueError from err

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.__data)

    def __reversed__(self) -> 'OrdArray':
        cls = type(self)

        return cls(self.__data[::-1])

    def __getitem__(self, key: Union[numbers.Integral, slice]) -> Union[Any, 'OrdArray']:
        cls = type(self)

        if isinstance(key, numbers.Integral):
            try:
                return self.__data[key]
            except IndexError as err:
                raise IndexError from err
        elif isinstance(key, slice):
            return cls(self.__data[key])
        else:
            raise TypeError(f'unsupported key type: {type(key)}, expected numbers.Integral or slice instead')

    def __delitem__(self, key: int) -> None:
        try:
            del self.__data[key]
        except IndexError as err:
            raise IndexError from err

    def __eq__(self, other) -> bool:
        return len(self.__data) == len(other) and all(a == b for a, b in zip(self.__data, other))

    def __contains__(self, item: Any) -> bool:
        try:
            self.find(item)

            return True
        except ValueError:
            return False

    def __str__(self):
        return str(self.__data)

    def __repr__(self) -> str:
        data = reprlib.repr(self.__data)

        return f'OrdArray({data[data.find("["):-1]})'
