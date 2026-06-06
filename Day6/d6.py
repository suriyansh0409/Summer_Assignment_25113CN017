# Pogram to Find x^n without pow().
n=int(input("enter the number:")) # N= the number
p=int(input("enter the power:"))  # P= The power

result=1
for i in range(1,p+1):
    result=result*n

print(result)
