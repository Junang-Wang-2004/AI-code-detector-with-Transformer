class SegTree:
    def __init__(self, arr, m):
        self.length = len(arr)
        self.m = m
        self.t = [None] * (4 * self.length)
        self._build(1, 0, self.length - 1, arr)

    def _build(self, idx, left, right, arr):
        if left == right:
            r = arr[left] % self.m
            c = [0] * (self.m + 1)
            c[r] = 1
            c[self.m] = r
            self.t[idx] = c
            return
        md = (left + right) // 2
        self._build(2 * idx, left, md, arr)
        self._build(2 * idx + 1, md + 1, right, arr)
        self.t[idx] = self._merge(self.t[2 * idx], self.t[2 * idx + 1])

    def _merge(self, l, r):
        res = l[:]
        lp = l[self.m]
        for i in range(self.m):
            res[(lp * i) % self.m] += r[i]
        res[self.m] = (lp * r[self.m]) % self.m
        return res

    def update_pos(self, idx, left, right, pos, val):
        if left == right:
            r = val % self.m
            c = [0] * (self.m + 1)
            c[r] = 1
            c[self.m] = r
            self.t[idx] = c
            return
        md = (left + right) // 2
        if pos <= md:
            self.update_pos(2 * idx, left, md, pos, val)
        else:
            self.update_pos(2 * idx + 1, md + 1, right, pos, val)
        self.t[idx] = self._merge(self.t[2 * idx], self.t[2 * idx + 1])

    def range_query(self, idx, left, right, ql, qr):
        if qr < left or right < ql:
            return None
        if ql <= left and right <= qr:
            return self.t[idx]
        md = (left + right) // 2
        lq = self.range_query(2 * idx, left, md, ql, qr)
        rq = self.range_query(2 * idx + 1, md + 1, right, ql, qr)
        if lq is None:
            return rq
        if rq is None:
            return lq
        return self._merge(lq, rq)

class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        seg = SegTree(nums, k)
        res = []
        for q in queries:
            i, v, s, x = q
            seg.update_pos(1, 0, n - 1, i, v)
            qr = seg.range_query(1, 0, n - 1, s, n - 1)
            res.append(qr[x])
        return res
