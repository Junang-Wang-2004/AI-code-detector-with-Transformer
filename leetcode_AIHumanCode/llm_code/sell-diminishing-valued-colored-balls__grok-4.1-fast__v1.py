class Solution:
    def maxProfit(self, inventory, orders):
        MOD = 10**9 + 7
        def feasible(pr):
            res = 0
            for val in inventory:
                if val >= pr:
                    res += val - pr + 1
            return res <= orders
        maxv = max(inventory) if inventory else 0
        l, r = 1, maxv + 1
        while l < r:
            m = (l + r) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
        pivot = l
        profit_high = 0
        cnt_high = 0
        for qty in inventory:
            if qty >= pivot:
                num = qty - pivot + 1
                cnt_high += num
                profit_high += num * pivot + num * (num - 1) // 2
        leftover = orders - cnt_high
        return (profit_high + leftover * (pivot - 1)) % MOD
