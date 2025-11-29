class Solution:
    def minOperations(self, nums):
        n = len(nums)
        ops = 0
        for k in range(n - 2):
            if nums[k] == 0:
                nums[k + 1] = 1 - nums[k + 1]
                nums[k + 2] = 1 - nums[k + 2]
                ops += 1
        if nums[n - 2] == 1 and nums[n - 1] == 1:
            return ops
        return -1
