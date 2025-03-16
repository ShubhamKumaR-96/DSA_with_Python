# Equilibrium Index
# Problem: Find indices where the sum of elements to the left equals the sum to the right.

def equlibriumIdx(arr):
    n=len(arr)
    count=0
    for i in range(n):
        leftSum=sum(arr[:i])
        rightSum=sum(arr[i+1:])
        if leftSum==rightSum:
            count+=1
            print(f"equlibrium index at {i}")  
    return count  

arr=list(map(int,input("Enter the elements : ").split()))    
print(equlibriumIdx(arr))

