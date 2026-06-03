#Program to Find GCD of two numbers
x=int(input("Enetr any number:")) # x=first number.
y=int(input("Enetr any number:")) # x=Second number.
if x>y:
    small=y
else:
    small=x
for i in range(1,small+1):
    if (x%i==0) and (y%i==0):
        gcd=i

print("GCD:",gcd)