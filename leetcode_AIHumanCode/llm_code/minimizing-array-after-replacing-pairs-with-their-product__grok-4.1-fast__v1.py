class Solution:
    def minArrayLength(self, nums, k):
        n = len(nums)
        has_zero = False
        for num in nums:
            if num == 0:
                has_zero = True
                break
        if has_zero:
            return 1
        groups = 1
        current = nums[0]
        i = 1
        while i < n:
            if current * nums[i] <= k:
                current *= nums[i]
            else:
                groups += 1
                current = nums[i]
            i += 1
        return groups
