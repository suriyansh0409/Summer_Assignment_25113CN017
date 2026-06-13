#Program to Write function for Fibonacci.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        a, b = b, a+b
    return a

n = int (input("Enter any number :"))    
print("Fibonacci of number is :",fibonacci (n))