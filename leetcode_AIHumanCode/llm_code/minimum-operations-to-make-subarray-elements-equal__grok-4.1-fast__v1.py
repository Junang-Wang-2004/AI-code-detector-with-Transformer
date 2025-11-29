from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums, k):
        lo = SortedList()
        hi = SortedList()
        sum_lo = sum_hi = 0
        res = float('inf')
        for idx, val in enumerate(nums):
            if lo and -lo[0][0] > val:
                lo.add((-val, -idx))
                sum_lo += val
            else:
                hi.add((val, idx))
                sum_hi += val
            while len(lo) > len(hi):
                mv, mi = lo.pop(0)
                sum_lo += mv
                hi.add((-mv, -mi))
                sum_hi -= mv
            while len(hi) > len(lo) + 1:
                mv, mi = hi.pop(0)
                sum_hi -= mv
                lo.add((-mv, -mi))
                sum_lo += mv
            if idx >= k - 1:
                cur = sum_hi - sum_lo
                if k % 2:
                    cur -= hi[0][0]
                res = min(res, cur)
                old_idx = idx - k + 1
                old_val = nums[old_idx]
                lo_key = (-old_val, -old_idx)
                if lo_key in lo:
                    lo.remove(lo_key)
                    sum_lo -= old_val
                else:
                    hi_key = (old_val, old_idx)
                    hi.remove(hi_key)
                    sum_hi -= old_val
                while len(lo) > len(hi):
                    mv, mi = lo.pop(0)
                    sum_lo += mv
                    hi.add((-mv, -mi))
                    sum_hi -= mv
                while len(hi) > len(lo) + 1:
                    mv, mi = hi.pop(0)
                    sum_hi -= mv
                    lo.add((-mv, -mi))
                    sum_lo += mv
        return res
