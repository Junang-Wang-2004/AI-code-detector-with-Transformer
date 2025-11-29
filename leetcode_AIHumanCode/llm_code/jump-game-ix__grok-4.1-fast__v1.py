class Solution:
    def maxValue(self, nums):
        n = len(nums)
        if n == 0:
            return []
        pmax = [0] * n
        pmax[0] = nums[0]
        for i in range(1, n):
            pmax[i] = max(pmax[i - 1], nums[i])
        smin = [0.0] * (n + 1)
        smin[n] = float('inf')
        for i in range(n - 1, -1, -1):
            smin[i] = min(smin[i + 1], nums[i])
        res = [0] * n
        for i in range(n - 1, -1, -1):
            if pmax[i] <= smin[i + 1]:
                res[i] = pmax[i]
            else:
                res[i] = res[i + 1]
        return res
