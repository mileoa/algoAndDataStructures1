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
        while node is not None:
            if node.value == val and node is self.head:
                if self.head is self.tail:
                    node.next = None
                    self.tail = None
                    self.head = None
                    break
                current = self.head
                self.head = node.next
                node = node.next
                current.next = None
                if not all:
                    break
                continue
            if node.next is None:
                break
            if node.next.value == val:
                if node.next is self.tail:
                    node.next = None
                    self.tail = node
                    break
                next_node = node.next.next
                node.next = None
                node.next = next_node
                if not all:
                    break
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
