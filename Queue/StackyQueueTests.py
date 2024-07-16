import unittest
import random

from StackyQueue import StackyQueue


class StackyQueueTests(unittest.TestCase):

    def setUp(self):
        self.q = StackyQueue()

    def test_regression_enqueue(self):
        self.assertEqual(self.q.size(), 0)

        for i in range(5):
            self.q.enqueue(i)
            self.assertEqual(self.q.size(), i + 1)

        for i in range(7):
            if i < 5:
                self.assertEqual(self.q.dequeue(), i)
                self.assertEqual(self.q.size(), 4 - i)
                continue
            self.assertEqual(self.q.dequeue(), None)
            self.assertEqual(self.q.size(), 0)

    def tearDown(self):
        self.q = None


if __name__ == "__main__":
    unittest.main()
