# Given a string and start and end index. Reverse the part of string 
# b/s S to e index 

def reverseString(A,start,end):
    
    char_list = list(A)

    left=start
    right=end

    while left<right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left+=1
        right-=1

    return ''.join(char_list)    


S=input("Enter String : ")
start=int(input("Enter Start idx : "))
end=int(input("Enter end idx : "))
print(f"After Sorting : {reverseString(S,start,end)}")   

