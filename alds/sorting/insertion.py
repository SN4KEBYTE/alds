from collections.abc import MutableSequence
from typing import Any


def insertion_sort(iterable: MutableSequence) -> None:
    for i in range(1, len(iterable)):
        tmp: Any = iterable[i]
        j: int = i

        while j > 0 and iterable[j - 1] > tmp:
            iterable[j] = iterable[j - 1]
            j -= 1

        iterable[j] = tmp
