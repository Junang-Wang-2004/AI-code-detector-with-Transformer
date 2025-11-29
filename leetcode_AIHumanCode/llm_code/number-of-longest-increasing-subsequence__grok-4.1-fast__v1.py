class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        lengths = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lengths[i] = max(lengths[i], lengths[j] + 1)
        max_length = max(lengths)
        counts = [1 if lengths[k] == 1 else 0 for k in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
        return sum(counts[i] for i in range(n) if lengths[i] == max_length)
