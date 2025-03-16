# Given N elements of array .Count the no of elements having atleast one greater than itself.
# Arr= -3 2 6 8 4 8 5 8 3

def countTotalGreater(A):
    n=len(A)
    cnt=0
    maxEle=float('-inf')
    for i in range(n):
        if arr[i]>maxEle:
            maxEle=arr[i]
            cnt=1
        elif arr[i]==maxEle:
            cnt+=1;    
    
    return (n-cnt)

arr=list(map(int,input("Enter the element : ").split()))    
print(f"Total Greater element itself : {countTotalGreater(arr)}")