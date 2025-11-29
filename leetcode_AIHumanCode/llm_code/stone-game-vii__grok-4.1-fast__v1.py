class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + stones[i]
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                remove_left = presum[right + 1] - presum[left + 1]
                remove_right = presum[right] - presum[left]
                dp[left][right] = max(remove_left - dp[left + 1][right],
                                      remove_right - dp[left][right - 1])
        return dp[0][n - 1]
