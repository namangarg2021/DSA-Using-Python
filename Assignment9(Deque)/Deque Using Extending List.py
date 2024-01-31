class Deque(list):

    def is_empty(self):
        return len(self) == 0

    def insert_front(self, data):
        self.insert(0, data)

    def insert_rear(self, data):
        self.append(data)

    def delete_front(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            print("Deque UnderFlow")

    def delete_rear(self):
        if not self.is_empty():
            return self.pop()
        else:
            print("Deque UnderFlow")

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            print("Deque UnderFlow")

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            print("Deque UnderFlow")

    def size(self):
        return len(self)

    def traverse(self):
        for x in self:
            print(x, " ")
        print()


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
