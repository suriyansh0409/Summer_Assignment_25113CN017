# a program to Reverse array. 
n=int(input("Enter number of elements of the array:"))
arr=[]
for i in range (n):
    x=int(input("Enter the elements:"))
    arr.append(x)
print("original array",arr)
rev=arr[::-1]                  #slicing is being donr here [start:stop:step]
print("Reversed array :",rev)
