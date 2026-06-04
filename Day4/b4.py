#Program to Find nth Fibonacci term
n=int(input("Enter any number:"))
a=0 #PERVIOUS TERM
b=1 #CURRENT TERM

if n==1:
    print("fibonacci terms",a)
elif n==2:
    print("fibonacci terms",b)
else:
     for i in range(3, n+1):
        c=a+b #NEXT TERM
        a=b
        b=c
print("fibonacci terms:",b) #printed B because b is the current term.
