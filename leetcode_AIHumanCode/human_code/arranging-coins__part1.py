# Time:  O(logn)
# Space: O(1)

import math


class Solution(object):
    def arrangeCoins(self, n):
        """
        """
        return int((math.sqrt(8*n+1)-1) / 2)  # sqrt is O(logn) time.


