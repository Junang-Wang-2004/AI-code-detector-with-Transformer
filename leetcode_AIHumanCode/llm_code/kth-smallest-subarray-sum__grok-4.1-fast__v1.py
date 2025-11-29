class Solution:
    def kthSmallestSubarraySum(self, nums, k):
        def can_achieve(threshold):
            total = 0
            start = 0
            num_sub = 0
            for end in range(len(nums)):
                total += nums[end]
                while total > threshold:
                    total -= nums[start]
                    start += 1
                num_sub += end - start + 1
            return num_sub >= k

        low = min(nums)
        hi = sum(nums)
        while low < hi:
            m = low + (hi - low) // 2
            if can_achieve(m):
                hi = m
            else:
                low = m + 1
        return low
