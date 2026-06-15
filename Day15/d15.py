# program to Move zeroes to end.
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j] = arr[i]
        j += 1

while j < len(arr):
    arr[j] = 0
    j += 1

print("Array after moving zeroes:", arr)