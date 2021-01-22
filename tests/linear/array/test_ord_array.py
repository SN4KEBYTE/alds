from unittest import TestCase

from alds.linear.array.ord_array import OrdArray

_ARRAY_SIZE: int = 5
_TEST_VALUE: int = 0


class TestOrdArray(TestCase):
    def __fill_array(self, start: int = 0, stop: int = _ARRAY_SIZE):
        for i in range(start, stop):
            self.arr.insert(i)

    def setUp(self) -> None:
        self.arr = OrdArray()

    def test_insert_to_empty(self):
        self.arr.insert(_TEST_VALUE)

        self.assertEqual(self.arr[0], _TEST_VALUE)

    def test_insert_into_beginning(self):
        self.__fill_array(1)
        self.arr.insert(_TEST_VALUE)

        self.assertEqual(self.arr[0], _TEST_VALUE)

    def test_insert_to_end(self):
        val: int = _ARRAY_SIZE - 1

        self.__fill_array(stop=val)
        self.arr.insert(val)

        self.assertEqual(self.arr[-1], val)

    def test_insert_into_middle(self):
        self.arr.insert(_TEST_VALUE - 1)
        self.arr.insert(_TEST_VALUE)
        self.arr.insert(_TEST_VALUE + 1)

        self.assertEqual(self.arr[1], _TEST_VALUE)

    def test_find_in_empty(self):
        self.assertRaises(ValueError, self.arr.find, _TEST_VALUE)

    def test_find_existing_all_elements_unique(self):
        self.__fill_array()

        pos = self.arr.find(_ARRAY_SIZE - 1)

        self.assertEqual(pos, _ARRAY_SIZE - 1)

    def test_find_existing_repeated_elements(self):
        self.__fill_array()
        self.__fill_array()

        pos = self.arr.find(_TEST_VALUE)

        self.assertEqual(pos, 1)

    def test_find_non_existing(self):
        self.__fill_array()

        self.assertRaises(ValueError, self.arr.find, _ARRAY_SIZE)

    def test_delete_from_empty(self):
        self.assertRaises(ValueError, self.arr.delete, _TEST_VALUE)

    def test_delete_existing_all_elements_unique(self):
        self.__fill_array()

        self.arr.delete(_TEST_VALUE)

        self.assertRaises(ValueError, self.arr.find, _TEST_VALUE)

    def test_delete_existing_repeated_elements(self):
        self.__fill_array()
        self.__fill_array()

        self.arr.delete(_TEST_VALUE)

        self.assertEqual(self.arr.find(0), 0)

    def test_delete_non_existing(self):
        self.__fill_array()

        self.assertRaises(ValueError, self.arr.delete, _ARRAY_SIZE)

    def test_len_of_empty(self):
        self.assertEqual(len(self.arr), 0)

    def test_len_of_not_empty(self):
        self.__fill_array()

        self.assertEqual(len(self.arr), _ARRAY_SIZE)

    def test_reversed_empty(self):
        self.assertEqual(reversed(self.arr), [])

    def test_reversed_not_empty(self):
        self.__fill_array()

        self.assertEqual(reversed(self.arr), list(reversed(list(range(_ARRAY_SIZE)))))

    def test_getitem_unsupported_key_type(self):
        self.assertRaises(TypeError, self.arr.__getitem__, 1.)

    def test_getitem_index_out_of_range(self):
        self.assertRaises(IndexError, self.arr.__getitem__, 1)

    def test_getitem_valid_int_key(self):
        self.arr.insert(_TEST_VALUE)

        self.assertEqual(self.arr.__getitem__(0), _TEST_VALUE)

    def test_getitem_valid_slice(self):
        self.__fill_array()

        self.assertEqual(self.arr[1:3], OrdArray([1, 2]))

    def test_delitem_unsupported_key_type(self):
        self.assertRaises(TypeError, self.arr.__delitem__, 1.)

    def test_delitem_index_out_of_range(self):
        self.assertRaises(IndexError, self.arr.__delitem__, 1)

    def test_delitem_valid_int_key(self):
        self.arr.insert(_TEST_VALUE)

        self.arr.__delitem__(0)

        self.assertEqual(self.arr, OrdArray())

    def test_delitem_valid_slice(self):
        self.__fill_array()

        del self.arr[1:3]

        self.assertEqual(self.arr[1:3], OrdArray([3, 4]))

    def test_eq_empty(self):
        self.assertEqual(self.arr, list())
        self.assertEqual(self.arr, tuple())
        self.assertEqual(self.arr, OrdArray())

    def test_eq_not_empty(self):
        self.__fill_array()

        self.assertEqual(self.arr, list(range(5)))
        self.assertEqual(self.arr, tuple(range(5)))
        self.assertEqual(self.arr, OrdArray(range(5)))

    def test_contains_in_empty(self):
        self.assertEqual(self.arr.__contains__(_TEST_VALUE), False)

    def test_contains(self):
        self.arr.insert(_TEST_VALUE)

        self.assertEqual(self.arr.__contains__(_TEST_VALUE), True)

    def test_contains_not(self):
        self.arr.insert(_TEST_VALUE)

        self.assertEqual(self.arr.__contains__(_TEST_VALUE + 1), False)
