def selection_sort(iterable):
    for i in range(len(iterable) - 1):
        min_ind: int = i

        for j in range(i + 1, len(iterable)):
            if iterable[j] < iterable[min_ind]:
                min_ind = j

        if min_ind != i:
            iterable[i], iterable[min_ind] = iterable[min_ind], iterable[i]
