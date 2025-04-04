# 540. Single Element in a Sorted Array


def unique(A):
    n=len(A)

    if n==1:
        return A[0]
    if A[0]!=A[1]:
        return A[0]
    if A[n-1]!=A[n-2]:
        return A[n-1]
    
    start=1
    end=n-2

    while start<=end:
        mid=start+(end-start)//2

        if A[mid]!=A[mid+1] and A[mid]!=A[mid-1]:
            return A[mid]
        
        if mid%2==0:
            if A[mid]==A[mid+1]:
                start=mid+2
            else:
              end=mid-1
        else:
            if A[mid]==A[mid-1]:
                start=mid+1
            else:
                end=mid-1  

A=list(map(int,input("Enter the ele: ").split()))
print(f"Unique Element : {unique(A)}")     