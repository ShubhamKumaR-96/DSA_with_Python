def equlibirumIndex(arr):
    n=len(arr)
    if n==0:
        return -1

    ps=[0]*n
    ps[0]=arr[0]
    for i in range(1,n):
        ps[i]=ps[i-1]+arr[i]

    for i in range(1,n-1):
        if ps[i-1]==ps[n-1]-ps[i]:
            return i    

    return -1


arr=input("Enter elements of array  : ").split()
arr=[int(i) for i in arr]
print(f"equlibirum index is {equlibirumIndex(arr)}")    
