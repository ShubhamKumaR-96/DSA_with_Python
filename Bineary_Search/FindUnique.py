# Find the unique element
# Question
# Every element occurs twice except for 1, find the unique element. Note: Duplicate elements are adjacent to each other but the array is not sorted.
# 7	7	6	6	3	8	8	1	1	9	9

def findUnique(arr):
    n = len(arr)
    
    # Edge case: If there's only one element
    if n == 1:
        return arr[0]
    
    startIdx = 0
    endIdx = n - 1

    while startIdx <= endIdx:
        mid = startIdx + (endIdx - startIdx) // 2

        # If mid is the unique element
        if (mid == 0 or arr[mid] != arr[mid-1]) and (mid == n-1 or arr[mid] != arr[mid+1]):
            return arr[mid]

        # If mid is part of a pair, check the pattern
        if mid > 0 and arr[mid] == arr[mid-1]:  
            if mid % 2 == 0:
                endIdx = mid - 2  # Move left
            else:
                startIdx = mid + 1  # Move right
        else:
            if mid % 2 == 0:
                startIdx = mid + 2  # Move right
            else:
                endIdx = mid - 1  # Move left

    return -1  # If no unique element is found (shouldn't happen for valid input)

# Taking user input
user_input = input("Enter elements (duplicates are adjacent): ")
arr = list(map(int, user_input.split()))  # Convert input to list of integers

print("Unique element:", findUnique(arr))

