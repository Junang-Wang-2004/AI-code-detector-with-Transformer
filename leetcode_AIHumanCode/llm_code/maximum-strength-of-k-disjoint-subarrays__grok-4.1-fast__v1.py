class Solution(object):
    def maximumStrength(self, nums, k):
        n = len(nums)
        NINF = -10**20
        dp = [[NINF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for s in range(k + 1):
                dp[i + 1][s] = max(dp[i + 1][s], dp[i][s])
                if s < k:
                    sign = 1 if s % 2 == 0 else -1
                    contrib = nums[i] * (k - s) * sign
                    dp[i + 1][s + 1] = max(dp[i + 1][s + 1], dp[i][s] + contrib)
        return dp[n][k]
