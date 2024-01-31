class Stack:
    def __init__(self):
        self.s = []

    def is_empty(self):
        return len(self.s) == 0

    def push(self, data=None):
        self.s.append(data)

    def pop(self):
        if not self.is_empty():
            return self.s.pop()
        else:
            raise IndexError("Stack is empty!!!")

    def peek(self):
        if not self.is_empty():
            return self.s[-1]
        else:
            raise IndexError("Stack is empty!!!")

    def size(self):
        return len(self.s)


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print('Top element is', s1.peek())
print('Removed element is', s1.pop())
print('Top element is', s1.peek())
