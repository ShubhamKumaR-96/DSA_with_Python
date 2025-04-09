# Selection Sort 

def selectionSort(A):
    n=len(A)

    for i in range(n):
        minIdx=i
        for j in range(i+1,n):
            if A[minIdx]>A[j]:
                minIdx=j
        A[i],A[minIdx]=A[minIdx],A[i] 
    return A     

A=[3,9,7,16,2,6]
print(f"List after Selection Sorting : {selectionSort(A)}")
