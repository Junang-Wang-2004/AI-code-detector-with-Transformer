class Solution:
    def longestSubarray(self, nums):
        n = len(nums)
        decreases = [i for i in range(n - 1) if nums[i] > nums[i + 1]]
        bounds = [-1] + decreases + [n - 1]
        ans = 0
        m = len(bounds)
        for i in range(m - 1):
            seg = bounds[i + 1] - bounds[i]
            ans = max(ans, seg)
        for i in range(m - 2):
            combined = (bounds[i + 1] - bounds[i]) + (bounds[i + 2] - bounds[i + 1])
            ans = max(ans, combined)
        return ans
