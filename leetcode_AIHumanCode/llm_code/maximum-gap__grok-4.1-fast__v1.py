class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        lo = min(nums)
        hi = max(nums)
        width = max(1, (hi - lo) // (n - 1))
        cnt = (hi - lo) // width + 1
        b_lo = [float('inf')] * cnt
        b_hi = [float('-inf')] * cnt
        for val in nums:
            if val == lo or val == hi:
                continue
            idx = (val - lo) // width
            b_lo[idx] = min(b_lo[idx], val)
            b_hi[idx] = max(b_hi[idx], val)
        res = 0
        prev = lo
        for i in range(cnt):
            if b_lo[i] == float('inf'):
                continue
            res = max(res, b_lo[i] - prev)
            prev = b_hi[i]
        res = max(res, hi - prev)
        return res
