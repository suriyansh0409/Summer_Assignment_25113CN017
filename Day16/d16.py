# Program to Remove duplicates from array.
arr=[4,5,8,9,8,9,8,7,5,4,8,1]

unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)

