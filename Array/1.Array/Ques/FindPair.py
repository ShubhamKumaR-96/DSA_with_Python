# Given N array elements.Check if there exits a pair (i,j) such that arr[i]+arr[j]==k and
#  a pair(i,j) such that arr[i]+arr[j]==k & i!=j.  
#  arr= 3 -2 1 4 3 6 8

def findPair(A,k):
    n=len(A)
    for i in range(n):
        for j in range(i+1,n):
            if A[i]+A[j]==k:
                return (i,j)

    return False

A=list(map(int,input("Enter the elememts : ").split()))  
K=int(input("Enter K : "))

result=findPair(A,K)
if(findPair(A,K)):
    print(f"Pairs at index {result[0],result[1]} ")  
else:
    print("Not pair")          