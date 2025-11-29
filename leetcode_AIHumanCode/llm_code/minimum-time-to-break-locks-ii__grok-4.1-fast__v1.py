class Solution:
    def findMinimumTime(self, strength):
        n = len(strength)
        vals = sorted(strength, reverse=True)
        res = 0
        for i in range(n):
            denom = n - i
            res += (vals[i] + denom - 1) // denom
        return res
