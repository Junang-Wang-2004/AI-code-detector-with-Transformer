# Time:  O(n)
# Space: O(1)

import bisect


class Solution(object):
    def increasingTriplet(self, nums):
        """
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False

