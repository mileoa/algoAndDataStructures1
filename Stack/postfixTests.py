import unittest
import random

from postfix import postfix
from StackReversed import StackReversed


class PosfixTests(unittest.TestCase):

    def test_regression(self):
        s1 = StackReversed()
        s1.push("=")
        s1.push("+")
        s1.push(9)
        s1.push("*")
        s1.push(5)
        s1.push("+")
        s1.push(2)
        s1.push(8)
        self.assertEqual(postfix(s1), 59)

    def test_border(self):
        s1 = StackReversed()
        s1.push("=")
        s1.push(8)
        self.assertEqual(postfix(s1), 8)


if __name__ == "__main__":
    unittest.main()
