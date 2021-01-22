from collections.abc import MutableSequence


def odd_even_sort(iterable: MutableSequence) -> None:
    n: int = len(iterable)

    while True:
        is_sorted: bool = True

        for i in range(0, n - 1, 2):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]

                is_sorted = False

        for i in range(1, n - 1, 2):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]

                is_sorted = False

        if is_sorted:
            break

