class Deque:
    def __init__(self):
        self.start = []

    def is_empty(self):
        return len(self.start) == 0

    def insert_front(self, data):
        self.start.insert(0, data)

    def insert_rear(self, data):
        self.start.append(data)

    def delete_front(self):
        if not self.is_empty():
            return self.start.pop(0)
        else:
            print("Deque UnderFlow")

    def delete_rear(self):
        if not self.is_empty():
            return self.start.pop()
        else:
            print("Deque UnderFlow")

    def get_front(self):
        if not self.is_empty():
            return self.start[0]
        else:
            print("Deque UnderFlow")

    def get_rear(self):
        if not self.is_empty():
            return self.start[-1]
        else:
            print("Deque UnderFlow")

    def size(self):
        return len(self.start)

    def traverse(self):
        for x in self.start:
            print(x, " ")
        print()


q1 = Deque()
q1.insert_front(10)
q1.insert_front(20)
q1.insert_rear(30)
q1.insert_rear(40)
print(q1.get_front(), q1.get_rear())
q1.traverse()

q1.delete_front()
q1.delete_rear()
q1.delete_front()
q1.traverse()
