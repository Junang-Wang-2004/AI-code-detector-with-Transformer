class Solution:
    def minimizedMaximum(self, n, quantities):
        l, r = 1, max(quantities)
        while l < r:
            m = (l + r) // 2
            total = 0
            for q in quantities:
                total += (q - 1) // m + 1
            if total <= n:
                r = m
            else:
                l = m + 1
        return l
