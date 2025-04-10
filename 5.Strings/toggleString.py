# Given a string S.Toggle the every char of string 

def toggleString(S):
    

    result=''
    for char in S:
        if 'a' <=char <= 'z':
            result+=chr(ord(char)-32)

        elif 'A' <=char <= 'Z':
            result+=chr(ord(char)+32)

        else:
            result+=char

    return result 

S=input("Enter String : ")
print(f"After Toggling : {toggleString(S)}")              

