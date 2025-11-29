class Solution(object):
    def numMovesStones(self, a, b, c):
        lo = min(a, b, c)
        hi = max(a, b, c)
        md = a + b + c - lo - hi
        res_max = hi - lo - 2
        if hi - lo == 2:
            return [0, res_max]
        if md - lo <= 2 or hi - md <= 2:
            return [1, res_max]
        return [2, res_max]
