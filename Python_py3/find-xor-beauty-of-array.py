# Time:  O(n)
# Space: O(1)

import operator
from functools import reduce


# bit manipulation, math
class Solution(object):
    def xorBeauty(self, nums):
        """
        """
        return reduce(operator.xor, nums)
