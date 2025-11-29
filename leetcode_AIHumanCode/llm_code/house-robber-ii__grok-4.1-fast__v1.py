class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        p2, p1 = 0, nums[0]
        for i in range(1, n - 1):
            cur = max(nums[i] + p2, p1)
            p2 = p1
            p1 = cur
        opt1 = p1
        p2, p1 = 0, nums[1]
        for i in range(2, n):
            cur = max(nums[i] + p2, p1)
            p2 = p1
            p1 = cur
        opt2 = p1
        return max(opt1, opt2)
