def insertion_sort(iterable):
    for i in range(1, len(iterable)):
        tmp = iterable[i]
        j = i

        while j > 0 and iterable[j - 1] > tmp:
            iterable[j] = iterable[j - 1]
            j -= 1

        iterable[j] = tmp
