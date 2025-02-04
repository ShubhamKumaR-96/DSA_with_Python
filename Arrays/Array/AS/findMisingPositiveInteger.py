# Given an unsorted integer array A of size N, find the first missing positive integer. The algorithm should run in O(n) time and use constant space.

# Example:

# Input: [3, 4, -1, 1]

# Output: 2 (because 2 is the first missing positive integer


def findMissingPostiveInteger(arr):
    n=len(arr)

    for i in range(1,n+2):
        if i not in arr:
            return i

    return 1

arr=[3,4,-1,1]
print(findMissingPostiveInteger(arr)) #2            