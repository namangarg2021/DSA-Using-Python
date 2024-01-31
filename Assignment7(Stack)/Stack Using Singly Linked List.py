class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data=None):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.start.data
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Stack is empty!!!")

    def peek(self):
        if not self.is_empty():
            return self.start.data
        else:
            raise IndexError("Stack is empty!!!")

    def size(self):
        return self.item_count


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

print("Total elements in the stack:", s1.size())
print("Is stack empty ?", s1.is_empty())
print('Removed element is', s1.pop())
print('Top element is', s1.peek())
print('Removed element is', s1.pop())
print('Removed element is', s1.pop())
print('Top element is', s1.peek())
print('Removed element is', s1.pop())
print("Is stack empty ?", s1.is_empty())
