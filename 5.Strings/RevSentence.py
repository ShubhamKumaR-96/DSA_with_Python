# Given a char[] which stores a sentence 

def reverse(A,start,end):
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1

def rev_word(S):
    char_list=list(S)
    n=len(S)
 
    # Step 1: Reverse the entire string
    reverse(char_list,0,n-1)

    # Step 2: Reverse each word
    start=0
    for i in range(n):
        if char_list[i] == "_":
            # Reverse the word from start to i-1
            reverse(char_list,start,i-1)
            start=i+1
    
    # Reverse the last word (from start to end of string)
    reverse(char_list,start,n-1)        

    return ''.join(char_list)

S=input("Enter String : ")
print(f"Reverse Word : {rev_word(S)}")


