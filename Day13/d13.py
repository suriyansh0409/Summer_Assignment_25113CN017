#Program to Count even and odd elements. 
l=[100,50,65,47,92,12,54,84,98,63]
even=0
odd=0
for i in l:
    if i%2==0:
        even+= 1
    else :
        odd+=1
print("Number of even elements:", even)
print("Number of odd elements:", odd)