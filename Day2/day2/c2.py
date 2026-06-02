#  Program to Find product of digit
product=int(input("enter the value:"))

pro=1
while product>0:
    digit=product%10
    pro=pro*digit
    product=product//10

print("The product of the digits of the given number is:", pro)
