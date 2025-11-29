# Time:  O(n^2 * k)
# Space: O(n)
# dp, prefix sum
class Solution2(object):
    def minXor(self, nums, k):
        """
        """
        INF = float("inf")
        prefix = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i]^nums[i]
        dp = [INF]*(len(nums)+1)
        dp[0] = 0
        for l in range(1, k+1):
            for i in reversed(range(l-1, len(dp))):
                dp[i] = INF
                for j in range(l-1, i):
                    dp[i] = min(dp[i], max(dp[j], prefix[i]^prefix[j]))
        return dp[-1]
