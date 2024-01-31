n=int(input("Enter the value of n:"))
list=[0,1]
count=2
while count<n:
    l=len(list)
    list.append(list[l-1]+list[l-2])
    count+=1
print("First",n,"fibonacci numbers are:")

for x in list:
    print(x,end=' ')