class Solution(object):
    def minEnd(self, n, x):
        res = x
        nn = n - 1
        free_powers = [1 << i for i in range(64) if (x & (1 << i)) == 0]
        idx = 0
        while nn > 0 and idx < len(free_powers):
            if nn & 1:
                res |= free_powers[idx]
            nn >>= 1
            idx += 1
        return res
