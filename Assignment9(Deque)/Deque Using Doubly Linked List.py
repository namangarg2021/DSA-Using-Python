class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_front(self, data):
        n = Node(None, data, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(self.rear, data, None)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def delete_front(self):
        if self.is_empty():
            print("Dequeue Underflow!!!")
            return
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1

    def delete_rear(self):
        if self.is_empty():
            print("Dequeue Underflow!!!")
            return
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            print("Dequeue Underflow!!!")
        else:
            return self.front.data

    def get_rear(self):
        if self.is_empty():
            print("Dequeue Underflow!!!")
        else:
            return self.rear.data

    def size(self):
        return self.item_count


q1 = Deque()
q1.insert_front(10)
q1.insert_front(20)
q1.insert_rear(30)
q1.insert_rear(40)
print(q1.get_front(), q1.get_rear())
print(q1.item_count)
q1.delete_front()
print(q1.get_front(), q1.get_rear())

q1.delete_rear()
print(q1.get_front(), q1.get_rear())

q1.delete_front()
print(q1.get_front(), q1.get_rear())
