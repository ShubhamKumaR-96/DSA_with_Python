# Given an array and q queries 
# A=[ 2 6 3 8 2 8 2 3 8] for each query element tell the freq

def freqCnt(A):
    freq_cnt={}

    for num in A:
        if num in freq_cnt:
            freq_cnt[num]+=1
        else:
            freq_cnt[num]=1

    return freq_cnt        

A=list(map(int,input("Enter the input : ").split()))  
frq_dict=freqCnt(A)

Q=int(input("Enter the Queries : "))

for _ in range(Q):
    value=int(input("Enter the Val : "))
    
    print(f"Freq of {value} is {frq_dict.get(value,0)}")




