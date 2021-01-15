from unittest import TestCase

from alds.sorting.bubble import bubble_sort


class TestBubbleSort(TestCase):
    def test_empty_list(self):
        arr = []
        bubble_sort(arr)

        self.assertEqual(arr, [])

    def test_one_element_list(self):
        arr = [0]
        bubble_sort(arr)

        self.assertEqual(arr, [0])

    def test_all_elements_same(self):
        arr = [1, 1, 1, 1, 1]
        bubble_sort(arr)

        self.assertEqual(arr, [1, 1, 1, 1, 1])

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)

        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        bubble_sort(arr)

        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_all_elements_unique(self):
        arr = [-1, -2, 1, 0, 2]
        bubble_sort(arr)

        self.assertEqual(arr, [-2, -1, 0, 1, 2])

    def test_repeated_elements(self):
        arr = [2, -1, -1, 1, 0]
        bubble_sort(arr)

        self.assertEqual(arr, [-1, -1, 0, 1, 2])
