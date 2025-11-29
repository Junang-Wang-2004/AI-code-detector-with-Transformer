# Time:  O(n^2)
# Space: O(n)
# dp
class Solution3(object):
    def minimumCoins(self, prices):
        """
        """
        dp = [float("inf")]*(len(prices)+1)
        dp[0] = 0
        for i in range(len(prices)):
            for j in range(i//2, i+1):
                dp[i+1] = min(dp[i+1], dp[j]+prices[j])
        return dp[-1]
