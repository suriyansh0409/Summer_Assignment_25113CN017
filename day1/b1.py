
# Program to Print multiplication table of a given table 
def table(n):
    for i in range(1,11):
        print(n ,"X", i, "=" , n * i)
       

x=(int(input("enter the number :")))
table(x)