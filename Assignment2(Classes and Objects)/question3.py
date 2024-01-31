import math
class Rectangle:
    def __init__(self):
        pass
    def set_dimensions(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def show_dimensions(self):
        print("Length is",self.length)
        print("Breadth is",self.breadth)
    def getArea(self):
        return self.length*self.breadth

r1=Rectangle()
r1.set_dimensions(10,20)
r1.show_dimensions()
area=r1.getArea()
print("Area of Rectange is",area)
