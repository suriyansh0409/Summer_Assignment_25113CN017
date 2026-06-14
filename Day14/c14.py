#program to Second largest element.
arr=[10,20,30,40,50,60,70,80,90]
largest=max(arr)
# print(largest)
arr.remove(largest)
secondlargest=max(arr)
print("Second largest element  of the list is ", secondlargest)