class Solution:
    def validPartition(self, nums):
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if i >= 2 and nums[i - 1] == nums[i - 2]:
                dp[i] = dp[i] or dp[i - 2]
            if i >= 3:
                prev1, prev2, prev3 = nums[i - 3:i]
                if prev1 == prev2 == prev3 or prev2 == prev1 + 1 == prev3:
                    dp[i] = dp[i] or dp[i - 3]
        return dp[n]
