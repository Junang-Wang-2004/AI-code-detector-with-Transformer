import math

class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        big = max(cost1, cost2)
        small = min(cost1, cost2)
        g = math.gcd(big, small)
        lcm_val = big // g * small
        period = lcm_val // small
        max_num = total // big + 1
        lim = min(max_num, period)
        res = 0
        for k in range(lim):
            leftover = total - k * big
            cnt = leftover // small + 1
            groups = (cnt + period - 1) // period
            fst = cnt
            lst = cnt - (groups - 1) * period
            res += groups * (fst + lst) // 2
        return res
