import math
class Book:
    def __init__(self,bookid=None,title=None,price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
    def show(self):
        print("Book id:",self.bookid)
        print("Book title:",self.title)
        print("Book price:",self.price)

b1=Book(101,"Let Us C",500)
b1.show()

b2=Book(102,"Java Is Love",1000)
b2.show()


b3=Book(103,"Learning Data Structures In Python",300)
b3.show()

