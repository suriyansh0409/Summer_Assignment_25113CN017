#Program to Find LCM of two numbers.
x=int(input("Enetr any number:")) # x=first number.
y=int(input("Enetr any number:")) # x=Second number.

#Using GCD: (a*b)/(gcd(a,b))
if x>y:
    small=y
else:
    small=x
for i in range(1,small+1):
    if x%i==0 and y%i==0 :
        gcd=i
lcm =(x*y)//(gcd)
print("Lcm:",lcm)