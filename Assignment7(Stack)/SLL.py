class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def delete_first(self):
        if self.start is None:
            return
        data = self.start.data
        self.start = self.start.next
        return data
