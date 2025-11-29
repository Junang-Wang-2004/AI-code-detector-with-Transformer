class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        if n == 0:
            return []
        res = [1] * n
        for i in range(n - 2, -1, -1):
            res[i] = res[i + 1] * nums[i + 1]
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]
        return res
