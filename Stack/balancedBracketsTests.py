import unittest
import random

from balancedBrackets import balancedBrackets


class balancedBracketsTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(balancedBrackets("()()()"), True)
        self.assertEqual(balancedBrackets("(())()"), True)
        self.assertEqual(balancedBrackets("(()))("), False)

    def test_empty(self):
        self.assertEqual(balancedBrackets(""), True)

    def test_border(self):
        self.assertEqual(balancedBrackets("()"), True)
        self.assertEqual(balancedBrackets(")"), False)
        self.assertEqual(balancedBrackets("("), False)


if __name__ == "__main__":
    unittest.main()
