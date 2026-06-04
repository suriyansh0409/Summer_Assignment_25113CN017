#  program to Check Armstrong number.
x=int(input("Enter any number:"))
power=len(str(x))
total=0
for digits in str(x):
    total=total+ (int(digits) ** power)
if (total==x):
    print("it is an Armstrong number!!")
else:
    print("It is not an Armstrong number!")

