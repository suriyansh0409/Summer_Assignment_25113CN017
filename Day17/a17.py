#Program to Merge arrays.
from array import *
arr1=array('i',[2,4,8,9,7,6,10])
arr2=array('i',[1,4,5,6,7,2,14,15])

arr1.extend(arr2)
print("Merged array :", arr1)
