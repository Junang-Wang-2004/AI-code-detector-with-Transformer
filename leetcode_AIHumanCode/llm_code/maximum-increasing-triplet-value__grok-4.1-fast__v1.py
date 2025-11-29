class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        suf = [0] * n
        suf[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = max(suf[i+1], nums[i])
        vals = sorted(set(nums))
        rk = {vals[i]: i+1 for i in range(len(vals))}
        sz = len(vals)
        tree = [-1] * (sz + 2)
        def upd(idx, v):
            while idx <= sz:
                tree[idx] = max(tree[idx], v)
                idx += idx & -idx
        def qmax(idx):
            res = -1
            while idx > 0:
                res = max(res, tree[idx])
                idx -= idx & -idx
            return res
        res = 0
        for j in range(n):
            if 1 <= j < n-1:
                rid = rk[nums[j]]
                lmx = qmax(rid - 1)
                rmx = suf[j+1]
                if lmx != -1 and rmx > nums[j]:
                    res = max(res, lmx - nums[j] + rmx)
            upd(rk[nums[j]], nums[j])
        return res
