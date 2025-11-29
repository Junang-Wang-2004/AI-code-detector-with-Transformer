# Time:  O(n^2 + q)
# Space: O(n^2)

# dp
class Solution(object):
    def maximumSubarrayXor(self, nums, queries):
        """
        """
        dp = [[nums[i] if j == 0 else 0 for j in range(len(nums)-i)] for i in range(len(nums))]
        for i in reversed(range(len(nums))):
            for l in range(1, len(nums)-i):
                dp[i][l] = dp[i][l-1]^dp[i+1][l-1]
        for i in reversed(range(len(nums))):
            for l in range(1, len(nums)-i):
                dp[i][l] = max(dp[i][l], dp[i][l-1], dp[i+1][l-1])
        return [dp[i][j-i] for i, j in queries]


