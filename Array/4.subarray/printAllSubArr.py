# Generate all subarray

def printAllSubArr(A):
    n=len(A)
    for i in range(n):
        for j in range(i,n):
            subArr=A[i:j+1]
            print(subArr)


A=list(map(int,input("Enter the element :").split())) 
printAllSubArr(A)           