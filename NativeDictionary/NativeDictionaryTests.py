import unittest
import random

from NativeDictionary import NativeDictionary


class NativeDictionaryTests(unittest.TestCase):

    def test_regression_hash_fun(self):
        nd_size = 19
        nd = NativeDictionary(nd_size)
        hash_count = {}
        for i in range(nd_size):
            hash = nd.hash_fun(str(i))
            if hash not in hash_count:
                hash_count[hash] = 0
            hash_count[hash] += 1

        for el, count in hash_count.items():
            self.assertLessEqual(count, 2)
            self.assertLessEqual(el, nd_size)
            self.assertGreaterEqual(el, 0)

    def test_regression_is_key(self):
        nd_size = 19
        nd = NativeDictionary(nd_size)

        # Empty list.
        self.assertEqual(nd.is_key("123"), False)

        # One element.
        nd.put("123", 123)
        self.assertEqual(nd.is_key("123"), True)

        # Common is_key.
        for i in range(nd.size - 1):
            nd.put(str(i), i)

        for i in nd.slots:
            self.assertEqual(nd.is_key(i), True)

        # is_key full list by not existing key.
        self.assertEqual(nd.is_key("abc"), False)

    def test_regression_put(self):
        nd_size = 19
        nd = NativeDictionary(nd_size)

        # Common put.
        for i in range(nd_size):
            nd.put(str(i), i)
            self.assertIn(str(i), nd.slots)
            self.assertIn(i, nd.values)
            self.assertEqual(nd.item_count, i + 1)

        # Put to full list.
        nd.put(str(nd_size), nd_size)
        for i in range(nd_size):
            self.assertNotEqual(nd.slots[i], str(nd_size))
            self.assertNotEqual(nd.values[i], nd_size)

        # Change value of existing key.
        nd.put("5", 99)
        for i in range(nd_size):
            if i == 5:
                self.assertEqual(nd.values[nd.slots.index(str(i))], 99)
                continue
            self.assertEqual(nd.values[nd.slots.index(str(i))], i)

        # Change value on only element in list.
        nd_size = 19
        nd = NativeDictionary(nd_size)

        nd.put("asd", 123)
        self.assertIn("asd", nd.slots)
        self.assertIn(123, nd.values)

        nd.put("asd", 545)
        self.assertEqual(nd.values[nd.slots.index("asd")], 545)
        self.assertEqual(nd.item_count, 1)

    def test_regression_get(self):
        nd_size = 19
        nd = NativeDictionary(nd_size)

        # Empty list.
        self.assertIsNone(nd.get("123"))

        # One element.
        nd.put("123", 123)
        self.assertEqual(nd.get("123"), 123)

        # Common get.
        for i in range(nd.size - 1):
            nd.put(str(i), i)

        for i in nd.slots:
            self.assertEqual(nd.get(i), int(i))

        # is_key full list by not existing key.
        self.assertIsNone(nd.get("abc"))

    def test_regression_seek_slot(self):
        nd_size = 7127
        nd = NativeDictionary(nd_size)
        for i in range(nd_size - 1):
            nd.put(str(i), i)

        # Find index of last empty place.
        self.assertEqual(nd.seek_slot(str(nd_size - 1)), nd.slots.index(None))

        # Check common seek correct.
        nd.put(str(nd_size - 1), nd_size - 1)
        for i in range(nd_size):
            self.assertEqual(nd.seek_slot(str(i)), nd.slots.index(str(i)))

        # Seek slot when not empty place.
        self.assertIsNone(nd.seek_slot(str(nd_size)))


if __name__ == "__main__":
    unittest.main()
