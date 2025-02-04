# write bubble sort arr = [5, 3, 8, 4, 6]

def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        flag=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True

        if not flag:
            break


list=input("Enter the list of numbers: ").split()
arr=[int(x) for x in list]
bubbleSort(arr)
print("Sorted array is: ",arr)

