# Given an array of size N. Rotate the array from right to left 'K' times (i.e) if the array last elements will
#  come at first position..
# N=5 arr= 1 2 3 4 5 6 7 8 9 K=3

# Brute Force
def RotateByK(A,K):
    n=len(A)
    K=K%n
    for _ in range(K):
        last_ele=A[-1]
        for i in range(n-1,0,-1):
            A[i]=A[i-1]

        A[0]=last_ele
    return A

 #  Optimized Way

def reverse(A,start,end):
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1

def rotate_K_times(A,K):
    n=len(A)
    K=K%n
    # reverse the entire array
    reverse(A,0,n-1)
    #  reverse the upto K elements
    reverse(A,0,K-1)
    #  reverse the remaining elements
    reverse(A,K,n-1)
    return A


A=list(map(int,input("Enter the element : ").split()))
K=int(input("Enter K : "))            
rotate_K_times(A,K)
print(f"After {K} rotation : {A}  ")