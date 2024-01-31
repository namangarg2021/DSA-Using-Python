class CDLLIterator:
    def __init__(self, start=None):
        if start is not None:
            self.start = start
            self.current = start
            self.flag = True
        else:
            self.start = start
            self.current = start
            self.flag = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.flag and self.current == self.start:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        self.flag = False
        return data
