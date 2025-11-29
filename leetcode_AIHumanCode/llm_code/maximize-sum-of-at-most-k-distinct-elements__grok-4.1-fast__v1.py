class Solution:
    def maxKDistinct(self, nums, k):
        unique_vals = list(set(nums))
        unique_vals.sort(reverse=True)
        return unique_vals[:k]
