# In-place Prefix Sum
# Given an array A of N integers. Construct prefix sum of the array in the given array itself.


def prefixSum(A):
    n=len(A)

    for i in range(1,n):
        A[i]=A[i-1]+A[i]

    return A

A=list(map(int,input("Enter the element : ").split()) )   
print(f"Prefix Sum : {prefixSum(A)}")