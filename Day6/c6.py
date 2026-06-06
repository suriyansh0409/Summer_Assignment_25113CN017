# program to Count set bits in a number.

n = int(input("Enter a number: "))

# Convert the number to binary and count how many times '1' appears
count = bin(n).count('1')

print("Number of set bits:", count)