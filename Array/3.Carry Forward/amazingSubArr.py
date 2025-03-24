def countAmazingSubarrays(S):
    n = len(S)
    vowels = set('aeiouAEIOU')
    count = 0
    
    # For each vowel, count substrings starting from it
    for i in range(n):
        if S[i] in vowels:
            count += (n - i)  # Number of substrings starting at i
    
    return count % 10003

# Test
S = "ABEC"
print(f"Total Amazing Subarrays (Optimized): {countAmazingSubarrays(S)}")  # Output: 6