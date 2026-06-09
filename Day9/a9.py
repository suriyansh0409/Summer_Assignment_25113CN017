#  a program to Print reverse star pattern. 
#                   ***** 
#                   **** 
#                   *** 
#                   ** 
#                   *

n=int(input("Enter the number:"))
for i in range (n,0,-1): #range(start,stop,step)
    for j in range (i):
        print("*", end="")
    print()
