class Solution(object):
    def longestSubarray(self, nums):
        n = len(nums)
        max_run = 0
        max_merge = 0
        prev_run = 0
        has_zero = False
        i = 0
        while i < n:
            z_start = i
            while i < n and nums[i] == 0:
                i += 1
            num_zeros = i - z_start
            if num_zeros > 0:
                has_zero = True
            if i == n:
                break
            r_start = i
            while i < n and nums[i] == 1:
                i += 1
            this_run = i - r_start
            max_run = max(max_run, this_run)
            if prev_run > 0 and num_zeros == 1:
                max_merge = max(max_merge, prev_run + this_run)
            prev_run = this_run
        if not has_zero:
            return max_run - 1
        return max(max_run, max_merge)
