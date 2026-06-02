#  program to Reverse a number
num=int(input("enter any Number:"))
reverse=0
while num>0:
    digit=num % 10
    reverse= reverse*10 + digit
    
    num=num//10

print("The reverse of the given number is:",reverse)