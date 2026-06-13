#Program to Write function for Armstrong
def armstrong(n):
    power =len(str(n))
    temp=n
    total=0
    while n>0:
        digit=n%10
        total= total + digit**power
        n=n//10
    if temp==total:
        print("It is an Armstrong number ")
    else:
        print("not an armstong number ")
n = int (input("Enter any number :"))
armstrong (n)

