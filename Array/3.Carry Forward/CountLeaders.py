#  Count Leaders in Array

# Brute DForce way

# def countLeaders(A):
#     n=len(A)
#     leader=0
#     for i in range(n):
#         is_leader=True
#         for j in range(i+1,n):
#             if A[i]<A[j]:
#                 is_leader=False
#                 break

#         if is_leader:
#             leader+=1

#     return leader

# Optimized Way

def countLeaders(A):
    n=len(A)
    max_so_far=A[n-1]
    leader=1
    for i in range(n-2,-1,-1):
        if A[i]>max_so_far:
            leader+=1
            max_so_far=A[i]

    return leader        

A=list(map(int,input("Enter the element : ").split()))
print(f"Total Leaders = {countLeaders(A)}")            