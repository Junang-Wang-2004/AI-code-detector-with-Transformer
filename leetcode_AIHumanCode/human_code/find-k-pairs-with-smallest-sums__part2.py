# Time:  O(k * log(min(n, m, k))), where n is the size of num1, and m is the size of num2.
# Space: O(min(n, m, k))

from heapq import heappush, heappop

class Solution2(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        """
        return nsmallest(k, product(nums1, nums2), key=sum)
