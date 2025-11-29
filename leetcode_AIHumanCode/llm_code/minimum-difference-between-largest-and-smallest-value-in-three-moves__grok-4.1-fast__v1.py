class Solution:
    def minDifference(self, nums):
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        ans = float('inf')
        for i in range(4):
            ans = min(ans, nums[n - 4 + i] - nums[i])
        return ans
