#Program to Linear search. 
arr=[10,20,30,40,50,60,70,80,90]
target=int(input("enter the number to search (10/20/30/40/50/60/70/80/90):"))
for i in range (len(arr)):
    if arr[i]==target:
        print("The index of the number is:",i)
        break
else:
    print("Number not found!")
