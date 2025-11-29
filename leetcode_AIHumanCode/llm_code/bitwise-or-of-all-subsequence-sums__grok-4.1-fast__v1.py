class Solution:
    def subsequenceSumOr(self, nums):
        total_or = 0
        current_sum = 0
        idx = 0
        n = len(nums)
        while idx < n:
            current_sum += nums[idx]
            total_or |= current_sum | nums[idx]
            idx += 1
        return total_or
