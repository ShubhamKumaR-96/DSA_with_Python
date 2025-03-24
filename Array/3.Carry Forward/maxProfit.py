def maxProfit(A):
    n = len(A)
    max_profit = 0
    
    # Check every buy-sell pair
    for i in range(n):
        for j in range(i + 1, n):
            profit = A[j] - A[i]
            max_profit = max(max_profit, profit)
    
    return max_profit if max_profit > 0 else 0

# Test
print(maxProfit([1, 2]))          
print(maxProfit([1, 4, 5, 2, 4])) 