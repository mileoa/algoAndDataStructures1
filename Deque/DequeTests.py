import unittest
import random

from Deque import Deque


class DequeTests(unittest.TestCase):

    def test_regression(self):
        d = Deque()
        self.assertEqual(d.size(), 0)
        self.assertEqual(d.removeFront(), None)
        self.assertEqual(d.removeTail(), None)

        for i in range(10):
            d.addFront(i)
            self.assertEqual(d.size(), i + 1)
        for i in range(10):
            self.assertEqual(d.removeTail(), i)
            self.assertEqual(d.size(), 10 - 1 - i)

        for i in range(10):
            d.addTail(i)
            self.assertEqual(d.size(), i + 1)
        for i in range(10):
            self.assertEqual(d.removeFront(), i)
            self.assertEqual(d.size(), 10 - 1 - i)


if __name__ == "__main__":
    unittest.main()
