# 4: Even Numbers in a Given Range
# Problem: Given an array and queries [𝐿],[𝑅][L],[R], count even numbers in each range.

# Brute force way
# def countEvenNo(arr,quries):
#     for l,r in quries:
#         count=0
#         for i in range(l,r+1):
#             if arr[i]%2==0:
#                 count+=1
#         print(f" Even NO from {l} to {r} = {count}")



# Optimized way using prefix sum

def totalEvenNo(arr,queries):
    n=len(arr)
    pf=[0]*n
    pf[0]=1 if arr[0]%2==0 else 0

    for i in range(1,n):
        pf[i]=pf[i-1] + (1 if arr[i]%2==0 else 0)


    for l,r in queries:
        count=0
        if l==0:
            count+=pf[r]
        else:
             count=pf[r] - pf[l-1]   
        print(f"Even count from {l} to {r}: {count}")    





arr=list(map(int, input("Enter the element : ").split()))
queries=[(4,8),(0,4)]   
print(totalEvenNo(arr,queries))             