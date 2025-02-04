# write stable selection sort

def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j

        min_val=arr[min_idx]

        while min_idx>i:
            arr[min_idx]=arr[min_idx-1]
            min_idx-=1

        arr[i]=min_val  

list=input("Enter the list of numbers: ").split()
arr=[int(x) for x in list]
selectionSort(arr)
print("Sorted array is: ",arr)   
