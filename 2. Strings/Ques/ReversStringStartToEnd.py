# Given a string and start and end index. Reverse the part of string b/w s to e idx

def reverseString(Str,s,e):
    s_list=list(Str)

    left=s
    right=e
    while left<right:
        s_list[left],s_list[right]=s_list[right],s_list[left]
        left+=1
        right-=1

    return ''.join(s_list)    


Str=input("Enter the string : ")
s=int(input("Enter start Idx : "))
e=int(input("Enter end Idx : "))

print(f"Reversing String : {reverseString(Str,s,e)}")