# Time:  O(n * b)
# Space: O(b)

import itertools


# dp, optimized from solution2
class Solution(object):
    def maximumProfit(self, present, future, budget):
        """
        """
        dp = [0]*(budget+1)
        for i, (p, f) in enumerate(zip(present, future)):
            if f-p < 0:
                continue
            for b in reversed(range(p, budget+1)):
                dp[b] = max(dp[b], dp[b-p]+(f-p))
        return dp[-1]


