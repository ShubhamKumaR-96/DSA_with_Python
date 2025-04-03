# Binary Search Problems - Find first occurrence
# Problem Statement
# Given a sorted array of N elements, find the first occurrence of the target element.
#  arr[] =-5 5	-3	0	0	1	1	5	5	5	5	5	5	5	8	10	10	15	15

def findFirstOcc(arr,k):
    n=len(arr)
    startIdx=0
    endIdx=n-1
    firstIdx=-1

    while startIdx<=endIdx:
        mid=startIdx+(endIdx-startIdx)//2
        if arr[mid]==k:
            firstIdx=mid
            endIdx=mid-1
        elif arr[mid]<k:
            startIdx=mid+1
        else:
            endIdx=mid-1

    return firstIdx


# Taking user input
A=list(map(int,input("Enter the ele: ").split()))

target = int(input("Enter the target element: "))

result=findFirstOcc(A,target)

if result!=-1:
    print(f"first element found at index : {result}")
else:
    print("element not found")
