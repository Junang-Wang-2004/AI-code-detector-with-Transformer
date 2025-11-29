class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        n = len(nums)
        nums.sort()
        mid_pos = n // 2
        ops = 0
        for idx in range(mid_pos + 1):
            if nums[idx] > k:
                ops += nums[idx] - k
        for idx in range(mid_pos, n):
            if nums[idx] < k:
                ops += k - nums[idx]
        return ops
