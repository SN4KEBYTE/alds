from unittest import TestCase

from alds.linear.array.ord_array import OrdArray


class TestOrdArray(TestCase):
    def setUp(self) -> None:
        self.arr = OrdArray()

    def test_insert_to_empty(self):
        self.arr.insert(1)

        self.assertEqual(self.arr[0], 1)

    def test_insert_into_beginning(self):
        for i in range(1, 5):
            self.arr.insert(i)

        self.arr.insert(1)

        self.assertEqual(self.arr[0], 1)

    def test_insert_to_end(self):
        for i in range(4):
            self.arr.insert(i)

        self.arr.insert(4)

        self.assertEqual(self.arr[-1], 4)

    def test_insert_into_middle(self):
        self.arr.insert(1)
        self.arr.insert(3)

        self.arr.insert(2)

        self.assertEqual(self.arr[1], 2)

    def test_find_in_empty(self):
        self.assertRaises(ValueError, self.arr.find, 1)

    def test_find_existing_all_elements_unique(self):
        for i in range(5):
            self.arr.insert(i)

        pos = self.arr.find(4)

        self.assertEqual(pos, 4)

    def test_find_existing_repeated_elements(self):
        for i in range(5):
            self.arr.insert(i)
            self.arr.insert(i)

        pos = self.arr.find(2)

        self.assertEqual(pos, 5)

    def test_find_non_existing(self):
        for i in range(5):
            self.arr.insert(i)

        self.assertRaises(ValueError, self.arr.find, 5)

    def test_delete_from_empty(self):
        self.assertRaises(ValueError, self.arr.delete, 0)

    def test_delete_existing_all_elements_unique(self):
        for i in range(5):
            self.arr.insert(i)

        self.arr.delete(0)

        self.assertRaises(ValueError, self.arr.find, 0)

    def test_delete_existing_repeated_elements(self):
        for i in range(5):
            self.arr.insert(i)
            self.arr.insert(i)

        self.arr.delete(0)

        self.assertEqual(self.arr.find(0), 0)

    def test_delete_non_existing(self):
        for i in range(5):
            self.arr.insert(i)

        self.assertRaises(ValueError, self.arr.delete, 5)

    def test_len_of_empty(self):
        self.assertEqual(len(self.arr), 0)

    def test_len_of_not_empty(self):
        for i in range(5):
            self.arr.insert(i)

        self.assertEqual(len(self.arr), 5)

    def test_getitem_unsupported_key_type(self):
        self.assertRaises(TypeError, self.arr.__getitem__, 1.)

    def test_getitem_index_out_of_range(self):
        self.assertRaises(IndexError, self.arr.__getitem__, 1)

    def test_getitem_valid_key(self):
        self.arr.insert(1)

        self.assertEqual(self.arr.__getitem__(0), 1)

    def test_setitem_unsupported_key_type(self):
        self.assertRaises(TypeError, self.arr.__setitem__, 1., 0)

    def test_setitem_index_out_of_range(self):
        self.assertRaises(IndexError, self.arr.__setitem__, 1, 0)

    def test_setitem_valid_key(self):
        self.arr.insert(1)
        raised = False

        try:
            self.arr.__setitem__(0, 2)
        except (TypeError, IndexError):
            raised = True

        self.assertEqual(raised, False)

    def test_contains_in_empty(self):
        self.assertEqual(self.arr.__contains__(0), False)

    def test_contains(self):
        self.arr.insert(0)

        self.assertEqual(self.arr.__contains__(0), True)

    def test_contains_not(self):
        self.arr.insert(0)

        self.assertEqual(self.arr.__contains__(1), False)

    def test_repr_empty(self):
        self.assertEqual(self.arr.__repr__(), 'OrdArray([])')

    def test_repr_one_element(self):
        self.arr.insert(0)

        self.assertEqual(self.arr.__repr__(), 'OrdArray([0])')

    def test_repr_many_elements(self):
        for i in range(5):
            self.arr.insert(i)

        self.assertEqual(self.arr.__repr__(), f'OrdArray([{", ".join(str(i) for i in range(5))}])')
