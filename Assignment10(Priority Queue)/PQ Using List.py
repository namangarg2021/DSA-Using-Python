class Pair:
    def __init__(self, data=None, priority=None):
        self.data = data
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.list = []

    def push(self, data, priority):
        pair = Pair(data, priority)
        index = 0
        for x in self.list:
            if x.priority > priority:
                break
            index += 1
        self.list.insert(index, pair)

    def pop(self):
        if self.is_empty():
            print("Priority Queue is empty!!!")
        else:
            return self.list.pop(0)

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)


p1 = PriorityQueue()
p1.push(10, 2)
p1.push(20, 6)
p1.push(30, 3)
p1.push(40, 1)
p1.push(50, 4)

# print(p1.pop().data)
# print(p1.pop().data)
# print(p1.pop().data)
# print(p1.pop().data)
# print(p1.pop().data)
# print(p1.pop())

p = PriorityQueue()
p.push("Amit", 4)
p.push("Arjun", 7)
p.push("Ashima", 2)
p.push("Agrah", 5)
p.push("Anant", 8)
p.push("Ambika", 1)

while not p.is_empty():
    print(p.pop().data)
