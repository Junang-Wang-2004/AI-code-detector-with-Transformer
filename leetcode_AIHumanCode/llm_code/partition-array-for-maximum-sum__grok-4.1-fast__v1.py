class Solution:
    def maxSumAfterPartitioning(self, A, K):
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            mx = 0
            left = max(0, i - K)
            for j in range(i - 1, left - 1, -1):
                mx = max(mx, A[j])
                dp[i] = max(dp[i], dp[j] + mx * (i - j))
        return dp[n]
