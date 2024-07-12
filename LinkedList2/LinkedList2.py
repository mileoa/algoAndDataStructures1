class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
            if node.value == val:
                if node.prev is not None:
                    node.prev.next = node.next
                    if node.next is None:
                        self.tail = node.prev
                    else:
                        node.next.prev = node.prev
                else:
                    self.head = self.head.next
                    if node.next is not None:
                        node.next.prev = None
                    if self.head is None:
                        self.tail = None
                current = node
                node = node.next
                current.next = None
                current.prev = None
                if not all:
                    break
                continue

            node = node.next

    def clean(self):
        node = self.head
        while self.head is not None:
            self.head = node.next
            node.next = None
            node.prev = None
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
                self.head = newNode
                self.tail = newNode
            else:
                newNode.prev = self.tail
                newNode.prev.next = newNode
                newNode.next = None
                self.tail = newNode
        else:
            if afterNode.next is not None:
                afterNode.next.prev = newNode
            newNode.next = afterNode.next
            newNode.prev = afterNode
            afterNode.next = newNode
            if afterNode is self.tail:
                self.tail = newNode

    def add_in_head(self, newNode):
        newNode.next = self.head
        if newNode.next is not None:
            newNode.next.prev = newNode
        newNode.prev = None
        if self.head is None:
            self.tail = newNode
        self.head = newNode
