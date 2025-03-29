# Linear Search - Multiple Occurences

def contOccurences(A,B):
    cnt=0
    for nums in A:
        if nums==B:
            cnt+=1

    return cnt;

A=list(map(int,input("Enter the input : ").split()))
B=int(input("Enter B : "))
print(f"Total Number of B in A : {contOccurences(A,B)}")    