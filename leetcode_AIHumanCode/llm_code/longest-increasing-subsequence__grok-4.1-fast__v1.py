class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        lengths = [1] * n
        max_len = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lengths[i] = max(lengths[i], lengths[j] + 1)
            max_len = max(max_len, lengths[i])
        return max_len
