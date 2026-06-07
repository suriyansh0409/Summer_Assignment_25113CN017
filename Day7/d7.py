#program to Recursive reverse number.
def reverse(n,rev=0):
    
    if n==0:
        return 
    
    return reverse(n//10, rev*10 + n%10) 
n=int(input("enter any number:"))
print(reverse(n))