#  a program to Print repeated character pattern
#                       A 
#                       BB 
#                       CCC 
#                       DDDD 
#                       EEEEE

n=int(input("Enter number of Rows :"))
for i in range (n):
    char=chr(65+i)
    for j in range (i+1):
        print(char,end="")

    print()