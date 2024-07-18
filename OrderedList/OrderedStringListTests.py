import unittest
import random

from OrderedList import OrderedStringList


class OrderedStringListTests(unittest.TestCase):

    def test_regression_compare(self):
        ol = OrderedStringList(True)
        self.assertEqual(ol.compare("   123 ", "   423 "), -1)
        self.assertEqual(ol.compare(" 123", "  123          "), 0)
        self.assertEqual(ol.compare("321", "   311   "), 1)


if __name__ == "__main__":
    unittest.main()
