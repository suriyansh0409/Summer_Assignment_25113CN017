# program to Binary search.
# array should be sorted 
def search (arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            print ("Element is at index  =",i)
            
        else :
            i+=1

arr=[10, 20, 30, 40, 50]
target=50
search(arr,target)

    