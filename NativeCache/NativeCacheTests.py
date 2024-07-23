import unittest
import random

from NativeCache import NativeCache


class NativeCacheTests(unittest.TestCase):

    def test_regression_hash_fun(self):
        nc_size = 19
        nc = NativeCache(nc_size)
        hash_count = {}
        for i in range(nc_size):
            hash = nc.hash_fun(str(i))
            if hash not in hash_count:
                hash_count[hash] = 0
            hash_count[hash] += 1

        for el, count in hash_count.items():
            self.assertLessEqual(count, 2)
            self.assertLessEqual(el, nc_size)
            self.assertGreaterEqual(el, 0)

    def test_regression_put(self):
        nc_size = 19
        nc = NativeCache(nc_size)

        # Common put.
        for i in range(nc_size):
            nc.put(str(i), i)
            self.assertIn(str(i), nc.slots)
            self.assertIn(i, nc.values)
            self.assertEqual(nc.item_count, i + 1)
            self.assertEqual(nc.hits[nc.slots.index(str(i))], 1)

        # Change value of existing key.
        for i in range(nc_size - 1):
            nc.put(str(i), 99)
            self.assertEqual(nc.hits[nc.slots.index(str(i))], 2)
            self.assertEqual(nc.values[nc.slots.index(str(i))], 99)
        self.assertEqual(nc.item_count, nc_size)

        self.assertEqual(nc.values[nc.slots.index(str(nc_size - 1))], nc_size - 1)

        # Put to full list.
        nc.put(str(nc_size), nc_size)
        for i in range(nc_size):
            self.assertNotIn(str(nc_size - 1), nc.slots)
            self.assertIn(str(nc_size), nc.slots)
        self.assertEqual(nc.item_count, nc_size)

    def test_regression_get(self):
        nc_size = 19
        nc = NativeCache(nc_size)
        for i in range(nc.size):
            nc.put(str(i), i)

        for i in nc.slots:
            self.assertEqual(nc.get(str(i)), int(i))
            self.assertEqual(nc.hits[nc.slots.index(i)], 2)

        # is_key full list by not existing key.
        self.assertIsNone(nc.get("abc"))

    def test_empty_get(self):
        nc_size = 19
        nc = NativeCache(nc_size)
        self.assertIsNone(nc.get("123"))
        for i in nc.hits:
            self.assertEqual(i, 0)

        # One element.
        nc.put("123", 123)
        self.assertEqual(nc.get("123"), 123)

    def test_regression_is_key(self):
        nc_size = 19
        nc = NativeCache(nc_size)

        for i in range(nc.size):
            nc.put(str(i), i)

        for i in nc.slots:
            self.assertTrue(nc.is_key(str(i)))
            self.assertEqual(nc.hits[nc.slots.index(str(i))], 2)

        for i in nc.slots:
            self.assertEqual(nc.is_key(str(i)), True)
            self.assertEqual(nc.hits[nc.slots.index(str(i))], 3)

        # is_key full list by not existing key.
        self.assertEqual(nc.is_key("abc"), False)
        for i in nc.slots:
            self.assertEqual(nc.hits[nc.slots.index(str(i))], 3)

    def test_empty_is_key(self):
        nc_size = 19
        nc = NativeCache(nc_size)

        # Empty list.
        self.assertEqual(nc.is_key("123"), False)

        # One element.
        nc.put("123", 123)
        self.assertEqual(nc.is_key("123"), True)


if __name__ == "__main__":
    unittest.main()
