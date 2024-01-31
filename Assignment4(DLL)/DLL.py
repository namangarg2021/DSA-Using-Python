from DLLIterator import *
from Node import *


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        new_Node = Node(None, data, self.start)
        if self.start is not None:
            self.start.prev = new_Node
        self.start = new_Node

    def insert_at_last(self, data):
        if self.start is None:
            self.start = Node(None, data, None)
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            new_Node = Node(temp, data, None)
            temp.next = new_Node

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            temp.next = n
            if n.next is not None:
                n.next.prev = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                print("\nValue is present")
                return temp
            temp = temp.next
        print("\nValue is not present")
        return None

    def traverse(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print("\n")

    def delete_first(self):
        if self.start is None:
            print("\n List is Empty")
            return
        if self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next
            self.start.prev = None

    def delete_last(self):
        if self.start is None:
            print("\n List is Empty")
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, item):
        if self.start is None:
            print("\n List is Empty")
            return
        temp = self.start
        prev = self.start
        while temp is not None:
            if temp.data == item:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print("Item not found")
        elif temp == prev:
            self.start = temp.next
            self.start.prev = None
        else:
            prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev

    def __iter__(self):
        return DLLIterator(self.start)


obj = DLL()
for x in obj:
    print(x, end=' ')
obj.insert_at_start(10)
obj.traverse()
obj.insert_at_start(20)
obj.traverse()
obj.insert_at_last(30)
obj.traverse()

obj.delete_first()
obj.traverse()
obj.delete_last()
obj.traverse()
obj.delete_item(60)
obj.traverse()
obj.delete_last()
obj.traverse()

# Using Iterator
for x in obj:
    print(x, end=' ')
