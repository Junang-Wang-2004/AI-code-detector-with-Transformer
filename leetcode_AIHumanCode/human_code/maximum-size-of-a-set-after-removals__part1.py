# Time:  O(n)
# Space: O(n)

# math, hash table, greedy
class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        """
        lookup1, lookup2 = set(nums1), set(nums2)
        n, c = len(nums1), len(lookup1&lookup2)
        d1, d2 = min(len(lookup1)-c, n//2), min(len(lookup2)-c, n//2)
        return min(n, d1+d2+c)


