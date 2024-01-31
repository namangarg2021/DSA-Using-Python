class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        if self.is_empty():
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue UnderFlow!!!")
        elif self.front == self.rear:
            data = self.front.data
            self.item_count -= 1
            self.front = None
            self.rear = None
            return data
        else:
            data = self.front.data
            self.front = self.front.next
            self.item_count -= 1
            return data

    def get_front(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("Queue UnderFlow!!!")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            print("Queue UnderFlow!!!")

    def size(self):
        return self.item_count


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(), q1.get_rear())
q1.dequeue()
print(q1.get_front(), q1.get_rear())
print(q1.size())
print(q1.get_front())
print(q1.get_rear())
print(q1.size())
print(q1.is_empty())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
q1.enqueue(10)
q1.enqueue(20)
print(q1.size())
