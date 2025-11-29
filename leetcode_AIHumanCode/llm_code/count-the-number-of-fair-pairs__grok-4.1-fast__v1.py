class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        n = len(nums)
        def first_ge(pos, val):
            l, r = pos, n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= val:
                    r = m - 1
                else:
                    l = m + 1
            return l
        def last_le(pos, val):
            l, r = pos, n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= val:
                    l = m + 1
                else:
                    r = m - 1
            return r
        res = 0
        for i in range(n):
            lo_val = lower - nums[i]
            hi_val = upper - nums[i]
            j_start = first_ge(i + 1, lo_val)
            j_end = last_le(i + 1, hi_val)
            if j_start <= j_end:
                res += j_end - j_start + 1
        return res
