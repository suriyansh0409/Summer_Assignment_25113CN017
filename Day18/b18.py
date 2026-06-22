# program to Selection sort. 
def selection (arr):
    n=len(arr)
    
    for i in range (n):
        mid_idx=i
        for j in range (i+1,n):

            if arr[j]<arr[mid_idx]:
                mid_idx=j

        arr[i],arr[mid_idx]=arr[mid_idx],arr[i]
    return arr

arr=[40,20,30,10,50]
selection(arr)
print("Sorted array =",arr) 