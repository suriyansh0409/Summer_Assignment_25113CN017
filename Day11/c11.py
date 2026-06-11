#Program to Write function to check prime 
def prime(n):
    if n<=1:
        return "Not a Prime Number!!!"
        
    for i in range (2,n):
        if n%i==0:
            return "Not a Prime Number!!!"
            
           
    return" it is a prime number"
n=int(input("Enter the  number:"))
print(prime (n))
    
