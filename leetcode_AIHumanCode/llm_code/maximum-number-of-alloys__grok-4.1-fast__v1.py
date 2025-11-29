class Solution:
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        total_stock = sum(stock)
        upper_limit = total_stock + budget + 1
        best = 0
        for recipe in composition:
            l = 0
            r = upper_limit
            while l < r:
                m = (l + r + 1) // 2
                required_cost = 0
                possible = True
                for idx in range(n):
                    demand = m * recipe[idx] - stock[idx]
                    if demand > 0:
                        required_cost += demand * cost[idx]
                        if required_cost > budget:
                            possible = False
                            break
                if possible:
                    l = m
                else:
                    r = m - 1
            best = max(best, l)
        return best
