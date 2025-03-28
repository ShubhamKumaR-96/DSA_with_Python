# Given a String S. Toggle the case of every char

def toggleString(S):
    result=""
    for char in S:
        if char.isupper():
            result+=char.lower()
        elif char.islower():
            result+=char.upper() 
        else:
            result+=char  

    return result   

S = input("Enter the string : ")
print(f"After toggling the String : {toggleString(S)}")    
