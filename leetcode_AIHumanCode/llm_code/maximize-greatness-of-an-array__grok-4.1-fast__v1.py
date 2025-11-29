class Solution:
    def maximizeGreatness(self, nums):
        nums.sort()
        n = len(nums)
        if n <= 1:
            return 0
        max_freq = 1
        curr_freq = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                curr_freq += 1
            else:
                max_freq = max(max_freq, curr_freq)
                curr_freq = 1
        max_freq = max(max_freq, curr_freq)
        return n - max_freq
