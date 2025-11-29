# Time:  O(k * n)
# Space: O(k)
class Solution2(object):
    def maxProfit(self, prices):
        """
        """
        def maxAtMostKPairsProfit(prices, k):
            max_buy = [float("-inf") for _ in range(k + 1)]
            max_sell = [0 for _ in range(k + 1)]
            for i in range(len(prices)):
                for j in range(1, k + 1):
                    max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                    max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
            return max_sell[k]

        return maxAtMostKPairsProfit(prices, 2)


