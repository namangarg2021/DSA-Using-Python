from Node import *
from CLLIterator import *


class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
        else:
            new_node.next = self.last.next
        self.last.next = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def search(self, data):
        if self.last is None:
            print("List is Empty!!!")
            return None
        temp = self.last.next
        while True:
            if temp.data == data:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data, temp.next)
            if temp == self.last:
                new_node.next  = self.last.next
                self.last.next = new_node
                self.last = new_node
            else:
                temp.next = new_node

    def traverse(self):
        if self.last is None:
            print("List is Empty!!!")
            return
        temp = self.last.next
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.last.next:
                break
        print(("\n"))

    def delete_first(self):
        if self.last is None:
            print("List is Empty!!!")
            return
        if self.last == self.last.next:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def delete_last(self):
        if self.last is None:
            print("List is Empty!!!")
            return
        if self.last == self.last.next:
            self.last = None
        else:
            second_last = self.last.next
            while second_last.next != self.last:
                second_last = second_last.next
            second_last.next = self.last.next
            self.last = second_last

    def delete_item(self, data):
        if self.last is None:
            print("List is Empty!!!")
            return
        if self.last == self.last.next and self.last.data == data:
            self.last = None
        else:
            temp = self.last.next
            prev = temp
            while True:
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next
                if temp == self.last.next:
                    break
            if temp != self.last.next or prev == temp:
                if temp == self.last.next:
                    self.last.next = self.last.next.next
                elif temp == self.last:
                    prev.next = self.last.next
                    self.last = prev
                else:
                    prev.next = temp.next

    def __iter__(self):
        return CLLIterator(self.last)


obj = CLL()
obj.insert_at_start(10)
obj.insert_at_start(20)
obj.insert_at_last(30)
obj.insert_at_last(40)

obj.insert_after(obj.search(10), 50)
# obj.insert_after(obj.search(40), 28)
# obj.insert_after(obj.search(45), 38)
# obj.insert_after(obj.search(36), 48)
# obj.traverse()
# obj.delete_last()
# obj.delete_first()
# obj.delete_last()
# obj.delete_first()
# obj.delete_last()
# obj.delete_first()

obj.traverse()
#
# obj.delete_item(25)
# obj.delete_item(20)
# obj.delete_item(10)

# Using Iterator
for x in obj:
    print(x, end=' ')
