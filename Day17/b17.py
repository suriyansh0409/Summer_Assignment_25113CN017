#  program to Union of array
from array import *
arr1=array('i',[1,5,4,7,8,9])
arr2=array('i',[2,5,4,20,54,9])

union=[]
for x in arr1:
    if x  not in union:
        union.append(x)
for x in arr2:
    if x not in union:
        union.append(x)

print("Union :", union )

