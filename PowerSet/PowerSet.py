class PowerSet:

    def __init__(self):
        self.slots = {}

    def size(self):
        return len(self.slots)

    def put(self, value):
        self.slots[value] = None

    def get(self, value):
        return value in self.slots

    def remove(self, value):
        if self.get(value):
            del self.slots[value]
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        for el in set2.slots:
            if el in self.slots:
                result.put(el)
        return result

    def union(self, set2):
        result = PowerSet()

        for i in self.slots:
            if i not in result.slots:
                result.put(i)

        for i in set2.slots:
            if i not in result.slots:
                result.put(i)

        return result

    def difference(self, set2):
        result = PowerSet()

        for i in self.slots:
            if i not in set2.slots:
                result.put(i)

        return result

    def issubset(self, set2):
        for i in set2.slots:
            if i not in self.slots:
                return False
        return True
