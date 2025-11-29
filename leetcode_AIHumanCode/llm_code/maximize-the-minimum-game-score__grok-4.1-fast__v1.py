class Solution:
    def maxScore(self, points, m):
        maxp = max(points)
        lo = 0
        hi = maxp * m
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            cost = 0
            carry = 0
            n = len(points)
            feasible = True
            for j in range(n):
                val = points[j]
                h = (mid + val - 1) // val
                incr = h - carry
                if incr >= 1:
                    cost += 2 * incr - 1
                    carry = incr - 1
                elif j < n - 1:
                    cost += 1
                    carry = 0
                if cost > m:
                    feasible = False
                    break
            if feasible:
                lo = mid
            else:
                hi = mid - 1
        return lo
