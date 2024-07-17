import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for j in range(self.count, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1
        if self.count < 0.5 * self.capacity:
            new_capacity = max(int(self.capacity / 1.5), 16)
            self.resize(new_capacity)

    def len(self):
        return self.count


class Deque:
    def __init__(self):
        self.deque = DynArray()

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.deque.len() == 0:
            return None
        result = self.deque[0]
        self.deque.delete(0)
        return result

    def removeTail(self):
        if self.deque.len() == 0:
            return None
        result = self.deque[self.deque.len() - 1]
        self.deque.delete(self.deque.len() - 1)
        return result

    def size(self):
        return self.deque.len()


def is_palindrome(string):
    d = Deque()
    for char in string:
        d.addTail(char)

    el1 = d.removeFront()
    el2 = d.removeTail()
    while el1 is not None and el2 is not None:
        if el1 != el2:
            return False
        el1 = d.removeFront()
        el2 = d.removeTail()
    return True
