# Time:  O(n)
# Space: O(1)

import operator
from functools import reduce


class Solution(object):
    def missingNumber(self, nums):
        """
        """
        return reduce(operator.xor, nums,
                      reduce(operator.xor, range(len(nums) + 1)))


