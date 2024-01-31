class Queue:
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue UnderFlow!!!")

    def get_front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Queue UnderFlow!!!")

    def get_rear(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            raise IndexError("Queue UnderFlow!!!")

    def size(self):
        return len(self.queue)


q1 = Queue()
try:
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.enqueue(40)
    q1.enqueue(50)
    print("Front=", q1.get_front())
    print("Rear=", q1.get_rear())
    print(q1.dequeue())
    print("Queue has now", q1.size(), "elements")

except IndexError as ex:
    print(ex.args[0])
