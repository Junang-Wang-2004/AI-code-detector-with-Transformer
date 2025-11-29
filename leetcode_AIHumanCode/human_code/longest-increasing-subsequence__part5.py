# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution5(object):
    def lengthOfLIS(self, nums):
        """
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

