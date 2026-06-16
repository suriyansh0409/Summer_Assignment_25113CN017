#Program to Find maximum frequency element.
arr=[1, 5, 7, 10, 5, 6, 8, 5, 8 ]
maxelements=0
frequency=0

for i  in range (len(arr)):
    freq=arr.count(i)
    if freq> frequency:
        frequency=freq
        maxelements=i

print("Maximum frequency elements",maxelements)
print("Frequency",frequency)



