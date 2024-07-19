class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.item_count = 0

    def hash_fun(self, value):
        a = 7
        b = 11
        p = 7127
        x = 0
        for char in value:
            x += ord(char)
        return ((a * x + b) % p) % self.size

    def seek_slot(self, value):
        if self.item_count == self.size:
            return None

        hash = self.hash_fun(value)
        index = hash
        current_step = self.step

        while self.slots[index] is not None:
            index = (hash + current_step) % self.size
            current_step += self.step
            if index == hash:
                return None

        return index

    def put(self, value):
        index_to_insert = self.seek_slot(value)

        if index_to_insert is None:
            return None

        self.slots[index_to_insert] = value
        self.item_count += 1
        return index_to_insert

    def find(self, value):
        hash = self.hash_fun(value)
        index = hash
        current_step = self.step

        while self.slots[index] is not None:
            if self.slots[index] == value:
                return index
            index = (hash + current_step) % self.size
            current_step += self.step
            if index == hash:
                return None
        return None
