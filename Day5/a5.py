#Program to Check perfect number.
# Perfect number is the number whose sum of the divisor is equal to the number (excluding the number itself)
x=int(input("Enter any number:"))
divisor=0
for i in range (1,x):
    if (x%i==0):
        divisor=divisor+i
if (divisor==x):
    print("it is Perfect number!!")
else:
    print("Not a Perfect number!!")
