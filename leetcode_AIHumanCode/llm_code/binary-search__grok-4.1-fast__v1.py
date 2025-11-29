class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            m = lo + (hi - lo) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                lo = m + 1
            else:
                hi = m - 1
        return -1
