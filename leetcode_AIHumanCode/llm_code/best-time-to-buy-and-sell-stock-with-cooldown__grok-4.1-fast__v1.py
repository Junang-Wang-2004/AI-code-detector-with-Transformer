class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        prev_hold = -prices[0]
        prev_sold = 0
        prev_rest = 0
        for p in prices[1:]:
            curr_hold = max(prev_hold, prev_rest - p)
            curr_sold = prev_hold + p
            curr_rest = max(prev_rest, prev_sold)
            prev_hold = curr_hold
            prev_sold = curr_sold
            prev_rest = curr_rest
        return max(prev_rest, prev_sold)
