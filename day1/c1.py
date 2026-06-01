# Program to print the factorial of a given number 
def factorial(n):
    factorial = 1
    for i in range (1,n+1):
        factorial = factorial*i

    print("Factorial is :"  ,factorial) 

x=(int(input("enter the number :")))
factorial(x)