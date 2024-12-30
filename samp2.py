def max_length_subsequence(arr, k):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if (arr[i] - arr[j]) % k == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
k = 2
print(max_length_subsequence(arr, k))
