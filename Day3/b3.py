#Program to Print prime numbers in a range
x=int(input("Enter the starting number:"))
y=int(input("Enter the ending number:"))
for num in range(x,y+1): #y+1 because last number is not included in python.
    if num>1:
        prime=True

    for i in range(2,num): #Here we are checking which numbers are Prime.
        if  (num%i==0):
            prime=False
            break
    else:
        print(num)
