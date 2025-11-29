# Time:  O(n * m)
# Space: O(1)
# brute force
class Solution2(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        """
        return sum(x%(k*y) == 0 for x in nums1 for y in nums2)
