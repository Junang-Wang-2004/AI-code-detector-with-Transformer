# Time:  O(m * 2^m)
# Space: O(2^m)

# bitmasks, knapsack dp
class Solution(object):
    def maxHammingDistances(self, nums, m):
        """
        """
        dp = [float("-inf")]*(1<<m)
        for x in nums:
            dp[x] = 0
        for i in range(m):
            new_dp = dp[:]
            for mask in range(1<<m):
                new_dp[mask] = max(new_dp[mask], dp[mask^(1<<i)]+1)
            dp = new_dp
        return [dp[x] for x in nums]


