def bubble_sort(iterable):
    for i in range(len(iterable) - 1):
        for j in range(i + 1, len(iterable)):
            if iterable[i] > iterable[j]:
                iterable[i], iterable[j] = iterable[j], iterable[i]
