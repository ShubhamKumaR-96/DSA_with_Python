
def countOddNo(arr,queries):
    n=len(arr)
    pf=[0]*n
    pf[0]=1 if arr[0]%2!=0 else 0

    for i in range(1,n):
        pf[i]=pf[i-1]+ (1 if arr[i]%2!=0 else 0)


    for l,r in queries:
        count=0
        if l==0:
            count=pf[r]
        else:
            count=pf[r]-pf[l-1]
        print(f"total odd no from {l} to {r}= {count}")   

arr = [2, 4, 3, 7, 9, 8, 6]    
queries = [(1, 5), (0, 3)]
countOddNo(arr,queries)     


