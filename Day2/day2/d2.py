#  program to Check whether a number is palindrome
x=int(input("Enter any number:"))
original=x
reverse=0

while (x>0):
    digit=x%10
    reverse= reverse*10 + digit
    x=x//10
if (reverse == original):
    print(" It is a palindrome number")
else:
    print("It is not a palindrome number")