class Solution:
    def moveZeroes(self, nums):
        cur = 0
        for val in nums:
            if val != 0:
                nums[cur] = val
                cur += 1
        for k in range(cur, len(nums)):
            nums[k] = 0
