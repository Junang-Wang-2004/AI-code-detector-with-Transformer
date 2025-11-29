class Solution:
    def minimumSum(self, nums):
        n = len(nums)
        BIG = 10**18
        after_min = [BIG] * n
        temp = BIG
        for i in range(n - 1, -1, -1):
            after_min[i] = temp
            temp = min(temp, nums[i])
        res = BIG
        before_min = BIG
        for i in range(n):
            if before_min < nums[i] and nums[i] > after_min[i]:
                res = min(res, before_min + nums[i] + after_min[i])
            before_min = min(before_min, nums[i])
        return res if res < BIG else -1
