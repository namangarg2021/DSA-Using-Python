class Person:
    def __init__(self,name="Naman",age=22):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

p1=Person()
p1.show()
p2=Person("Ajay",23)
p2.show()