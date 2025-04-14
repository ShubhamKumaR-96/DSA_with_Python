# Given an array elements find distinct elements

def distinctEle(A):

    num_list=set()

    for num in A:
        num_list.add(num)

    ans=len(num_list)    

    return ans

A=list(map(int,input("Enter the input : ").split()))  
print(f"Total disinc Element : {distinctEle(A)}")