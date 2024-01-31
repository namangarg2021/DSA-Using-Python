class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_Node = Node(data, self.start)
        self.start = new_Node

    def insert_at_last(self, data):
        if self.start is None:
            self.start = Node(data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

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

        print('\n')

    def delete_first(self):
        if self.start is None:
            print("\n List is Empty")
            return
        self.start = self.start.next

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
        else:
            prev.next = temp.next
