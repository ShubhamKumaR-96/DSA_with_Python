#  Given an array. Reverse the entire array
#  Note => Change the given array -> S.C=O(1)  A= 8 7 6 5 4 3 2 1

def revArr(A):
    n=len(A)
    p1,p2=0,n-1
    while p1<p2:
        A[p1],A[p2]=A[p2],A[p1]
        p1+=1
        p2-=1


A=list(map(int,input("Enter the elememnt : ").split()))   

revArr(A)
print(f"Reverse Array : {A}")