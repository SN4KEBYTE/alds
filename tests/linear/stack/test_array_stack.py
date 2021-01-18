from unittest import TestCase

from alds.linear.stack.array_stack import ArrayStack
from alds.linear.stack._exceptions import StackError


_STACK_SIZE: int = 3


class TestArrayStack(TestCase):
    def __fill_stack(self):
        for i in range(_STACK_SIZE):
            self.stack.push(i)

    def setUp(self) -> None:
        self.stack = ArrayStack(_STACK_SIZE)

    def test_push_to_empty(self):
        self.stack.push(0)

        self.assertEqual(len(self.stack), 1)

    def test_push_to_full(self):
        self.__fill_stack()

        self.assertRaises(StackError, self.stack.push, 0)

    def test_pop_from_empty(self):
        self.assertRaises(StackError, self.stack.pop)

    def test_pop_from_non_empty(self):
        self.__fill_stack()
        elem = self.stack.pop()

        self.assertEqual(elem, _STACK_SIZE - 1)
        self.assertEqual(len(self.stack), _STACK_SIZE - 1)

    def test_peek_empty(self):
        self.assertRaises(StackError, self.stack.peek)

    def test_peek_non_empty(self):
        self.__fill_stack()
        elem = self.stack.peek()

        self.assertEqual(elem, _STACK_SIZE - 1)
        self.assertEqual(len(self.stack), _STACK_SIZE)

    def test_is_empty_really_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

    def test_is_full_really_empty(self):
        self.__fill_stack()

        self.assertEqual(self.stack.is_empty(), False)

    def test_is_full_really_full(self):
        self.assertEqual(self.stack.is_full(), False)

    def test_is_empty_really_full(self):
        self.__fill_stack()

        self.assertEqual(self.stack.is_full(), True)
