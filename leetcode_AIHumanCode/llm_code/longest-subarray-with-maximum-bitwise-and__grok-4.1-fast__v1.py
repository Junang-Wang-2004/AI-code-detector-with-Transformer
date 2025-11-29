class Solution(object):
    def longestSubarray(self, nums):
        if not nums:
            return 0
        best = 1
        peak = nums[0]
        streak = 1
        for val in nums[1:]:
            if val > peak:
                peak = val
                streak = 1
            elif val == peak:
                streak += 1
            else:
                streak = 0
            best = max(best, streak)
        return best
