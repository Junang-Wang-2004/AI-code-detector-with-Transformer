class Solution(object):
    def longestSubarray(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        ans = 2
        cur = 2
        for j in range(2, n):
            if nums[j] == nums[j - 2] + nums[j - 1]:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 2
        return ans
