# program to Print reverse pyramid. 
#                       ********* 
#                        ******* 
#                         ***** 
#                          *** 
#                           * 

n=int(input("Enter the number of rows:"))
for i in range(n):
    spaces=i
    stars=2*(n-i)-1        
    print(" " * spaces,end="")
    print("*" *stars)


