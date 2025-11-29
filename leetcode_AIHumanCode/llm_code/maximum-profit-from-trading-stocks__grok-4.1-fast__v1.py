class Solution:
    def maximumProfit(self, present, future, budget):
        gains = [0] * (budget + 1)
        def enhance(cost, value, cap):
            for funds in range(cap, cost - 1, -1):
                gains[funds] = max(gains[funds], gains[funds - cost] + value)
        for cost_now, val_future in zip(present, future):
            benefit = val_future - cost_now
            if benefit > 0:
                enhance(cost_now, benefit, budget)
        return gains[budget]
