#  program to Print character pyramid
#                                A 
#                               ABA 
#                              ABCBA 
#                             ABCDCBA 
#                            ABCDEDCBA 

n=int(input("Enter the number of rows:"))
for i in range (1,n+1):
    spaces=(n-i)
    print(" " *spaces,end="")
    for j in range(i-1):
        print(chr(65+j),end="")
    for j in range(i-1,-1,-1):
        print(chr(65+j),end="")
    print()
