# Time:  O(n)
# Space: O(n)
import collections
from functools import reduce


# freq table
class Solution2(object):
    def duplicateNumbersXOR(self, nums):
        """
        """
        return reduce(lambda x, y: x^y, (x for x, c in collections.Counter(nums).items() if c == 2), 0)

