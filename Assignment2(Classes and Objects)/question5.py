import math
class Team:
    def __init__(self):
        self.list=[]
    def addMember(self,member=None):
        self.list.append(member)
    def show(self):
        print("Members of the list are:")
        for x in self.list:
            print(x)

t1=Team()
t1.addMember("Naman")
t1.addMember("Ajay")
t1.addMember("Amit")
t1.show()

t2=Team()
t2.addMember("Arun")
t2.addMember("Priyam")
t2.addMember("Vijay")
t2.show()