# Search element K
# Problem Statement
# Given a sorted array with distinct elements, search the index of an element k, if k is not present, return -1.
#  arr[] =3	6	9	12	14	19	20	23	25	27

def bineaySearch(arr,k):
    n=len(arr)
    startIdx=0
    endIdx=n-1
    while startIdx<endIdx:
        mid=startIdx+(endIdx-startIdx)//2
        if arr[mid]==k:
            return mid;
        elif arr[mid]<k:
            startIdx=startIdx+1
        else:
            endIdx-=1

    return -1

# Taking user input
user_input = input("Enter sorted elements  ")
arr = list(map(int, user_input.split()))  # Convert input to list of integers

target = int(input("Enter the target element: "))

result=bineaySearch(arr,target)

if(result!=-1):
    print("element index : " ,result)
else:
    print("element not found")
 
