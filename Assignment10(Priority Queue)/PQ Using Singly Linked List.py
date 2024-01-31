class Node:
    def __init__(self, data=None, priority=None, next=None):
        self.data = data
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def push(self, data, priority):
        n = Node(data, priority)
        if self.is_empty() or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            prev = self.start
            while temp is not None:
                if temp.priority > priority:
                    break
                prev = temp
                temp = temp.next
            prev.next = n
            n.next = temp
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            print("Priority Queue is empty!!!")
        else:
            data = self.start.data
            self.start = self.start.next
            self.item_count -= 1
            return data

    def is_empty(self):
        return self.start is None

    def size(self):
        return self.item_count


p1 = PriorityQueue()
p1.push(10, 2)
p1.push(20, 2)
p1.push(30, 3)
p1.push(40, 1)
p1.push(50, 3)

print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())
print(p1.pop())

p = PriorityQueue()
p.push("Amit", 4)
p.push("Arjun", 7)
p.push("Ashima", 2)
p.push("Agrah", 5)
p.push("Anant", 8)
p.push("Ambika", 1)

while not p.is_empty():
    print(p.pop())
