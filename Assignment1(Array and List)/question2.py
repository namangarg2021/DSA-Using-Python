list=[10,25.9,True,"Naman",False,30,56.0,"Garg"]

print("Original List is:")
for x in list:
    print(x,end=" ")

list =  [x for x in list if type(x) == int]

print("\nAfter removing all non integer values.List is:")
for x in list:
    print(x,end=" ")