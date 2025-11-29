class Solution(object):
    def minCost(self, s, cost):
        total = sum(cost)
        n = len(s)
        i = 0
        savings = 0
        while i < n:
            ch = s[i]
            highest = 0
            while i < n and s[i] == ch:
                highest = max(highest, cost[i])
                i += 1
            savings += highest
        return total - savings
