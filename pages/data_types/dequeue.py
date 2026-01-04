
class Deque:
    def __init__(self):
        self.data = []

    def addFront(self, item):
        self.data.insert(0, item)

    def addRear(self, item):
        self.data.append(item)

    def removeFront(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        return self.data.pop(0)

    def removeRear(self):
        if self.isEmpty():
            raise IndexError("deque is empty")
        return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0
    
    def display(self):
        for s in self.data:
            print(s)
        