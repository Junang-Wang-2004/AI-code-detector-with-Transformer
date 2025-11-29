class Solution:
    def missingElement(self, nums, k):
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] - m - 1 < k:
                l = m + 1
            else:
                r = m
        return k + l
