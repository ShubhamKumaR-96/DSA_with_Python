# Given an array A[N] , (x,y,z) Array A is sorted from x=>y-1 sorted from y-z   sort the array x-z   i/p = 8 1 3 6 11 2 4 9 7 6

def sortSubarray(A,x,y,z):
    left=A[x:y]
    right=A[y:z+1]

    i=j=0
    merged=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1


    merged.extend(left[i:])
    merged.extend(right[j:])

    A[x:z+1]=merged

       

A = list(map(int, input("Enter list : ").split()))
x=int(input("Enter X : "))
y=int(input("Enter y : "))
z=int(input("Enter z : "))

sortSubarray(A,x,y,z)
print("Sorted Subarray : ",A)
