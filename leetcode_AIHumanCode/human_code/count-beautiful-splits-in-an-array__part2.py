# Time:  O(n^2)
# Space: O(n^2)
# dp
class Solution2(object):
    def beautifulSplits(self, nums):
        """
        """
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for i in reversed(range(len(nums))):
            for j in range(i+1, len(dp)):
                dp[i][j] = 1+(dp[i+1][j+1] if j+1 < len(nums) else 0) if nums[i] == nums[j] else 0
        result = 0
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                if (dp[0][i] >= i and j-i >= i) or dp[i][j] >= j-i:
                    result += 1
        return result


