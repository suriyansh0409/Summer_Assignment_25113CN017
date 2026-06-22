# program to Bubble sort. 
def bubble(arr):
    n=len(arr)
    swaped=False
    for i in range (n):
        for j  in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaped= True
        if not swaped:
            break

arr=[40,20,30,10,50]
bubble(arr)
print("Sorted array =",arr)
        
