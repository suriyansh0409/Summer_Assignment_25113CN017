#  program to Print star pyramid. 
#                       * 
#                      *** 
#                     ***** 
#                    ******* 
#                   *********

n=int(input("Enter the number of rows:"))
for i in range (n):
    star= 2*i+1
    spaces= n-i-1
    print(" " * spaces,end="") 
    print("*" * star)
