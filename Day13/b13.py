# program to Find sum and average of array.
# Program to Find Sum and Average of Array

n = int(input("Enter the number of elements: "))

arr = []
sum = 0

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

for i in arr:
    sum = sum + i

avg = sum / len(arr)

print("Array elements are:", arr)
print("Sum of elements =", sum)
print("Average of elements =", avg)