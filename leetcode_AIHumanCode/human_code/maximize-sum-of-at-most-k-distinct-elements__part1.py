# Time:  O(nlogk)
# Space: O(k)

import heapq


# heap, sort
class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        """
        return heapq.nlargest(k, set(nums))


