# Time:  O(1)
# Space: O(1)

import math


class Solution2(object):
    def isPowerOfThree(self, n):
        return n > 0 and (math.log10(n)/math.log10(3)).is_integer()

