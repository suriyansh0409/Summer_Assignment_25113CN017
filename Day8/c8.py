# program to Print character triangle. 
#                   A 
#                   AB 
#                   ABC 
#                   ABCD 
#                   ABCDE 
n=int(input("Enter any number:"))  #chr(65)=A,chr(66)=B and so on
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end="") #chr() converts an ASCII value to a character.
    print()