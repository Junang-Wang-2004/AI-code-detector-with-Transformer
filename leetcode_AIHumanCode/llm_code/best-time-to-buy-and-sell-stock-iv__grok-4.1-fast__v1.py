class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1:
            return 0
        if k >= n // 2:
            res = 0
            for i in range(n - 1):
                diff = prices[i + 1] - prices[i]
                if diff > 0:
                    res += diff
            return res
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - p)
                sell[j] = max(sell[j], buy[j] + p)
        return sell[k]
