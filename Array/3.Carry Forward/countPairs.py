# Count PAIRS 'ag'

# Brute force way

# def countPairs(A):
#     n=len(A)
#     count=0
#     for i in range(n):
#         if A[i]=='a':
#             for j in range(i,n):
#                 if A[j]=='g':
#                     count+=1

#     return count

# Optimized way

# def countPairs(A):
#     n=len(A)
#     count_g=0
#     ans=0
#     for i in range(n-1,-1,-1):
#         if A[i]=='g':
#             count_g+=1
#         elif A[i]=='a':
#             ans+=count_g

#     return ans

# Assignment Todo
def countPairs(A):
    n=len(A)
    count_a=0
    ans=0
    for i in range(n):
        if A[i]=='a':
            count_a+=1
        elif A[i]=='g':
            ans+=count_a

    return ans
            
        


A=input("Enter the characters : ")
print(f"Total Pairs : {countPairs(A)}")

