from DLL import *


class Deque(DLL):

    def is_empty(self):
        return super().is_empty()

    def insert_front(self, data):
        self.insert_at_start(data)

    def insert_rear(self, data):
        self.insert_at_last(data)

    def delete_front(self):
        if not self.is_empty():
            return self.delete_first()
        else:
            print("Deque UnderFlow")

    def delete_rear(self):
        if not self.is_empty():
            return self.delete_last()
        else:
            print("Deque UnderFlow")

    def get_front(self):
        if not self.is_empty():
            return self.getFirst()
        else:
            print("Deque UnderFlow")

    def get_rear(self):
        if not self.is_empty():
            return self.getLast()
        else:
            print("Deque UnderFlow")

    def size(self):
        return len(self)


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
