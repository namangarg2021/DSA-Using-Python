class CLLIterator:
    def __init__(self,last=None):
        if last is not None:
            self.start=last.next
            self.current=last.next
            self.flag=True
        else:
            self.start = last
            self.current = last
            self.flag = False
    def __iter__(self):
        return self
    def __next__(self):
        if not self.flag and self.current == self.start:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        self.flag=False
        return data

