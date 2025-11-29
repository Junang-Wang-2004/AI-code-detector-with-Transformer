class Solution:
    def maximumLength(self, nums, k):
        freq = {}
        max_freq = 0
        n = len(nums)
        for val in nums:
            freq[val] = freq.get(val, 0) + 1
            if freq[val] > max_freq:
                max_freq = freq[val]
        return min(n, max_freq + k)
