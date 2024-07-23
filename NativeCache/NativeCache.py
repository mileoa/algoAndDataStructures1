class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1
        self.item_count = 0

    def hash_fun(self, key):
        a = 7
        b = 11
        p = 7127
        x = 0
        for char in key:
            x += ord(char)
        return ((a * x + b) % p) % self.size

    def seek_slot(self, key):
        hash = self.hash_fun(key)
        index = hash
        current_step = self.step

        while self.slots[index] is not None:
            if self.slots[index] == key:
                return index
            index = (hash + current_step) % self.size
            current_step += self.step
            if index == hash:
                return None
        return index

    def is_key(self, key):
        supposed_index = self.seek_slot(key)
        if supposed_index is None:
            return False
        return self.slots[supposed_index] == key

    def put(self, key, value):
        index = self.seek_slot(key)
        if index is None:
            return None
        if self.slots[index] is None:
            self.slots[index] = key
            self.item_count += 1
        self.values[index] = value
        return None

    def get(self, key):
        supposed_index = self.seek_slot(key)
        if supposed_index is None:
            return None
        if self.slots[supposed_index] is None:
            return None
        return self.values[supposed_index]


class NativeCache(NativeDictionary):
    def __init__(self, sz):
        super().__init__(sz)
        self.hits = [0] * self.size

    def is_key(self, key):
        supposed_index = self.seek_slot(key)
        if supposed_index is None:
            return False
        self.hits[supposed_index] += 1
        return self.slots[supposed_index] == key

    def remove(self, index):
        self.hits[index] = 0
        self.slots[index] = None
        self.values[index] = None
        self.item_count -= 1

    def find_min_access_index(self):
        min_index = None
        min_acces = None
        for i, el in enumerate(self.hits):
            if min_index is None and el is not None:
                min_index = i
                min_acces = el
                continue
            if el is None:
                continue
            if el < min_acces:
                min_index = i
                min_acces = el
        return min_index

    def put(self, key, value):
        index = self.seek_slot(key)
        if index is None:
            self.remove(self.find_min_access_index())
        index = self.seek_slot(key)
        if self.slots[index] is None:
            self.slots[index] = key
            self.item_count += 1
        self.hits[index] += 1
        self.values[index] = value
        return None

    def get(self, key):
        supposed_index = self.seek_slot(key)
        if supposed_index is None:
            return None
        if self.slots[supposed_index] is None:
            return None
        self.hits[supposed_index] += 1
        return self.values[supposed_index]
