class Solution:
    def kthSmallestProduct(self, nums1, nums2, k):
        def count_leq(a, b, val):
            res = 0
            nb = len(b)
            for x in a:
                if x == 0:
                    if val >= 0:
                        res += nb
                    continue
                lo = 0
                hi = nb
                if x > 0:
                    maxy = val // x
                    while lo < hi:
                        md = (lo + hi) // 2
                        if b[md] <= maxy:
                            lo = md + 1
                        else:
                            hi = md
                    res += lo
                else:
                    while lo < hi:
                        md = (lo + hi) // 2
                        if b[md] * x <= val:
                            hi = md
                        else:
                            lo = md + 1
                    res += nb - lo
            return res

        prods = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1]
        ]
        l = min(prods)
        r = max(prods)
        while l < r:
            md = l + (r - l) // 2
            if count_leq(nums1, nums2, md) >= k:
                r = md
            else:
                l = md + 1
        return l
