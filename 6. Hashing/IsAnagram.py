def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    char_cnt = {}
    for char in s1:
        char_cnt[char] = char_cnt.get(char, 0) + 1
    
    for char in s2:
        if char not in char_cnt:
            return False
        
        char_cnt[char] -= 1
        if char_cnt[char] == 0:
            del char_cnt[char]
    
    return len(char_cnt) == 0

# Test the function
print(anagram("listen", "silent"))  # True
print(anagram("hello", "world"))    # False