# 162. Find Peak Element

def peakEle(A):
    n=len(A)

    if n==1:
        return 0
    if A[0]>+A[1]:
        return A[0]
    if A[n-1]>A[n-2]:
        return A[n-1]
    
    start=1
    end=n-2

    while start<=end:
        mid=start+(end-start)//2

        if A[mid]>A[mid+1] and A[mid]>A[mid+1]:
            return A[mid]
        
        elif A[mid]<A[mid-1]:
            end=mid-1

        else:
            start=mid+1


A=list(map(int,input("Enter the ele: ").split()))
print(f"Peak Element : {peakEle(A)}")                