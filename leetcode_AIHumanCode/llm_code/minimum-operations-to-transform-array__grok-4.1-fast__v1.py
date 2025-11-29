class Solution(object):
    def minOperations(self, nums1, nums2):
        total = sum(abs(a - b) for a, b in zip(nums1, nums2))
        p = nums2[-1]
        min_d = min(
            0 if min(a, b) <= p <= max(a, b) else min(abs(p - a), abs(p - b))
            for a, b in zip(nums1, nums2)
        )
        return total + 1 + min_d
