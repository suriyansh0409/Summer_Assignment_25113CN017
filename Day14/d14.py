#  program to Find duplicates in array.
# Program to find duplicates in an array

l = [10,20,10,50,60,20,80,50,40,30,]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            print(l[i])
            break