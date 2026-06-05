#Program to Check strong number
#A Strong Number is a number whose value is equal to the sum of the factorials of its digits. (Example 145)
x=int(input("Enter any number:"))
temp=x #storing the number in temp variable. 
sum=0
while temp>0:
    digit = temp%10

    fact=1
    for i in range(1,digit+1):
        fact = fact*i
    sum += fact

    temp = temp//10
if(sum==x):
    print("It is a Strong number!!")
else:
    print("Not a Strong number!!")    


