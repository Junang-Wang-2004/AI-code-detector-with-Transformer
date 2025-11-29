# Time:  O(n^2)
# Space: O(n)
# dp
class Solution2(object):
    def minimumCost(self, nums, cost, k):
        """
        """
        prefix1 = [0]*(len(nums)+1)
        for i in range(len(nums)):
            prefix1[i+1] = prefix1[i]+nums[i]
        prefix2 = [0]*(len(cost)+1)
        for i in range(len(nums)):
            prefix2[i+1] = prefix2[i]+cost[i]
        dp = [float("inf")]*(len(nums)+1)
        dp[-1] = 0
        for i in reversed(range(len(nums))):
            for j in range(i, len(nums)):
                dp[i] = min(dp[i], prefix1[j+1]*(prefix2[j+1]-prefix2[i])+dp[j+1]+(k*(prefix2[-1]-prefix2[i])))
        return dp[0]
