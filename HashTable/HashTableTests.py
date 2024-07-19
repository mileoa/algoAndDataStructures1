import unittest
import random

from HashTable import HashTable


class HashTableTests(unittest.TestCase):

    def test_regression_hash_fun(self):
        ht_size = 19
        ht = HashTable(ht_size, 1)
        hash_count = {}
        for i in range(ht_size):
            hash = ht.hash_fun(str(i))
            if hash not in hash_count:
                hash_count[hash] = 0
            hash_count[hash] += 1

        for el, count in hash_count.items():
            self.assertLessEqual(count, 2)
            self.assertLessEqual(el, ht_size)
            self.assertGreaterEqual(el, 0)

    def test_regression_put(self):
        ht_size = 17
        ht = HashTable(ht_size, 1)
        for i in range(ht_size):
            self.assertIsNotNone(ht.put("0"))

        self.assertIsNone(ht.put("0"))

    def test_regression_seek_slot(self):
        ht_size = 7127
        ht = HashTable(ht_size, 1)
        for i in range(ht_size - 1):
            ht.put("0")

        self.assertEqual(ht.seek_slot("1"), ht.slots.index(None))
        ht.put("0")
        self.assertIsNone(ht.seek_slot("2"))

    def test_regression_find(self):
        ht_size = 7127
        ht = HashTable(ht_size, 1)
        for i in range(ht_size):
            ht.put(str(i))

        for i in range(ht_size):
            self.assertEqual(ht.find(str(i)), ht.slots.index(str(i)))
        self.assertIsNone(ht.seek_slot(ht_size + 1))


if __name__ == "__main__":
    unittest.main()
