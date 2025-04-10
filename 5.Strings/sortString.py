# Given a string containing lowercase alphabet (N). Sort the String 

def sort_String(S):
    
    count = [0] * 26

    for char in S:
        count[ord(char) - ord('a')] += 1

    result=''

    for i in range(26):
        result += chr(i + ord('a')) * count[i]

    return result


S=input("Enter String : ")
print(f"After Sorting : {sort_String(S)}")             