import unittest
import random

from sum_of_linked_lists_nodes import sum_of_linked_lists_nodes, LinkedList, Node


class SumOfLinkedListsNodesTests(unittest.TestCase):

    def test_regression(self):
        list1 = LinkedList()
        list2 = LinkedList()

        for i in range(1, 11):
            list1.add_in_tail(Node(i))

        for i in range(10):
            list2.add_in_tail(Node(i))

        lists_sum = sum_of_linked_lists_nodes(list1, list2)
        self.assertEqual(lists_sum.head.value, 1)
        self.assertEqual(lists_sum.tail.value, 19)
        node = lists_sum.head
        for i in range(lists_sum.len()):
            self.assertEqual(node.value, i + i + 1)
            node = node.next

        for i in range(11, 12):
            list1.add_in_tail(Node(i))

        lists_sum = sum_of_linked_lists_nodes(list1, list2)
        self.assertEqual(lists_sum, None)

        for i in range(10, 12):
            list2.add_in_tail(Node(i))

        lists_sum = sum_of_linked_lists_nodes(list1, list2)
        self.assertEqual(lists_sum, None)

    def test_empty(self):
        list1 = LinkedList()
        list2 = LinkedList()

        lists_sum = sum_of_linked_lists_nodes(list1, list2)
        self.assertEqual(lists_sum.head, None)
        self.assertEqual(lists_sum.tail, None)

    def test_border(self):
        list1 = LinkedList()
        list2 = LinkedList()

        list1.add_in_tail(Node(1))
        list2.add_in_tail(Node(2))

        lists_sum = sum_of_linked_lists_nodes(list1, list2)

        self.assertEqual(lists_sum.head.next, None)
        self.assertEqual(lists_sum.tail.next, None)
        self.assertEqual(lists_sum.head.value, 3)
        self.assertEqual(lists_sum.tail.value, 3)


if __name__ == "__main__":
    unittest.main()
