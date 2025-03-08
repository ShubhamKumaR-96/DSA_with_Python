# Given an array of size N initiliazed with 0 .
# Given Q queries pf index i and value v Add the given value to all index >=i.
#  Add the given value to all the index >=i. Return the final state of the array 

# Brute force way T.C => O(Q*N)

# def finalStateArrBF(N,Q):
#     arr=[0]*N

#     for i,v in queries:
#         for j in range(i,N):
#             arr[j]+=v

#     return arr



# Optimized Way => T.C O(Q+N)
def finalStateArr(N,Q):
    arr=[0]*N

    for i,v in Q:
        arr[i] += v

    # compute prefix sum
    for j in range(1,N):
        arr[j]+=arr[j-1]

    return arr            

# Taking user input 
N=int(input("Enter Array Size : "))
Q=int(input("Enter number of queries : "))

queries=[]

for _ in range(Q):
    i,v=map(int,input("Enter idx and value : ").split())
    queries.append((i,v))    

arr=finalStateArr(N,queries)
print(f"final state of Arr : {arr}")


# N=7;
# queries=[(1,3),(4,2),(2,1)]    
# list=finalStateArrBF(N,queries)
# print(list)
