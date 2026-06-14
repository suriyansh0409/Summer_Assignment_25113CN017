# program to Frequency of an element.
arr=[10,20,10,50,60,20,10,80,50,40,30,20,10]
x = int(input("Enter the element to find frequency: "))
count=0
for i in arr:
    if i==x:
        count=count+1

print("Frequency of ",x," in the list is ",count)
