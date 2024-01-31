from DLL import *


class Deque:
    def __init__(self):
        self.start = DLL()

    def is_empty(self):
        return self.start.is_empty()

    def insert_front(self, data):
        self.start.insert_at_start(data)

    def insert_rear(self, data):
        self.start.insert_at_last(data)

    def delete_front(self):
        if not self.is_empty():
            return self.start.delete_first()
        else:
            print("Deque UnderFlow")

    def delete_rear(self):
        if not self.is_empty():
            return self.start.delete_last()
        else:
            print("Deque UnderFlow")

    def get_front(self):
        if not self.is_empty():
            return self.start.getFirst()
        else:
            print("Deque UnderFlow")

    def get_rear(self):
        if not self.is_empty():
            return self.start.getLast()
        else:
            print("Deque UnderFlow")

    def size(self):
        return len(self.start)


q1 = Deque()
q1.insert_front(10)
q1.insert_front(20)
q1.insert_rear(30)
q1.insert_rear(40)
print(q1.get_front(), q1.get_rear())

q1.delete_front()
print(q1.get_front(), q1.get_rear())

q1.delete_rear()
print(q1.get_front(), q1.get_rear())

q1.delete_front()
print(q1.get_front(), q1.get_rear())

q1.delete_rear()
print(q1.get_front(), q1.get_rear())
