class Solution:
    def maxTastiness(self, price, tastiness, maxAmount, maxCoupons):
        table = [[0] * (maxCoupons + 1) for _ in range(maxAmount + 1)]
        n = len(price)
        for idx in range(n):
            cost = price[idx]
            value = tastiness[idx]
            reduced_cost = cost // 2
            for budget in range(maxAmount, -1, -1):
                for coupons in range(maxCoupons, -1, -1):
                    if budget >= cost:
                        table[budget][coupons] = max(table[budget][coupons], value + table[budget - cost][coupons])
                    if coupons > 0 and budget >= reduced_cost:
                        table[budget][coupons] = max(table[budget][coupons], value + table[budget - reduced_cost][coupons - 1])
        return table[maxAmount][maxCoupons]
