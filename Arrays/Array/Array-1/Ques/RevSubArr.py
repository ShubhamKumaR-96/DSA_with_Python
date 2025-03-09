# Given an array of N elements. Two Indices S1 and e1 are also given . Reverse the array from s1 to e1.
# arr= 1 2 3 4 8 10

def RevSubArray(A,S1,E1):
    n=len(A)
    if S1 < 0 or E1 >= n or S1 > E1:
        print("Invalid indices. No changes made.")
        return
    p1, p2 = S1, E1
    while p1 < p2:
        A[p1], A[p2] = A[p2], A[p1]
        p1 += 1
        p2 -= 1

A=list(map(int,input("Enter Elements: ").split()))
S1=int(input("Starting Idx : "))
E1=int(input("Ending Idx: "))
RevSubArray(A,S1,E1)
print(f"Reversing from {S1} to {E1} : {A}" )