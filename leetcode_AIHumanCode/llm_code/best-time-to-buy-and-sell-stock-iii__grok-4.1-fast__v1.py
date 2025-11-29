class Solution:
    def maxProfit(self, prices):
        buy_one = float('inf')
        sell_one = 0
        buy_two = float('inf')
        sell_two = 0
        for p in prices:
            buy_one = min(buy_one, p)
            sell_one = max(sell_one, p - buy_one)
            buy_two = min(buy_two, p - sell_one)
            sell_two = max(sell_two, p - buy_two)
        return sell_two
