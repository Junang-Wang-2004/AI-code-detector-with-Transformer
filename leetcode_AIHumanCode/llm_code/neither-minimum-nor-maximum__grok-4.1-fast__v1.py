class Solution:
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1
        small = large = nums[0]
        for val in nums:
            if val < small:
                small = val
            elif val > large:
                large = val
        for val in nums:
            if small < val < large:
                return val
        return -1
