#program to Rotate array left.
arr = [10, 20, 30, 40, 50]

arr = arr[1:] + arr[:1]

print("Left Rotated Array:", arr)