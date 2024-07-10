import unittest
import random

from LinkedList import LinkedList, Node


class LinkedListTests(unittest.TestCase):

    def setUp(self):
        self.empty_linked_list = LinkedList()

        self.one_el_linked_list = LinkedList()
        self.one_el_linked_list.add_in_tail(Node(10))

        self.lot_el_linked_list = LinkedList()
        for i in range(1000):
            self.lot_el_linked_list.add_in_tail(Node(i))

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

        self.one_el_linked_list.delete(11, True)
        self.assertEqual(self.one_el_linked_list.head.value, 10)
        self.assertEqual(self.one_el_linked_list.tail.value, 10)

        self.one_el_linked_list.delete(10, False)
        self.assertEqual(self.one_el_linked_list.head, None)
        self.assertEqual(self.one_el_linked_list.tail, None)

    def test_regression_delete_lot_el_list(self):
        self.lot_el_linked_list.delete(11, False)
        self.assertEqual(self.lot_el_linked_list.head.value, 0)
        self.assertEqual(self.lot_el_linked_list.tail.value, 999)
        for i in range(1000):
            if i == 11:
                self.assertEqual(self.lot_el_linked_list.find(11), None)
                continue
            self.assertEqual(self.lot_el_linked_list.find(i).value, i)

        self.lot_el_linked_list.add_in_tail(Node(0))
        self.lot_el_linked_list.delete(0, True)
        self.assertEqual(self.lot_el_linked_list.head.value, 1)
        self.assertEqual(self.lot_el_linked_list.tail.value, 999)
        for i in range(1000):
            if i == 0 or i == 11:
                self.assertEqual(self.lot_el_linked_list.find(0), None)
                continue
            self.assertEqual(self.lot_el_linked_list.find(i).value, i)

        self.lot_el_linked_list.add_in_tail(Node(1))
        self.lot_el_linked_list.delete(1, False)
        self.assertEqual(self.lot_el_linked_list.head.value, 2)
        self.assertEqual(self.lot_el_linked_list.tail.value, 1)

    def test_regression_empty_linked_list(self):
        self.empty_linked_list.clean()
        self.assertEqual(self.empty_linked_list.head, None)
        self.assertEqual(self.empty_linked_list.tail, None)

    def test_regression_clean_one_el_list(self):
        self.one_el_linked_list.clean()
        self.assertEqual(self.one_el_linked_list.head, None)
        self.assertEqual(self.one_el_linked_list.tail, None)

    def test_regression_clean_lot_el_list(self):
        self.lot_el_linked_list.clean()
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
        self.empty_linked_list.insert(None, Node(1))
        self.assertEqual(self.empty_linked_list.head.value, 1)
        self.assertEqual(self.empty_linked_list.tail.value, 1)

        self.empty_linked_list.insert(None, Node(2))
        self.assertEqual(self.empty_linked_list.head.value, 2)
        self.assertEqual(self.empty_linked_list.tail.value, 1)

        self.empty_linked_list.insert(self.empty_linked_list.find(1), Node(3))
        self.assertEqual(self.empty_linked_list.head.value, 2)
        self.assertEqual(self.empty_linked_list.tail.value, 3)

    def tearDown(self):
        self.empty_linked_list = None
        self.one_el_linked_list = None
        self.lot_el_linked_list = None


if __name__ == "__main__":
    unittest.main()
