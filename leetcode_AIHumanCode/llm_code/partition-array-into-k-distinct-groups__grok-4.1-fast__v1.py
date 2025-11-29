class Solution:
    def partitionArray(self, nums, k):
        n = len(nums)
        if n % k != 0:
            return False
        target = n // k
        counts = {}
        for val in nums:
            counts[val] = counts.get(val, 0) + 1
        return max(counts.values()) <= target
