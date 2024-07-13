class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class NodeDummy(Node):
    def __init__(self, v):
        super().__init__(v)
        self.isDummy = True


class LinkedList2:
    def __init__(self):
        self.dummy = NodeDummy(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    @property
    def head(self):
        if self.dummy.next is self.dummy:
            return None
        return self.dummy.next

    @property
    def tail(self):
        if self.dummy.prev is self.dummy:
            return None
        return self.dummy.prev

    def delete(self, val, all=False):
        node = self.dummy.next
        while node is not self.dummy:
            if node.value != val:
                node = node.next
                continue
            node.prev.next = node.next
            node.next.prev = node.prev
            current = node
            node = node.next
            current.next = None
            current.prev = None
            if not all:
                break

    def find(self, val):
        node = self.dummy.next
        while node is not self.dummy:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.dummy.next
        while node is not self.dummy:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def clean(self):
        node = self.dummy.next
        while node is not self.dummy:
            next_node = node.next
            self.delete(node.value)
            node = next_node

    def len(self):
        result = 0
        node = self.dummy.next
        while node is not self.dummy:
            result += 1
            node = node.next
        return result

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.prev = self.dummy.prev
            newNode.next = self.dummy
            self.dummy.prev.next = newNode
            self.dummy.prev = newNode
            return

        newNode.prev = afterNode
        newNode.next = afterNode.next
        afterNode.next.prev = newNode
        afterNode.next = newNode

    def add_in_tail(self, item):
        self.insert(self.dummy.prev, item)

    def add_in_head(self, newNode):
        self.insert(self.dummy, newNode)
