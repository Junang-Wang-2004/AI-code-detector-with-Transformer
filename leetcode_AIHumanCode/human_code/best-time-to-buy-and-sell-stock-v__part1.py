# Time:  O(n * k)
# Space: O(k)

# dp
class Solution(object):
    def maximumProfit(self, prices, k):
        """
        """
        dp = [0]*(len(prices)+1)
        result = 0
        for i in range(k):
            x, y = float("-inf"), float("-inf")
            new_dp = [float("-inf")]*(len(prices)+1)
            for j in range(i, len(prices)):
                x, y = max(x, dp[j]-prices[j]), max(y, dp[j]+prices[j])
                new_dp[j+1] = max(new_dp[j], x+prices[j], y-prices[j])
            dp = new_dp
            result = max(result, dp[-1])
        return result


