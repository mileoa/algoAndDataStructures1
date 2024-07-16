from Stack import Stack


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class NodeDummy(Node):
    def __init__(self, v):
        super().__init__(v)


class LinkedList2:
    def __init__(self):
        self.dummy = NodeDummy(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.size = 0

    @property
    def head(self):
        if isinstance(self.dummy.next, NodeDummy):
            return None
        return self.dummy.next

    @property
    def tail(self):
        if isinstance(self.dummy.prev, NodeDummy):
            return None
        return self.dummy.prev

    def delete(self, val, all=False):
        node = self.dummy.next
        while not isinstance(node, NodeDummy):
            if node.value != val:
                node = node.next
                continue
            node.prev.next = node.next
            node.next.prev = node.prev
            current = node
            node = node.next
            current.next = None
            current.prev = None
            self.size -= 1
            if not all:
                break

    def find(self, val):
        node = self.dummy.next
        while not isinstance(node, NodeDummy):
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.dummy.next
        while not isinstance(node, NodeDummy):
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def clean(self):
        node = self.dummy.next
        while not isinstance(node, NodeDummy):
            next_node = node.next
            self.delete(node.value)
            node = next_node

    def len(self):
        return self.size

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.prev = self.dummy.prev
            newNode.next = self.dummy
            self.dummy.prev.next = newNode
            self.dummy.prev = newNode
        else:
            newNode.prev = afterNode
            newNode.next = afterNode.next
            afterNode.next.prev = newNode
            afterNode.next = newNode
        self.size += 1

    def add_in_tail(self, item):
        self.insert(self.dummy.prev, item)

    def add_in_head(self, newNode):
        self.insert(self.dummy, newNode)

    def delete_tail(self):
        if isinstance(self.dummy.prev, NodeDummy):
            return None
        self.dummy.prev.prev.next = self.dummy.prev.next
        current = self.dummy.prev
        self.dummy.prev = self.dummy.prev.prev
        current.next = None
        current.prev = None
        self.size -= 1

    def delete_head(self):
        if isinstance(self.dummy.next, NodeDummy):
            return None
        self.delete(self.head.value)


class StackReversed(Stack):
    def __init__(self):
        super().__init__()

    def pop(self):
        if self.stack.len() == 0:
            return None
        result = self.stack.head.value
        self.stack.delete_head()
        return result

    def push(self, value):
        self.stack.add_in_head(Node(value))

    def peek(self):
        if self.stack.len() == 0:
            return None
        return self.stack.head.value
