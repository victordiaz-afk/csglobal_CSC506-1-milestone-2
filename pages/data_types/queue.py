
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)   # add to rear

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("queue is empty")
        return self.data.pop(0)  # remove from front

    def front(self):
        if self.isEmpty():
            raise IndexError("queue is empty")
        return self.data[0]      # view front item

    def isEmpty(self):
        return len(self.data) == 0
