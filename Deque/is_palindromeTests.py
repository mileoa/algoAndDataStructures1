import unittest
import random

from is_palindrome import is_palindrome


class IsPalindromeTests(unittest.TestCase):

    def test_regression(self):

        self.assertEqual(is_palindrome("aba"), True)
        self.assertEqual(is_palindrome("abab"), False)
        self.assertEqual(is_palindrome("abba"), True)
        self.assertEqual(is_palindrome("cabxbac"), True)
        self.assertEqual(is_palindrome("cabxbсc"), False)

    def test_border(self):
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("aa"), True)
        self.assertEqual(is_palindrome("ab"), False)


if __name__ == "__main__":
    unittest.main()
