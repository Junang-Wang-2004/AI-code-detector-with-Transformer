class Solution:
    def validSubarraySplit(self, nums):
        def compute_gcd(a, b):
            if b == 0:
                return a
            return compute_gcd(b, a % b)

        length = len(nums)
        minimum_parts = [float('inf')] * (length + 1)
        minimum_parts[0] = 0
        for right in range(1, length + 1):
            for left in range(right):
                if compute_gcd(nums[left], nums[right - 1]) > 1:
                    minimum_parts[right] = min(minimum_parts[right], minimum_parts[left] + 1)
        result = minimum_parts[-1]
        return result if result < float('inf') else -1
