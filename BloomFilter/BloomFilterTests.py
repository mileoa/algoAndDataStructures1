import unittest
import random

from BloomFilter import BloomFilter


class BloomFilterTests(unittest.TestCase):

    def setUp(self):
        self.bf = BloomFilter(32)
        self.test_strings = [
            "0123456789",
            "1234567890",
            "2345678901",
            "3456789012",
            "4567890123",
            "5678901234",
            "6789012345",
            "7890123456",
            "8901234567",
            "9012345678",
        ]

    def test_regression_add(self):
        self.bf.add("0123456789")
        h1 = self.bf.hash1(self.test_strings[0])
        h2 = self.bf.hash2(self.test_strings[0])
        self.assertEqual(h1 & self.bf.bit_list, h1)
        self.assertEqual(h2 & self.bf.bit_list, h2)
        self.assertEqual(self.bf.bit_list ^ (h1 | h2), 0)

    def test_regression_is_value(self):
        for s in self.test_strings:
            self.assertFalse(self.bf.is_value(s))

        self.bf.add(self.test_strings[0])
        self.assertTrue(self.bf.is_value(self.test_strings[0]))

    def tearDown(self):
        del self.bf
        del self.test_strings


if __name__ == "__main__":
    unittest.main()
