# Given an array A of N non-negative numbers and a non-negative number B, 
# you need to find the number of subarrays in A with a sum less than B. 
# We may assume that there is no overflow.

def countSubArr(A,B):
    n=len(A)
    cnt=0
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum+=A[j]
            if curr_sum<=B:
                cnt+=1
            else:
                break    
    return cnt
            
A=list(map(int,input("Enter the input : ").split())) 
B=int(input("Enter the B : "))
print(f"Total Sub Array Greater than {B} : {countSubArr(A,B)} ")            
