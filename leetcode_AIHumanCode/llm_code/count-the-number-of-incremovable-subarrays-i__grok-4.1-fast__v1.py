class Solution(object):
    def incremovableSubarrayCount(self, nums):
        n = len(nums)
        pref_end = 0
        while pref_end + 1 < n and nums[pref_end] < nums[pref_end + 1]:
            pref_end += 1
        if pref_end + 1 == n:
            return n * (n + 1) // 2
        suff_start = n - 1
        while suff_start - 1 >= 0 and nums[suff_start - 1] < nums[suff_start]:
            suff_start -= 1
        total = 0
        right_idx = suff_start
        total += n - right_idx + 1
        for left_end in range(pref_end + 1):
            while right_idx < n and nums[left_end] >= nums[right_idx]:
                right_idx += 1
            total += n - right_idx + 1
        return total
