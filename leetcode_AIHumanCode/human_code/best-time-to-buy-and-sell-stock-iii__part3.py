# Time:  O(n)
# Space: O(n)
class Solution3(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit_from_left, max_profits_from_left = \
            float("inf"), 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit_from_left = max(max_profit_from_left, price - min_price)
            max_profits_from_left.append(max_profit_from_left)

        max_price, max_profit_from_right, max_profits_from_right = 0, 0, []
        for i in reversed(list(range(len(prices)))):
            max_price = max(max_price, prices[i])
            max_profit_from_right = max(max_profit_from_right,
                                        max_price - prices[i])
            max_profits_from_right.insert(0, max_profit_from_right)

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit,
                             max_profits_from_left[i] +
                             max_profits_from_right[i])

        return max_profit

