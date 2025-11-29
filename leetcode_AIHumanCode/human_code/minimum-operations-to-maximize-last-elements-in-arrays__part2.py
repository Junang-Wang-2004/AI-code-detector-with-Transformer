# Time:  O(n)
# Space: O(1)
import itertools


# simulation
class Solution2(object):
    def minOperations(self, nums1, nums2):
        """
        """
        INF = float("inf")
        def count(mx1, mx2):
            return sum(1 if y <= mx1 and x <= mx2 else INF for x, y in zip(nums1, nums2) if not (x <= mx1 and y <= mx2))

        result = min(count(nums1[-1], nums2[-1]), count(nums2[-1], nums1[-1]))
        return result if result != INF else -1
