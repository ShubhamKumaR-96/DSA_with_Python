# Question 1: Print a Subarray Given Start and End Indices

def printStartEndIdx(A,S,E):
    n=len(A)
    if S < 0 or E >= n or S > E:
        print("Give valid indices")
        return
    for i in range(S,E+1):
        print(A[i],end=" ")

A=list(map(int,input("Enter the input : ").split())) 
S=int(input("Enter Start Idx : "))
E=int(input("Enter end Idx : "))  
print(printStartEndIdx(A,S,E))     
