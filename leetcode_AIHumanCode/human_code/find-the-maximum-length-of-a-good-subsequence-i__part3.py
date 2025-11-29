# Time:  O(n^2 * k)
# Space: O(n * k)
# dp
class Solution(object):
    def maximumLength(self, nums, k):
        """
        """
        dp = [[0]*(k+1) for _ in range(len(nums))]
        result = 0
        for i in range(len(nums)):
            dp[i][0] = 1
            for l in range(k+1):
                for j in range(i):
                    dp[i][l] = max(dp[i][l], dp[j][l]+1 if nums[j] == nums[i] else 1, dp[j][l-1]+1 if l-1 >= 0 else 1)
                result = max(result, dp[i][l])
        return result
