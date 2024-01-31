from SLL import *


class Queue:
    def __init__(self):
        self.queue = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.queue.is_empty()

    def enqueue(self, data):
        self.queue.insert_at_last(data)
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            self.queue.delete_first()
            self.item_count -= 1
        else:
            print("Queue UnderFlow!!!")

    def get_front(self):
        if not self.is_empty():
            return self.queue.start.data
        else:
            print("Queue UnderFlow!!!")

    def get_rear(self):
        if not self.is_empty():
            temp = self.queue.start
            while temp.next is not None:
                temp = temp.next
            return temp.data
        else:
            print("Queue UnderFlow!!!")

    def size(self):
        return self.item_count


q1 = Queue()
print(q1.is_empty())
q1.enqueue(10)
print(q1.dequeue())
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
print(q1.get_front())
print(q1.get_rear())
