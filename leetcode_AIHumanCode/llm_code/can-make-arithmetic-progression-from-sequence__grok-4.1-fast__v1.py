class Solution:
    def canMakeArithmeticProgression(self, nums):
        nums.sort()
        delta = nums[1] - nums[0]
        for k in range(2, len(nums)):
            if nums[k] - nums[k - 1] != delta:
                return False
        return True
