# Given a S String containing lowercase alphabet(n). Sort the string 

# brute force way

def sortString(S):
    s_list=list(S)
    n=len(s_list)
    for i in range(n):
        for j in range(0,n-i-1):
            if s_list[j]>s_list[j+1]:
                s_list[j],s_list[j+1]=s_list[j+1],s_list[j]

    return ''.join(s_list)   

S=input("Enter the string : ")
print(f"After String Sorting : {sortString(S)}")        