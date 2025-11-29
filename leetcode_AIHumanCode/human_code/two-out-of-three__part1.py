# Time:  O(n)
# Space: O(min(n, r)), r is the range size of nums

import collections


class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        """
        K = 2
        cnt = collections.Counter()
        for nums in nums1, nums2, nums3:
            cnt.update(set(nums))
        return [x for x, c in cnt.items() if c >= K]


