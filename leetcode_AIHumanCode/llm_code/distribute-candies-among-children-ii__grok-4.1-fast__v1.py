class Solution(object):
    def distributeCandies(self, n, limit):
        def unbounded(m):
            return 0 if m < 0 else (m + 1) * (m + 2) // 2
        
        excess = limit + 1
        total = unbounded(n)
        minus = 3 * unbounded(n - excess)
        plus = 3 * unbounded(n - 2 * excess)
        minus2 = unbounded(n - 3 * excess)
        return total - minus + plus - minus2
