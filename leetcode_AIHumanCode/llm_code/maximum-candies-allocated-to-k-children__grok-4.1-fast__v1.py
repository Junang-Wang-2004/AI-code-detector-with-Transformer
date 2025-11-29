class Solution:
    def maximumCandies(self, piles, target):
        def feasible(amt):
            cnt = 0
            for pile in piles:
                cnt += pile // amt
            return cnt >= target
        
        lo = 1
        hi = max(piles)
        while lo < hi:
            md = (lo + hi + 1) // 2
            if feasible(md):
                lo = md
            else:
                hi = md - 1
        return lo
