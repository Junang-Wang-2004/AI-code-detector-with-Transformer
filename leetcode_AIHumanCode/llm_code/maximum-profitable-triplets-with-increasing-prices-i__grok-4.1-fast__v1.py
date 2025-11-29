class Solution:
    def maxProfit(self, prices, profits):
        n = len(prices)
        NINF = float('-inf')
        uniq_prices = sorted(set(prices))
        m = len(uniq_prices)
        if m < 3:
            return -1
        rank = {uniq_prices[i]: i + 1 for i in range(m)}
        rev_rank = {uniq_prices[i]: m - i for i in range(m)}

        class MaxFenwick:
            def __init__(self, sz, default):
                self.sz = sz
                self.default = default
                self.t = [default] * (sz + 2)

            def upd(self, i, v):
                while i <= self.sz:
                    self.t[i] = max(self.t[i], v)
                    i += i & -i

            def q(self, i):
                res = self.default
                while i > 0:
                    res = max(res, self.t[i])
                    i -= i & -i
                return res

        ft_fwd = MaxFenwick(m, NINF)
        lmax = [NINF] * n
        for i in range(n):
            r = rank[prices[i]]
            lmax[i] = ft_fwd.q(r - 1) if r > 1 else NINF
            ft_fwd.upd(r, profits[i])

        ft_bwd = MaxFenwick(m, NINF)
        rmax = [NINF] * n
        for i in range(n - 1, -1, -1):
            rr = rev_rank[prices[i]]
            rmax[i] = ft_bwd.q(rr - 1) if rr > 1 else NINF
            ft_bwd.upd(rr, profits[i])

        res = NINF
        for i in range(n):
            res = max(res, lmax[i] + profits[i] + rmax[i])
        return -1 if res == NINF else res
