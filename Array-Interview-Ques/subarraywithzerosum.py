# Subarray with Zero Sum
# Given an array of size N, return whether the array contains a subarray with sum=0
#  A = 1 -4 9 -1 2 -10 6 5

# Brute force way
# def has_Zero_Sum(A):
#     n=len(A)
#     for i in range(n):
#         curr_sum=0
#         for j in range(i,n):
#             curr_sum+=A[j]
#             if curr_sum==0:
#                 return True
            
#     return False
    

# Prefix Sum + Hashing

def has_Zero_Sum(A):
    n=len(A)
    pf=0
    sum_map={0:1}
    for num in A:
        pf+=num
        if pf in sum_map:
            return True
        sum_map[pf]=sum_map.get(pf,0)+1

    return False    


A=list(map(int,input("Enter the input : ").split())) 
if(has_Zero_Sum(A)):
    print("Array Contains Zero Sum")
else:
    print("Not having Zeo Sum")    
            