class Solution:
    def longestBalanced(self, nums):
        if not nums:
            return 0
        N = len(nums) + 1
        class SegTree:
            def __init__(self, sz):
                self.sz = sz
                self.tmin = [0] * (4 * sz)
                self.tmax = [0] * (4 * sz)
                self.lz = [0] * (4 * sz)

            def _prop(self, nd, l, r):
                if self.lz[nd]:
                    self.tmin[nd] += self.lz[nd]
                    self.tmax[nd] += self.lz[nd]
                    if l != r:
                        self.lz[2 * nd] += self.lz[nd]
                        self.lz[2 * nd + 1] += self.lz[nd]
                    self.lz[nd] = 0

            def _merge(self, nd):
                self.tmin[nd] = min(self.tmin[2 * nd], self.tmin[2 * nd + 1])
                self.tmax[nd] = max(self.tmax[2 * nd], self.tmax[2 * nd + 1])

            def upd_range(self, ql, qr, val, nd=1, l=0, r=None):
                if r is None:
                    r = self.sz - 1
                self._prop(nd, l, r)
                if ql > qr or ql > r or qr < l:
                    return
                if ql <= l and r <= qr:
                    self.lz[nd] += val
                    self._prop(nd, l, r)
                    return
                m = (l + r) // 2
                self.upd_range(ql, qr, val, 2 * nd, l, m)
                self.upd_range(ql, qr, val, 2 * nd + 1, m + 1, r)
                self._merge(nd)

            def get_left(self, target, nd=1, l=0, r=None):
                if r is None:
                    r = self.sz - 1
                self._prop(nd, l, r)
                if self.tmin[nd] > target or self.tmax[nd] < target:
                    return float('inf')
                if l == r:
                    return l if self.tmin[nd] == target else float('inf')
                m = (l + r) // 2
                res_l = self.get_left(target, 2 * nd, l, m)
                if res_l < float('inf'):
                    return res_l
                return self.get_left(target, 2 * nd + 1, m + 1, r)

        tr = SegTree(N)
        last_pos = {}
        bal = 0
        res = 0
        for i in range(len(nums)):
            val = nums[i]
            d = 1 if val % 2 else -1
            if val in last_pos:
                p = last_pos[val]
                tr.upd_range(p, N - 1, -d)
                bal -= d
            bal += d
            p = i + 1
            last_pos[val] = p
            tr.upd_range(p, N - 1, d)
            j = tr.get_left(bal)
            if j < float('inf'):
                res = max(res, p - j)
        return res
