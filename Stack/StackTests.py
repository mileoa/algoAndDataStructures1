import unittest
import random

from Stack import Stack


class StackTests(unittest.TestCase):

    def test_regression(self):
        s = Stack()
        self.assertEqual(s.pop(), None)
        self.assertEqual(s.peek(), None)
        self.assertEqual(s.size(), 0)

        for i in range(5):
            s.push(i)
            self.assertEqual(s.size(), i + 1)

        for i in range(4, -2, -1):
            if i > -1:
                self.assertEqual(s.pop(), i)
                self.assertEqual(s.size(), i)
                continue
            self.assertEqual(s.pop(), None)
            self.assertEqual(s.size(), 0)


if __name__ == "__main__":
    unittest.main()
