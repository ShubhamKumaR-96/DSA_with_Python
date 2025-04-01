# Reverse in a range
# Given an array A of N integers. Also given are two integers B and C. Reverse the array A in the given range [B, C]

def reverseRange(A,B,C):
    left=B
    right=C
    while left<=right:
        A[left],A[right]=A[right],A[left]
        left+=1
        right-=1
    return A    

        
        
A=list(map(int,input("Enter the input : ").split()))
B=int(input("Enter B : "))
C=int(input("Enter C : "))
print(f" Reverse in a range {reverseRange(A,B,C)}")