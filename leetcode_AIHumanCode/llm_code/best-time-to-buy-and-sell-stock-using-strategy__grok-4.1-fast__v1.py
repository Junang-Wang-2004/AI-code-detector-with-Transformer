class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        half = k // 2
        full = 0
        modified = 0
        for i in range(n):
            full += prices[i] * strategy[i]
            if i < k:
                if i >= half:
                    modified += prices[i]
            else:
                modified += prices[i] * strategy[i]
        ans = max(full, modified)
        for i in range(k, n):
            modified += prices[i - k] * strategy[i - k]
            modified += prices[i] - prices[i - half]
            modified -= prices[i] * strategy[i]
            ans = max(ans, modified)
        return ans
