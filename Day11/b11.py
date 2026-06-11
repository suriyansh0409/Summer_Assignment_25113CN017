#Program to Write function to find maximum
def maxima(x,y):
    if (x>y):
        return x
    else:
        return y

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print("The greatest is:", maxima(x,y))