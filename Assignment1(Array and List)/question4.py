import math

n=int(input("Enter the value of n:"))
list=[]
x=2
count=0
while count<n:
    i=2
    while i<=math.sqrt(x):
        if x%i ==0:
            break
        i+=1
    if i>math.sqrt(x):
        list.append(x)
        count+=1
    x+=1
print("First",n,"prime numbers are:")

for x in list:
    print(x,end=' ')