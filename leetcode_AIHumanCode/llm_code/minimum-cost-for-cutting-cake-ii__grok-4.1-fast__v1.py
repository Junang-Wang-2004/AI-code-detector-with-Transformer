class Solution:
    def minimumCost(self, m, n, hcuts, vcuts):
        h = sorted(hcuts, reverse=True)
        v = sorted(vcuts, reverse=True)
        total = 0
        p1 = p2 = 0
        rows = cols = 1
        while p1 < len(h) or p2 < len(v):
            if p2 == len(v) or (p1 < len(h) and h[p1] > v[p2]):
                total += h[p1] * cols
                p1 += 1
                rows += 1
            else:
                total += v[p2] * rows
                p2 += 1
                cols += 1
        return total
