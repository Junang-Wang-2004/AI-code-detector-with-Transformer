class Solution:
    def longestMonotonicSubarray(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        ans = 1
        curr_up = 1
        curr_down = 1
        for j in range(1, n):
            if nums[j - 1] < nums[j]:
                curr_up += 1
                curr_down = 1
            elif nums[j - 1] > nums[j]:
                curr_down += 1
                curr_up = 1
            else:
                curr_up = 1
                curr_down = 1
            ans = max(ans, curr_up, curr_down)
        return ans
