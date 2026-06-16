#Program to Find pair with given sum. 
arr=[2,7,8,11]
target=13
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("Pair found:", arr[i],arr[j])