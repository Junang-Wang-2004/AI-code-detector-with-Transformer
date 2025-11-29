class Solution:
    def increasingTriplet(self, nums):
        n = len(nums)
        lmin = [float('inf')] * n
        mn = float('inf')
        for i in range(n):
            lmin[i] = mn
            mn = min(mn, nums[i])
        rmax = [float('-inf')] * n
        mx = float('-inf')
        for i in range(n - 1, -1, -1):
            rmax[i] = mx
            mx = max(mx, nums[i])
        for i in range(1, n - 1):
            if lmin[i] < nums[i] < rmax[i]:
                return True
        return False
