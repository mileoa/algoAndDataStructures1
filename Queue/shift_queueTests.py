import unittest
import random

from shift_queue import shift_queue, Queue


class shift_queueTests(unittest.TestCase):

    def test_regression(self):

        for i in range(6):
            q = Queue()
            for j in range(5):
                q.enqueue(j)
            q.shift(i)
            el = q.dequeu()
            if i < 5:
                self.assertEqual(el, i + 1)
            else:
                self.assertEqual(el, 1)


if __name__ == "__main__":
    unittest.main()
