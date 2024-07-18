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

    def test_random_delete(self):
        for i in range(10000):
            ol = OrderedList(True)

            repeats = random.randint(0, 10)
            for j in range(repeats):
                n = random.randint(0, 5)
                ol.add(n)

            nodes = ol.get_all()

            to_delete = random.randint(0, 5)
            if to_delete in [x.value for x in nodes]:
                delete_index = [x.value for x in nodes].index(to_delete)
            else:
                delete_index = -1
            deleted_node = ol.find(to_delete)

            ol.delete(to_delete)

            first = None
            last = None
            for k, n in enumerate(nodes):
                if n == deleted_node:
                    self.assertEqual(deleted_node.next, None)
                    self.assertEqual(deleted_node.prev, None)
                    continue
                if first is None:
                    first = n
                last = n
                for j in range(k + 1, repeats):
                    if j != delete_index:
                        self.assertEqual(n.next, nodes[j])
                        break
                for p in range(k - 1, -1, -1):
                    if p != delete_index:
                        self.assertEqual(n.prev, nodes[p])
                        break

            self.assertEqual(ol.head, first)
            self.assertEqual(ol.tail, last)


if __name__ == "__main__":
    unittest.main()
