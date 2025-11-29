import bisect

class Solution:
    def lengthOfLIS(self, nums, k):
        vals = sorted(set(x - 1 for x in nums))
        if not vals:
            return 0
        rank = {v: i for i, v in enumerate(vals)}
        sz = len(vals)
        tree = [0] * (4 * sz)

        def upd(pos, val, nd=1, lo=0, hi=sz - 1):
            if lo == hi:
                tree[nd] = max(tree[nd], val)
                return
            md = (lo + hi) // 2
            if pos <= md:
                upd(pos, val, nd * 2, lo, md)
            else:
                upd(pos, val, nd * 2 + 1, md + 1, hi)
            tree[nd] = max(tree[nd * 2], tree[nd * 2 + 1])

        def qry(ql, qr, nd=1, lo=0, hi=sz - 1):
            if ql > hi or qr < lo:
                return 0
            if ql <= lo and hi <= qr:
                return tree[nd]
            md = (lo + hi) // 2
            return max(qry(ql, qr, nd * 2, lo, md), qry(ql, qr, nd * 2 + 1, md + 1, hi))

        res = 0
        for num in nums:
            xv = num - 1
            if xv not in rank:
                continue
            idx = rank[xv]
            lft = bisect.bisect_left(vals, xv - k)
            prev = qry(lft, idx - 1) if lft < idx else 0
            upd(idx, prev + 1)
            res = max(res, prev + 1)
        return res
