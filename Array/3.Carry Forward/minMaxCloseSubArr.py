
# Closet MinMax
#  Given an array. Find the length of smallest subarray which contains both min and max of array

def minmaxCloset(A):
    n=len(A)
    min_val=min(A)
    max_val=max(A)
    result=float('inf')

    for i in range(n):
        for j in range(i,n):
            subarray=A[i:j+1]

            if min_val in subarray and max_val in subarray:
                length=j-i+1
                result=min(result,length)

    return result    

A=list(map(int,input("Enter the element : ").split()))
print(f"closet min max in subArray length : {minmaxCloset(A)}")
