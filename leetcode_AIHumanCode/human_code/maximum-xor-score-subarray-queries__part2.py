# Time:  O(n^2 + q)
# Space: O(n^2)
# dp
class Solution2(object):
    def maximumSubarrayXor(self, nums, queries):
        """
        """
        dp = [[nums[i] if i == j else 0 for j in range(len(nums))] for i in range(len(nums))]
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                dp[i][j] = dp[i][j-1]^dp[i+1][j]
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(nums)):
                dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i+1][j])
        return [dp[i][j] for i, j in queries]
