class Queue:
    def __init__(self):
        self.queue = []
        self.begin = -1
        self.end = -1

    def enqueue(self, item):
        self.queue.append(item)
        self.end += 1

    def dequeue(self):
        if self.begin == self.end:
            return None
        self.begin += 1
        return self.queue[self.begin]

    def size(self):
        return self.end - self.begin
