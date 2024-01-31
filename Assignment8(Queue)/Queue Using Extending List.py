class Queue(list):

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            print("Queue UnderFlow!!!")

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            print("Queue UnderFlow!!!")

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            print("Queue UnderFlow!!!")

    def size(self):
        return len(self)


q1 = Queue()
print(q1.is_empty())
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
print(q1.dequeue())
print(q1.size())
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
print(q1.is_empty())
print(q1.dequeue())
