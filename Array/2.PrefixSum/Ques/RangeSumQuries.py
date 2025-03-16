# Topic 1: Range Sum Queries
# Problem: Given an array and queries with left (L) and right (𝑅) indices, compute the sum of elements from 𝐿 to 𝑅

# def rangeQuerySum(arr,quries):
#     for l,r in quries:
#         total=0
#         for i in range(l,r+1):
#             total+=arr[i]
#         print(f" sum from {l} to {r} = {total}")  # T.C =>O(Q.N)

# arr=list(map(int,input("Enter element : ").split()))     
# quries=[(1,4),(0,2)]
# rangeQuerySum(arr,quries)

# OPTIMIZED WAY USING PREFIX_SUM

def quriesSum(arr,queries):
    n=len(arr)
    pf=[0]*n
    pf[0]=arr[0]
    
    # prefix sum
    for i in range(1,n):
        pf[i]=pf[i-1]+arr[i]

    for l,r in queries:
        if l==0:
            total=pf[r]
        else:
            total=pf[r]-pf[l-1]
        print(f" sum from {l} to {r} = {total}")  

arr=list(map(int,input("Enter the elements: ").split())) 
quries=[(4,8),(3,7),(1,3),(0,4)]
quriesSum(arr,quries)

            



