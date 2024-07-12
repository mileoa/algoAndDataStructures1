import unittest
import random

from DynArray import DynArray


class DynArrayTests(unittest.TestCase):

    def test_insert_regression(self):
        array = DynArray()

        self.assertRaises(IndexError, array.insert, -1, 0)
        self.assertRaises(IndexError, array.insert, 17, 0)

        for i in range(15):
            array.append(i)

        array.insert(15, 15)
        self.assertEqual(array.capacity, 16)
        array.insert(16, 16)
        self.assertEqual(array.capacity, 32)

        for i, el in enumerate(array):
            self.assertEqual(el, i)

        array.insert(10, -1)
        self.assertEqual(array.capacity, 32)
        for i, el in enumerate(array):
            if i < 10:
                self.assertEqual(el, i)
                continue
            if i == 10:
                self.assertEqual(el, -1)
                continue
            self.assertEqual(el, i - 1)

        array.insert(0, -1)
        array.insert(0, -2)
        self.assertEqual(array.capacity, 32)
        for i, el in enumerate(array):
            if i == 0:
                self.assertEqual(el, -2)
                continue
            if i == 1:
                self.assertEqual(el, -1)
                continue
            if i < 12:
                self.assertEqual(el, i - 2)
                continue
            if i == 12:
                self.assertEqual(el, -1)
                continue
            self.assertEqual(el, i - 3)

    def test_delete_regression(self):
        array = DynArray()
        for i in range(17):
            array.append(i)

        self.assertRaises(IndexError, array.delete, -1)
        self.assertRaises(IndexError, array.delete, 17)
        array.delete(7)
        for i, el in enumerate(array):
            if i < 7:
                self.assertEqual(el, i)
                continue
            self.assertEqual(el, i + 1)
        self.assertEqual(array.capacity, 32)

        array.delete(7)
        for i, el in enumerate(array):
            if i < 7:
                self.assertEqual(el, i)
                continue
            self.assertEqual(el, i + 2)
        self.assertEqual(array.capacity, 21)

        for i in range(5):
            array.delete(7)
        for i, el in enumerate(array):
            if i < 7:
                self.assertEqual(el, i)
                continue
            self.assertEqual(el, i + 7)
        self.assertEqual(array.capacity, 16)


if __name__ == "__main__":
    unittest.main()
