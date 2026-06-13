#Program to Input and display array.
n=int(input("Enter the number of elements:"))
x=[]
for i in range(n):
    num=(input(f"Enter the element {i+1}:"))
    x.append(num)

print("Array Elements are:")
for i in x:
    print(i, end=" ,")
