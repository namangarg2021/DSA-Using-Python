from CDLLIterator import *
from Node import *


class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(None, data, None)
        if self.start is None:
            n.prev = n
            n.next = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.start is None:
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n

    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                if temp.data == data:
                    return temp
                temp = temp.next
            if temp.data == data:
                return temp
            print(data, " not present")
        else:
            print("List is Empty!!!")

    def insert_after(self, temp, data):
        if temp is not None:
            if temp == self.start:
                n = Node(self.start, data, self.start.next)
                self.start.next.prev = n
                self.start.next = n
            elif temp == self.start.prev:
                self.insert_at_last(data)
            else:
                n = Node(temp, data, temp.next)
                temp.next.prev = n
                temp.next = n

    def traverse(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != self.start:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data, end=' ')
            print("\n")
        else:
            print("List is Empty!!!")

    def delete_first(self):
        if self.is_empty():
            print("List is Empty!!!")
        elif self.start == self.start.next:
            self.start = None
        else:
            self.start.next.prev = self.start.prev
            self.start.prev.next = self.start.next
            self.start = self.start.next

    def delete_last(self):
        if self.is_empty():
            print("List is Empty!!!")
        elif self.start == self.start.next:
            self.start = None
        else:
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if self.is_empty():
            print("List is empty!!!")
            return
        if self.start.data == data:
            self.delete_first()
        else:
            temp = self.start
            while temp.next != self.start:
                if temp.data == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return
                temp = temp.next
            if temp.data == data:
                self.delete_last()

    def __iter__(self):
        return CDLLIterator(self.start)


cdll = CDLL()
cdll.insert_at_start(10)
cdll.insert_at_last(20)
cdll.insert_at_last(30)
cdll.insert_at_last(40)
cdll.insert_after(cdll.search(30), 35)

# Using Iterator
for x in cdll:
    print(x, end=' ')
