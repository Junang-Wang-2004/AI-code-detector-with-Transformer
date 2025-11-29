class Solution:
    def buildArray(self, nums):
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[i] = nums[nums[i]]
        return result
