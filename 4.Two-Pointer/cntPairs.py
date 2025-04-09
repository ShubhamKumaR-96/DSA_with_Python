def cntPairs(A,K):
    n=len(A)
    A.sort()
    start=0
    end=n-1
    cnt=0

    while start<end:
         if A[start]+A[end]==K:
              cnt+=1
              start+=1
              end-=1
         if A[start]+A[end]>K:
              end-=1
         else:
              start+=1 
    return cnt          

A=list(map(int,input("Enter elements : ").split()))
K=int(input("Enter K : "))
print(f"Total Pairs: {cntPairs(A,K)}")                       
              

              




       

