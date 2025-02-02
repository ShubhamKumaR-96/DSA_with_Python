# Given n array element and q queries, find the sum of elements between the given range of queries
# Time Complexity: O(n) + O(q)

def prefix_sum(arr,q):
    n=len(arr)
    prefix=[0]*n
    prefix[0]=arr[0]
    for i in range(1,n):
        prefix[i]=prefix[i-1]+arr[i]

    # quries handling
    for i in range(q):
        while True:
            try:
                l,r=map(int,input(f"Query {i+1}: Enter starting and ending index :  ").split())
                if l<0 or r>=n or l>r:
                    print(f"Invalid input, please enter valid index between 0 to {n-1}")
                else:
                    break
            except ValueError:
                print(f"Invalid input, please enter valid index between 0 to {n-1}")



        if l==0:
            print(f"Sum of elements from index {l} to {r} = {prefix[r]}")
        else:
            print(f"Sum of elements from index {l} to {r} = {prefix[r]-prefix[l-1]}")


arr=input("Enter elements of array : ").split()
arr=[int(i) for i in arr]   
q=int(input("Enter number of queries : "))
prefix_sum(arr,q)


