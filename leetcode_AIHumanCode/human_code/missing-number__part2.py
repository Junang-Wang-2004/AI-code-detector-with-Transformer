# Time:  O(n)
# Space: O(1)

import operator
from functools import reduce


class Solution2(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

