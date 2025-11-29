# Time:  O(n^2)
# Space: O(n)
# dp
class Solution2(object):
    def maxScore(self, nums):
        """
        """
        dp = [0]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                dp[i] = max(dp[i], dp[j]+(i-j)*nums[i])
        return dp[-1]
