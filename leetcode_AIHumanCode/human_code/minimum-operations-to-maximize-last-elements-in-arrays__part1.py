# Time:  O(n)
# Space: O(1)

import itertools


# simulation
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        """
        cnt = [0]*2
        for x, y in zip(nums1, nums2):
            if not (min(x, y) <= min(nums1[-1], nums2[-1]) and max(x, y) <= max(nums1[-1], nums2[-1])):
                return -1
            if not (x <= nums1[-1] and y <= nums2[-1]):
                cnt[0] += 1
            if not (x <= nums2[-1] and y <= nums1[-1]):
                cnt[1] += 1
        return min(cnt)


