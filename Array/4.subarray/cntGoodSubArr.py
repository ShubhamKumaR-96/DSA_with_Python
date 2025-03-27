# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:

# Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.
# Input 1: A = [1, 2, 3, 4, 5] B = 4

# Input 2: A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9] B = 65

def cntGoodSubArr(A, B):
    n = len(A)
    cnt = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += A[j]
            length = j - i + 1
            if (length % 2 == 0 and curr_sum < B) or (length % 2 != 0 and curr_sum > B):
                cnt += 1
    return cnt

A = list(map(int, input("Enter the input : ").split())) 
B = int(input("Enter the B : "))
print(f"Total Good Sub Array : {cntGoodSubArr(A, B)}")
           
