# Program to Count digits in a number. 

num = input("Enter a number: ")

if num[0] == '-':
    print("Number of digits =", len(num) - 1)
else:
    print("Number of digits =", len(num))