
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)   # add to top (end of list)

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.data.pop()   # remove from top

    def peek(self):
        if self.isEmpty():
            raise IndexError("stack is empty")
        return self.data[-1]     # return top item

    def isEmpty(self):
        return len(self.data) == 0

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top:", s.peek())   # 30
print("Pop:", s.pop())    # 30
print("Is Empty:", s.isEmpty())  # False
