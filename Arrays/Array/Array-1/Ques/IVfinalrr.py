# Google => Given an array of size N. initiliazed with 0.Given Q queries of s,e,val.
# Add the given val to all indexs from s to e (both included).Return the final Array 

# Brute force way T.C => O(Q*N)

# def finalArrBF(N,Q):
#     arr=[0]*N

#     for s,e,val in Q:
#         for j in range(s,e+1):
#             arr[j]+=val
        
#     return arr    
 
# # Optimized Way => T.C O(Q+N) 

def finalArrOP(N,Q):
    arr=[0]*N

    for s,e,val in Q:
        arr[s]+=val
        if s+1<N:
            arr[s+1]-=val

    return arr        

# Example usage
N = 7
Q = [(1, 3, 2), (4, 6, 3), (2, 5, 1)]
result = finalArrOP(N, Q)
print("Final array (Optimized):", result)


# Taking user input
# N = int(input("Enter array size (N): "))
# Q = int(input("Enter number of queries (Q): "))

# queries = []
# for _ in range(Q):
#     s, e, val = map(int, input("Enter s, e, val (separated by spaces): ").split())
#     queries.append((s, e, val))
# result = finalArrOP(N, Q)
# print("Final array (Optimized):", result)       