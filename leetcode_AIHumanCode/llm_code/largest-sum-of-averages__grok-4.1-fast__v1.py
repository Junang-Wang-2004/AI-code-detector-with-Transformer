class Solution(object):
    def largestSumOfAverages(self, A, K):
        n = len(A)
        prefix = [0.0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + A[i]
        dp = [[0.0] * n for _ in range(K + 1)]
        for i in range(n):
            dp[1][i] = prefix[i + 1] / (i + 1)
        for parts in range(2, K + 1):
            for i in range(parts - 1, n):
                dp[parts][i] = max(
                    dp[parts - 1][j] + (prefix[i + 1] - prefix[j + 1]) / (i - j)
                    for j in range(parts - 2, i)
                )
        return dp[K][n - 1]
