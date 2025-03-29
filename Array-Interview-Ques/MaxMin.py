# Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

def maxMinSum(A):
    maxNo=max(A)
    minNo=min(A)
    totalSum=maxNo+minNo
    return totalSum


A=list(map(int,input("Enter the input : ").split()))
print(f"max min of sum : {maxMinSum(A)}")



