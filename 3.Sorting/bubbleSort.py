# Bubble sort 

def bubbleSorting(A):
    n=len(A)

    for i in range(n):
        flag=True
        for j in range(0,n-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                flag=False
    return A

A=[3,9,7,16,2,6]
print(f"Bubble Sort: {bubbleSorting(A)}")


