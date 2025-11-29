# Time:  O(n)
# Space: O(1)

import operator
import collections
from functools import reduce


class Solution3(object):
    def singleNumber(self, nums):
        """
        """
        return [x[0] for x in sorted(list(collections.Counter(nums).items()), key=lambda i: i[1], reverse=False)[:2]]

