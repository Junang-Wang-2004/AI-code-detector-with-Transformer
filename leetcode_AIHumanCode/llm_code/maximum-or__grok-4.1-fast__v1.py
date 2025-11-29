class Solution:
    def maximumOr(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] | nums[i]
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = nums[i] | suffix[i + 1]
        maximum = 0
        for i in range(n):
            current = prefix[i] | (nums[i] << k) | suffix[i + 1]
            if current > maximum:
                maximum = current
        return maximum
