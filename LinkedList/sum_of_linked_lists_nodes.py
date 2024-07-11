class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        previous = None
        while node is not None:
            if node.value == val:
                if previous is not None:
                    previous.next = node.next
                    if node.next is None:
                        self.tail = previous
                else:
                    self.head = self.head.next
                    if self.head is None:
                        self.tail = None
                current = node
                node = node.next
                current.next = None
                if not all:
                    break
                continue

            previous = node
            node = node.next

    def clean(self):
        node = self.head
        while self.head is not None:
            self.head = node.next
            node.next = None
            node = self.head
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next
        return result

    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.tail = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            next_node = afterNode.next
            afterNode.next = newNode
            newNode.next = next_node
            if afterNode is self.tail:
                self.tail = newNode


def sum_of_linked_lists_nodes(linked_list1, linked_list2):
    if linked_list1.len() != linked_list2.len():
        return None

    result = LinkedList()
    node1 = linked_list1.head
    node2 = linked_list2.head

    while node1 is not None:
        result.add_in_tail(Node(node1.value + node2.value))
        node1 = node1.next
        node2 = node2.next

    return result
