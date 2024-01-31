from SLL import *


class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self, data=None):
        self.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.item_count -= 1
            return self.delete_first()
        else:
            raise IndexError("Stack UnderFlow")

    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Stack UnderFlow")

    def size(self):
        return self.item_count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
# s1.push(40)

# print("Is stack empty ?", s1.is_empty())
# print('Removed element is', s1.pop())
print('Top element is', s1.peek())
print('Removed element is', s1.pop())
# print('Removed element is', s1.pop())
print('Top element is', s1.peek())
# print('Removed element is', s1.pop())
# print("Is stack empty ?", s1.is_empty())
