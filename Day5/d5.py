#Program to Find largest prime factor
x=int(input("enter any number:"))

largest=0
for i in range (2,x+1):
    if (x%i==0):
        prime=True

        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            largest=i
print("The largest prime factor is:",largest)

