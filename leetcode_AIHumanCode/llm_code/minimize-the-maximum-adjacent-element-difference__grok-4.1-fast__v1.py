class Solution:
    def minDifference(self, nums):
        n = len(nums)
        max_adj = 0
        for i in range(n - 1):
            if nums[i] != -1 and nums[i + 1
