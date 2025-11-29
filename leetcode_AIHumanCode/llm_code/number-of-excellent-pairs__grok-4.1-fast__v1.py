import bisect

class Solution:
    def countExcellentPairs(self, nums, k):
        def ones_count(val):
            res = 0
            while val:
                res += val & 1
                val >>= 1
            return res

        pops = sorted(ones_count(x) for x in nums)
        ans = 0
        m = len(pops)
        for p in pops:
            need = k - p
            pos = bisect.bisect_left(pops, need)
            ans += m - pos
        return ans
