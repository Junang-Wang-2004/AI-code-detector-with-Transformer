# Time:  O(m * n)
# Space: O(1)

import itertools


class Solution(object):
    def maximumWealth(self, accounts):
        """
        """
        return max(map(sum, accounts))
