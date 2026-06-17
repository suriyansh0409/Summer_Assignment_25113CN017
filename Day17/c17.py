# program to Intersection of arrays.
from array import *

arr1 = array('i', [1, 2, 2, 3])
arr2 = array('i', [2, 2 ,3,4])

intersection = []
temp = list(arr2)

for x in arr1:
    if x in temp:
        intersection.append(x)
        temp.remove(x)

print("Intersection:", intersection)