# Given an array of size N. find and return the max sum of any sub array I/P = -2 3 4 -1 5 -10 7

# Brute forre way

def maxSubArraySum(arr):
    n = len(arr)
    
    # Edge case: Empty array
    if n == 0:
        return 0  # Return 0 and invalid indices for empty array

    maxSum = float('-inf')  # Initialize maximum sum
    start = end = 0  # Initialize start and end indices of the maximum subarray

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            # Update maxSum and indices if current sum is greater
            if curr_sum > maxSum:
                maxSum = curr_sum
                start = i
                end = j

    return maxSum, start, end

# Input handling
arr = list(map(int, input("Enter list elements: ").split()))
maxSum, start, end = maxSubArraySum(arr)

# Output the result
if start == -1 and end == -1:
    print("The array is empty.")
else:
    print(f"Maximum subarray sum: {maxSum}")
    print(f"Subarray starts at index {start} and ends at index {end}")
    print(f"Subarray: {arr[start:end+1]}")