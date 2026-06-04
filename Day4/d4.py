# Program to Print Armstrong numbers in a range
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
for i in range (start,end+1):
    power=len(str(i))
    total=0

    for digits in str(i):
        total=total+ (int(digits)** power)
    if total==i:
        print(total)
        



