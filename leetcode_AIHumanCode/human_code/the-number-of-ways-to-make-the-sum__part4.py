from functools import reduce
# Time:  O(n)
# Space: O(n)
# dp
class Solution4(object):
    def numberOfWays(self, n):
        """
        """
        MOD = 10**9+7
        dp = [0]*(n+1)
        dp[0] = 1
        for i in (1, 2, 6):
            for j in range(i, n+1):
                dp[j] += dp[j-i]
        return reduce(lambda x, y: (x+dp[n-4*y])%MOD, (i for i in range(min(n//4, 2)+1)), 0)
