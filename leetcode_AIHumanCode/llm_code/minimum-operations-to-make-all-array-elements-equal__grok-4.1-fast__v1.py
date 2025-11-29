class Solution(object):
    def minOperations(self, nums, queries):
        arr = sorted(nums)
        n = len(arr)
        ps = [0]
        for x in arr:
            ps.append(ps[-1] + x)
        def get_pos(a, v):
            l, r = 0, n
            while l < r:
                m = (l + r) // 2
                if a[m] < v:
                    l = m + 1
                else:
                    r = m
            return l
        res = []
        for q in queries:
            p = get_pos(arr, q)
            lcost = q * p - ps[p]
            rcost = ps[n] - ps[p] - q * (n - p)
            res.append(lcost + rcost)
        return res
