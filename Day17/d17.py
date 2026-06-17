# program to Find common elements.

from array import *
arr1=array('i',[2,6,8,10])
arr2=array('i',[2,10,3,7])

inter=[]
for x in arr1:
    if x in arr2 and x not in inter:
        inter.append(x)
    

print(inter)