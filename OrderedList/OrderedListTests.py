import unittest
import random

from OrderedList import OrderedList, Node


class OrderedListTests(unittest.TestCase):

    def test_regression_compare(self):
        ol = OrderedList(True)
        self.assertEqual(ol.compare(1, 2), -1)
        self.assertEqual(ol.compare(2, 1), 1)
        self.assertEqual(ol.compare(2, 2), 0)

    def test_regression_add_asc(self):
        ol = OrderedList(True)
        for i in range(5):
            ol.add(i)

        ol.add(-1)
        ol.add(-1)
        ol.add(2)
        ol.add(4)
        ol.add(5)

        for i, el in enumerate(ol.get_all()):
            if i == 0 and el.value == -1:
                self.assertEqual(el.prev, None)
                self.assertEqual(el.next.value, -1)
                continue
            if i == 1 and el.value == -1:
                self.assertEqual(el.prev.value, -1)
                self.assertEqual(el.next.value, 0)
                continue
            if i == 4 and el.value == 2:
                self.assertEqual(el.prev.value, 1)
                self.assertEqual(el.next.value, 2)
                continue
            if i == 5 and el.value == 2:
                self.assertEqual(el.prev.value, 2)
                self.assertEqual(el.next.value, 3)
                continue
            if i == 7 and el.value == 4:
                self.assertEqual(el.prev.value, 3)
                self.assertEqual(el.next.value, 4)
                continue
            if i == 8 and el.value == 4:
                self.assertEqual(el.prev.value, 4)
                self.assertEqual(el.next.value, 5)
                continue
            if el.value == 5:
                self.assertEqual(el.prev.value, 4)
                self.assertEqual(el.next, None)
                continue
            self.assertEqual(el.prev.value, el.value - 1)
            self.assertEqual(el.next.value, el.value + 1)

        self.assertEqual(ol.head.value, -1)
        self.assertEqual(ol.tail.value, 5)

    def test_regression_add_desc(self):
        ol = OrderedList(False)
        for i in range(5):
            ol.add(i)

        ol.add(-1)
        ol.add(-1)
        ol.add(2)
        ol.add(4)
        ol.add(5)

        for i, el in enumerate(ol.get_all()):
            if i == 8 and el.value == -1:
                self.assertEqual(el.prev.value, 0)
                self.assertEqual(el.next.value, -1)
                continue
            if i == 9 and el.value == -1:
                self.assertEqual(el.prev.value, -1)
                self.assertEqual(el.next, None)
                continue
            if i == 4 and el.value == 2:
                self.assertEqual(el.prev.value, 3)
                self.assertEqual(el.next.value, 2)
                continue
            if i == 5 and el.value == 2:
                self.assertEqual(el.prev.value, 2)
                self.assertEqual(el.next.value, 1)
                continue
            if i == 1 and el.value == 4:
                self.assertEqual(el.prev.value, 5)
                self.assertEqual(el.next.value, 4)
                continue
            if i == 2 and el.value == 4:
                self.assertEqual(el.prev.value, 4)
                self.assertEqual(el.next.value, 3)
                continue
            if i == 0 and el.value == 5:
                self.assertEqual(el.prev, None)
                self.assertEqual(el.next.value, 4)
                continue
            self.assertEqual(el.prev.value, el.value + 1)
            self.assertEqual(el.next.value, el.value - 1)

        self.assertEqual(ol.head.value, 5)
        self.assertEqual(ol.tail.value, -1)

    def test_regression_delete(self):
        ol = OrderedList(True)
        for i in range(5):
            ol.add(i)
        nodes = ol.get_all()
        ol.delete(0)
        for i, node in enumerate(nodes):
            if i == 0:
                self.assertEqual(node.prev, None)
                self.assertEqual(node.next, None)
                continue
            if i == 1:
                self.assertEqual(node.prev, None)
                self.assertEqual(node.next, nodes[i + 1])
                continue
            if i == 4:
                self.assertEqual(node.prev, nodes[i - 1])
                self.assertEqual(node.next, None)
                continue
            self.assertEqual(node.prev, nodes[i - 1])
            self.assertEqual(node.next, nodes[i + 1])

        ol = OrderedList(True)
        for i in range(5):
            ol.add(i)
        nodes = ol.get_all()
        ol.delete(3)
        ol.delete(4)
        for i, node in enumerate(nodes):
            if i >= 3:
                self.assertEqual(node.prev, None)
                self.assertEqual(node.next, None)
                continue
            if i == 0:
                self.assertEqual(node.prev, None)
                self.assertEqual(node.next, nodes[i + 1])
                continue
            if i == 2:
                self.assertEqual(node.prev, nodes[i - 1])
                self.assertEqual(node.next, None)
                continue
            self.assertEqual(node.prev, nodes[i - 1])
            self.assertEqual(node.next, nodes[i + 1])


if __name__ == "__main__":
    unittest.main()
