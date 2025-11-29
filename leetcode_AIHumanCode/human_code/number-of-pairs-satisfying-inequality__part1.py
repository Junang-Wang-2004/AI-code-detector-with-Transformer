# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList
import itertools


# sorted list, binary search
class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        """
        sl = SortedList()
        result = 0
        for x, y in zip(nums1, nums2):
            result += sl.bisect_right((x-y)+diff)
            sl.add(x-y)
        return result

    
