import unittest
import random

from PowerSet import PowerSet


class PowerSetTests(unittest.TestCase):

    def test_regression_put(self):
        ps = PowerSet()
        for i in range(2001):
            ps.put(i)
            self.assertEqual(ps.size(), i + 1)
            self.assertTrue(i in ps.slots)
        self.assertEqual(ps.slots, dict(((i, None) for i in range(2001))))

        for i in range(2001):
            ps.put(i)
        self.assertEqual(ps.size(), 2001)
        self.assertEqual(ps.slots, dict(((i, None) for i in range(2001))))

    def test_regression_remove(self):
        ps = PowerSet()
        for i in range(2001):
            ps.put(i)

        self.assertTrue(ps.remove(6))
        self.assertNotIn(6, ps.slots)
        self.assertEqual(ps.size(), 2000)

        self.assertFalse(ps.remove(6))
        self.assertEqual(ps.size(), 2000)

    def test_regression_intersection(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        for i in range(0, 2001, 2):
            ps1.put(i)
        for i in range(2001):
            ps2.put(i)

        self.assertTrue(isinstance(ps1.intersection(ps2), PowerSet))
        self.assertEqual(
            ps1.intersection(ps2).slots, dict(((i, None) for i in range(0, 2001, 2)))
        )

    def test_empty_intersection(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        self.assertEqual(ps1.intersection(ps2).slots, {})

        for i in range(2001):
            ps2.put(i)

        self.assertEqual(ps1.intersection(ps2).slots, {})

    def test_empty_union(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        self.assertEqual(ps1.union(ps2).slots, {})

        for i in range(2001):
            ps2.put(i)

        self.assertEqual(
            ps1.union(ps2).slots,
            dict(((i, None) for i in range(2001))),
        )
        self.assertEqual(
            ps2.union(ps1).slots,
            dict(((i, None) for i in range(2001))),
        )

    def test_regression_union(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        for i in range(0, 2001, 2):
            ps1.put(i)
        for i in range(1, 2001, 2):
            ps2.put(i)

        self.assertTrue(isinstance(ps1.union(ps2), PowerSet))
        self.assertEqual(ps1.union(ps2).slots, dict(((i, None) for i in range(2001))))

    def test_empty_difference(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        self.assertEqual(ps1.difference(ps2).slots, {})

        for i in range(2001):
            ps1.put(i)

        self.assertTrue(isinstance(ps1.difference(ps2), PowerSet))
        self.assertEqual(
            ps1.difference(ps2).slots, dict(((i, None) for i in range(2001)))
        )
        self.assertEqual(ps2.difference(ps1).slots, {})

    def test_regression_difference(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        for i in range(0, 2001, 2):
            ps1.put(i)
        for i in range(1, 2001, 2):
            ps2.put(i)

        ps1.put(2002)
        ps2.put(2002)

        self.assertTrue(isinstance(ps1.difference(ps2), PowerSet))
        self.assertEqual(
            ps1.difference(ps2).slots, dict(((i, None) for i in range(0, 2001, 2)))
        )
        self.assertEqual(
            ps2.difference(ps1).slots, dict(((i, None) for i in range(1, 2001, 2)))
        )
        self.assertEqual(ps1.difference(ps1).slots, {})

    def test_empty_issubset(self):
        ps1 = PowerSet()
        ps2 = PowerSet()
        self.assertTrue(ps2.issubset(ps1))

        for i in range(2000):
            ps1.put(i)

        self.assertFalse(ps2.issubset(ps1))
        self.assertTrue(ps1.issubset(ps2))

    def test_regression_issubset(self):
        ps1 = PowerSet()
        ps2 = PowerSet()

        for i in range(2000):
            ps1.put(i)
        for i in range(2001):
            ps2.put(i)

        self.assertTrue(ps2.issubset(ps1))
        self.assertFalse(ps1.issubset(ps2))

        ps1.put(2000)
        self.assertTrue(ps1.issubset(ps2))


if __name__ == "__main__":
    unittest.main()
