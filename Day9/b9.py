#  a program to Print reverse number triangle
#                        12345 
#                        1234 
#                        123 
#                        12 
#                        1
n=int(input("enter the number :"))
for i in range (n,0,-1): #range(start,stop,step)
    for j in range(1,i+1): #range(start,step)
        print(j,end="")
    print()