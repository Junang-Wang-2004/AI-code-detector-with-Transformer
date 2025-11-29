class Solution:
    def maxScore(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        sufmax = [0] * n
        sufmax[n-1] = nums[n-1]
        for pos in range(n-2, -1, -1):
            sufmax[pos] = max(nums[pos], sufmax[pos+1])
        return sum(sufmax[1:])
