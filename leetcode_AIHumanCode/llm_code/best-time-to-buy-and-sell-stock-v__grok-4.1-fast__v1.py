class Solution:
    def maximumProfit(self, prices, k):
        if not prices or k == 0:
            return 0
        hold = [-float('inf')] * (k + 1)
        cash = [0] + [-float('inf')] * k
        for p in prices:
            for j in range(k, 0, -1):
                hold[j] = max(hold[j], cash[j - 1] - p)
                cash[j] = max(cash[j], hold[j] + p)
        return max(cash)
