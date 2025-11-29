# Time:  O(nlogn)
# Space: O(n)

import itertools


class Solution(object):
    def heightChecker(self, heights):
        """
        """
        return sum(i != j for i, j in zip(heights, sorted(heights)))
