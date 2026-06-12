#Program to Write function for perfect number.
def perfect(n):
    divisor=0
    for i in range (1,n):
        if n%i==0:
            divisor=divisor+i
    if divisor==n:
        print("It is a perfect number!")

    else :
        print("Not a perfect number !")

n = int (input("Enter any number :"))
perfect(n)