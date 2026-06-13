#Program to Write function for palindrome.
def palindrome(n):
    temp=n
    rev=0
    while n>0:
        digits=n%10
        rev=rev*10+digits
        n=n//10
    if (rev==temp):
        print("It is a palindrome number !")
    else:
        print("It is a  NOT palindrome number !")

n=int (input("Enter any number :"))
palindrome(n)
