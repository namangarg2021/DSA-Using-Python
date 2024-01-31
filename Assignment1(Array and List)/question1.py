from array import *

arr=array('i',[26,78,1,34,6,7])

print("Original Array is:")
for x in arr:
    print(x,end=' ')

arr=sorted(arr)

print("\nSorted Array is:")
for x in arr:
    print(x,end=' ')
