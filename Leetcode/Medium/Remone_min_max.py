# 2091. Removing Minimum and Maximum From Array

def removeMinMaX(A):
    n=len(A)

    min_val=min(A)
    max_val=max(A)

    min_idx=A.index(min_val)
    max_idx=A.index(max_val)

    left=min(min_idx,max_idx)
    right=max(min_idx,max_idx)

    option1=right+1
    option2=n-left
    option3=(left+1)+(n-right) 

    return min(option1,option2,option3)


A=list(map(int,input("Enter the ele: ").split()))
print(f"Min operation Required : {removeMinMaX(A)}")