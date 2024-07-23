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
        for i, b in enumerate(self.bf.byte_list):
            if i in (h1, h2):
                self.assertEqual(b, 1)
                continue
            self.assertEqual(b, 0)

        self.bf.add("8901234567")
        self.assertEqual(self.bf.byte_list[self.bf.hash1(self.test_strings[8])], 1)
        self.assertEqual(self.bf.byte_list[self.bf.hash2(self.test_strings[8])], 1)

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
