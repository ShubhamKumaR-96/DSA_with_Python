
# Given an array of size N. initialized with 0. Give q queries of index i and value v.
#  you have to add the given value to all index >= i. return the final state of arr  n= 7

def updateArrayBruteForce(N, queries):
    arr = [0] * N  # Initialize array with 0s

    # Process each query
    for i, v in queries:
        for j in range(i, N):  # Add v to all elements from index i to N-1
            arr[j] += v

    return arr

# Input
N = int(input("Enter size of array (N): "))
Q = int(input("Enter number of queries (Q): "))
queries = []
for _ in range(Q):
    i = int(input("Enter index (i): "))
    v = int(input("Enter value (v): "))
    queries.append((i, v))

# Output
print("Final array:", updateArrayBruteForce(N, queries))