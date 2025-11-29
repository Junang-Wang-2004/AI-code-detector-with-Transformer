# Time:  O(n * b)
# Space: O(b)
import itertools


# dp
class Solution2(object):
    def maximumProfit(self, present, future, budget):
        """
        """
        dp = [[0]*(budget+1) for _ in range(2)]
        for i, (p, f) in enumerate(zip(present, future)):
            for b in range(budget+1):
                dp[(i+1)%2][b] = max(dp[i%2][b], (dp[i%2][b-p]+(f-p) if b-p >= 0 else 0))
        return dp[len(present)%2][-1]
