import unittest
import random

from LinkedList2 import LinkedList2, Node


class LinkedList2Tests(unittest.TestCase):

    def setUp(self):
        self.empty_linked_list = LinkedList2()

        self.one_el_linked_list = LinkedList2()
        self.one_el = Node(10)
        self.one_el_linked_list.add_in_tail(self.one_el)

        self.lot_el_linked_list = LinkedList2()
        self.lot_el = []
        for i in range(1000):
            el = Node(i)
            self.lot_el.append(el)
            self.lot_el_linked_list.add_in_tail(el)

    def test_regression_find(self):
        self.assertEqual(self.empty_linked_list.find(1), None)

        self.assertEqual(self.one_el_linked_list.find(10), self.one_el)

        for i in range(1000):
            self.assertEqual(self.lot_el_linked_list.find(i), self.lot_el[i])

    def test_regression_find_all(self):
        self.assertEqual(self.empty_linked_list.find_all(1), [])

        self.assertEqual(self.one_el_linked_list.find_all(10), [self.one_el])

        n = Node(500)
        self.lot_el_linked_list.add_in_tail(n)
        self.assertEqual(self.lot_el_linked_list.find_all(500), [self.lot_el[500], n])

    def test_random_delete(self):
        for i in range(10000):
            nodes = []
            linked_list = LinkedList2()
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
                    self.assertEqual(n.prev, None)
                    continue
                if first is None:
                    first = n
                last = n
                for j in range(i + 1, repeats):
                    if nodes[j].value != to_delete:
                        self.assertEqual(n.next, nodes[j])
                        break
                for k in range(i - 1, -1, -1):
                    if nodes[k].value != to_delete:
                        self.assertEqual(n.prev, nodes[k])
                        break
            self.assertEqual(linked_list.head, first)
            self.assertEqual(linked_list.tail, last)

    def test_add_in_head(self):
        n = Node(1234)
        self.empty_linked_list.add_in_head(n)
        self.assertEqual(self.empty_linked_list.head, n)
        self.assertEqual(self.empty_linked_list.tail, n)
        self.assertEqual(n.next, None)
        self.assertEqual(n.prev, None)

        n = Node(1234)
        self.one_el_linked_list.add_in_head(n)
        self.assertEqual(self.one_el_linked_list.head, n)
        self.assertEqual(self.one_el_linked_list.tail, self.one_el)
        self.assertEqual(n.next, self.one_el)
        self.assertEqual(n.prev, None)
        self.assertEqual(self.one_el.next, None)
        self.assertEqual(self.one_el.prev, n)

        n = Node(-1)
        self.lot_el_linked_list.add_in_head(n)
        self.lot_el = [n] + self.lot_el
        self.assertEqual(self.lot_el_linked_list.head, n)
        self.assertEqual(self.lot_el_linked_list.tail, self.lot_el[-1])
        for i, node in enumerate(self.lot_el):
            if i == len(self.lot_el) - 1:
                self.assertEqual(node.next, None)
            else:
                self.assertEqual(node.next, self.lot_el[i + 1])
            if i == 0:
                self.assertEqual(node.prev, None)
            else:
                self.assertEqual(node.prev, self.lot_el[i - 1])

    def test_clean_regression(self):
        self.empty_linked_list.clean()
        self.assertEqual(self.empty_linked_list.head, None)
        self.assertEqual(self.empty_linked_list.tail, None)

        self.one_el_linked_list.clean()
        self.assertEqual(self.one_el_linked_list.head, None)
        self.assertEqual(self.one_el_linked_list.tail, None)
        self.assertEqual(self.one_el.prev, None)
        self.assertEqual(self.one_el.next, None)

        self.lot_el_linked_list.clean()
        self.assertEqual(self.lot_el_linked_list.head, None)
        self.assertEqual(self.lot_el_linked_list.tail, None)
        for node in self.lot_el:
            self.assertEqual(node.next, None)
            self.assertEqual(node.prev, None)

    def test_len_regression(self):
        self.assertEqual(self.empty_linked_list.len(), 0)
        self.assertEqual(self.one_el_linked_list.len(), 1)
        self.assertEqual(self.lot_el_linked_list.len(), len(self.lot_el))

    def test_insert_regression(self):
        n = Node(1234)
        self.empty_linked_list.insert(None, n)
        self.assertEqual(self.empty_linked_list.head, n)
        self.assertEqual(self.empty_linked_list.tail, n)
        self.assertEqual(n.next, None)
        self.assertEqual(n.prev, None)

        n = Node(1234)
        self.one_el_linked_list.insert(None, n)
        self.assertEqual(self.one_el_linked_list.head, self.one_el)
        self.assertEqual(self.one_el_linked_list.tail, n)
        self.assertEqual(n.next, None)
        self.assertEqual(n.prev, self.one_el)
        self.assertEqual(self.one_el.prev, None)
        self.assertEqual(self.one_el.next, n)

        n1 = Node(1234)
        n2 = Node(1234)
        n3 = Node(1234)
        self.lot_el_linked_list.insert(self.lot_el[0], n1)
        self.lot_el_linked_list.insert(self.lot_el[13], n2)
        self.lot_el_linked_list.insert(self.lot_el[999], n3)
        self.lot_el = (
            self.lot_el[:1] + [n1] + self.lot_el[1:14] + [n2] + self.lot_el[14:] + [n3]
        )
        self.assertEqual(self.lot_el_linked_list.head, self.lot_el[0])
        self.assertEqual(self.lot_el_linked_list.tail, n3)
        for i, node in enumerate(self.lot_el):
            if i == 0:
                self.assertEqual(node.next, self.lot_el[i + 1])
                self.assertEqual(node.prev, None)
                continue
            if i == len(self.lot_el) - 1:
                self.assertEqual(node.next, None)
                self.assertEqual(node.prev, self.lot_el[i - 1])
                continue
            self.assertEqual(node.next, self.lot_el[i + 1])
            self.assertEqual(node.prev, self.lot_el[i - 1])

    def test_border(self):
        pass

    def tearDown(self):
        self.empty_linked_list = None
        self.one_el_linked_list = None
        self.lot_el_linked_list = None


if __name__ == "__main__":
    unittest.main()
