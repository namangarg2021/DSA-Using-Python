from SLL import *


class Stack:
    def __init__(self):
        self.st = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.st.is_empty()

    def push(self, data=None):
        self.st.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.item_count -= 1
            return self.st.delete_first()
        else:
            raise IndexError("Stack is empty!!!")

    def peek(self):
        if not self.is_empty():
            return self.st.start.data
        else:
            raise IndexError("Stack is empty!!!")

    def size(self):
        return self.item_count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)

print('Top element is', s1.peek())
s1.pop()
print('Top element is', s1.peek())

# print("Is stack empty ?", s1.is_empty())
# print('Popped element is', s1.pop())
# print('Top element is', s1.peek())
# print('Popped element is', s1.pop())
# print('Popped element is', s1.pop())
# print('Top element is', s1.peek())
# print('Popped element is', s1.pop())
# print("Is stack empty ?", s1.is_empty())
