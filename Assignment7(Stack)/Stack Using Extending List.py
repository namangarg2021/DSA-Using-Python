class Stack(list):
    def is_empty(self):
        return len(self) == 0

    def push(self, data=None):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty!!!")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty!!!")

    def size(self):
        return len(self)

    def insert(self, index, data):
        # raise AttributeError("No Attribute insert in Stack")
        print("insert method is not allowed!")


s1 = Stack()
s1.insert(0, 10)
s1.push(10)
s1.push(20)
s1.push(30)

print('Top element is', s1.peek())
print('Popped element is', s1.pop())
print('Top element is', s1.peek())
