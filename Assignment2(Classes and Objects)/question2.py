import math
class Circle:
    def __init__(self):
        pass
    def set_radius(self,radius):
        self.radius=radius
    def get_radius(self):
        return self.radius
    def getArea(self):
        return math.pi*math.pow(self.radius,2)
    def getCircumference(self):
        return 2*math.pi*self.radius
c1=Circle()
c1.set_radius(3)
area=c1.getArea()
circum=c1.getCircumference()

print("Area of Circle is",area)
print("\nCircumferenc of Circle is",circum)