import unittest
import random

from LinkedList import LinkedList, Node


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.empty_linked_list = LinkedList()

        self.one_el_linked_list = LinkedList()
        self.one_el = Node(10)
        self.one_el_linked_list.add_in_tail(self.one_el)

        self.lot_el_linked_list = LinkedList()
        self.lot_el = []
        for i in range(1000):
            el = Node(i)
            self.lot_el.append(el)
            self.lot_el_linked_list.add_in_tail(el)

    def test_regression_delete_empty_list(self):
        self.empty_linked_list.delete(1, False)
        self.assertEqual(self.empty_linked_list.head, None)
        self.assertEqual(self.empty_linked_list.tail, None)

        self.empty_linked_list.delete(1, True)
        self.assertEqual(self.empty_linked_list.head, None)
        self.assertEqual(self.empty_linked_list.tail, None)

    def test_regression_delete_one_el_list(self):
        self.one_el_linked_list.delete(11, False)
        self.assertEqual(self.one_el_linked_list.head.value, 10)
        self.assertEqual(self.one_el_linked_list.tail.value, 10)
        self.assertEqual(self.one_el.value, 10)
        self.assertEqual(self.one_el.next, None)

        self.one_el_linked_list.delete(11, True)
        self.assertEqual(self.one_el_linked_list.head.value, 10)
        self.assertEqual(self.one_el_linked_list.tail.value, 10)
        self.assertEqual(self.one_el.value, 10)
        self.assertEqual(self.one_el.next, None)

        self.one_el_linked_list.delete(10, False)
        self.assertEqual(self.one_el_linked_list.head, None)
        self.assertEqual(self.one_el_linked_list.tail, None)
        self.assertEqual(self.one_el.value, 10)
        self.assertEqual(self.one_el.next, None)

    def test_regression_delete_lot_el_list(self):
        self.lot_el_linked_list.delete(11, False)
        self.assertEqual(self.lot_el_linked_list.head.value, 0)
        self.assertEqual(self.lot_el_linked_list.tail.value, 999)
        for i in range(1000 - 1):
            if i == 11:
                self.assertEqual(self.lot_el_linked_list.find(i), None)
                self.assertEqual(self.lot_el[i].next, None)
                self.assertEqual(self.lot_el[i].value, i)
                continue
            if i == 10:
                self.assertEqual(self.lot_el[i].next, self.lot_el[i + 2])
                self.assertEqual(self.lot_el[i].value, i)
                continue
            if i == 998:
                self.assertEqual(self.lot_el_linked_list.find(i).value, i)
                self.assertEqual(self.lot_el[i].next, self.lot_el[999])
                self.assertEqual(self.lot_el[999].next, None)
            self.assertEqual(self.lot_el_linked_list.find(i).value, i)
            self.assertEqual(self.lot_el[i].next, self.lot_el[i + 1])

        el = Node(0)
        self.lot_el.append(el)
        self.lot_el_linked_list.add_in_tail(el)
        self.lot_el_linked_list.delete(0, True)
        self.assertEqual(self.lot_el_linked_list.head.value, 1)
        self.assertEqual(self.lot_el_linked_list.tail.value, 999)
        self.assertEqual(self.lot_el_linked_list.find(0), None)
        for i in range(1001):
            if i == 0 or i == 1000 or i == 999 or i == 11:
                self.assertEqual(self.lot_el[i].next, None)
                continue
            if i == 10:
                self.assertEqual(self.lot_el[i].next, self.lot_el[i + 2])
                self.assertEqual(self.lot_el[i].value, i)
                continue
            self.assertEqual(self.lot_el[i].next, self.lot_el[i + 1])

    def test_random_delete(self):
        for i in range(10000):
            nodes = []
            linked_list = LinkedList()
            repeats = random.randint(0, 100)
            for i in range(repeats):
                n = Node(random.randint(0, 5))
                nodes.append(n)
                linked_list.add_in_tail(n)
            to_delete = random.randint(0, 5)
            linked_list.delete(to_delete, True)
            first = None
            last = None
            for i, n in enumerate(nodes):
                if n.value == to_delete:
                    self.assertEqual(n.next, None)
                    continue
                if first is None:
                    first = n
                last = n
                for j in range(i + 1, repeats):
                    if nodes[j].value != to_delete:
                        self.assertEqual(n.next, nodes[j])
                        break
            self.assertEqual(linked_list.head, first)
            self.assertEqual(linked_list.tail, last)

    def test_regression_empty_linked_list(self):
        self.empty_linked_list.clean()
        self.assertEqual(self.empty_linked_list.head, None)
        self.assertEqual(self.empty_linked_list.tail, None)

    def test_regression_clean_one_el_list(self):
        self.one_el_linked_list.clean()
        self.assertEqual(self.one_el.next, None)
        self.assertEqual(self.one_el_linked_list.head, None)
        self.assertEqual(self.one_el_linked_list.tail, None)

    def test_regression_clean_lot_el_list(self):
        self.lot_el_linked_list.clean()
        for i in range(1000):
            self.assertEqual(self.lot_el[i].next, None)
            self.assertEqual(self.lot_el[i].value, i)
        self.assertEqual(self.lot_el_linked_list.head, None)
        self.assertEqual(self.lot_el_linked_list.tail, None)

    def test_regression_find_all_empty_linked_list(self):
        arr = self.empty_linked_list.find_all(0)
        self.assertEqual(len(arr), 0)

    def test_regression_find_all_one_el_list(self):
        arr = self.one_el_linked_list.find_all(0)
        self.assertEqual(len(arr), 0)
        arr = self.one_el_linked_list.find_all(10)
        self.assertEqual(len(arr), 1)
        for i in arr:
            self.assertEqual(i.value, 10)

    def test_regression_find_all_lot_el_list(self):
        self.lot_el_linked_list.add_in_tail(Node(0))
        arr = self.lot_el_linked_list.find_all(0)
        self.assertEqual(len(arr), 2)
        for i in arr:
            self.assertEqual(i.value, 0)

    def test_regression_len(self):
        self.assertEqual(self.empty_linked_list.len(), 0)
        self.assertEqual(self.one_el_linked_list.len(), 1)
        self.assertEqual(self.lot_el_linked_list.len(), 1000)

    def test_regression_insert(self):
        el1 = Node(1)
        self.empty_linked_list.insert(None, el1)
        self.assertEqual(self.empty_linked_list.head, el1)
        self.assertEqual(self.empty_linked_list.tail, el1)
        self.assertEqual(el1.next, None)

        el2 = Node(2)
        self.empty_linked_list.insert(el1, el2)
        self.assertEqual(self.empty_linked_list.head, el1)
        self.assertEqual(self.empty_linked_list.tail, el2)
        self.assertEqual(el1.next, el2)
        self.assertEqual(el2.next, None)

        el3 = Node(3)
        self.empty_linked_list.insert(self.empty_linked_list.find(1), el3)
        self.assertEqual(self.empty_linked_list.head, el1)
        self.assertEqual(self.empty_linked_list.tail, el2)
        self.assertEqual(el1.next, el3)
        self.assertEqual(el3.next, el2)
        self.assertEqual(el2.next, None)

    def tearDown(self):
        self.empty_linked_list = None
        self.one_el_linked_list = None
        self.lot_el_linked_list = None


if __name__ == "__main__":
    unittest.main()
