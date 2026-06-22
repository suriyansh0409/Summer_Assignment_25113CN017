# program to Sort array in descending order. 
def desending(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                # i+=1
                arr[i],arr[j]=arr[j],arr[i]

    return arr
arr=[90,100,80,110,50,89,67,157]
desending(arr)
print("Sorted array =",arr)

