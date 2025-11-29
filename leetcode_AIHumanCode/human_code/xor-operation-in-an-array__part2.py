# Time:  O(n)
# Space: O(1)
import operator
from functools import reduce


class Solution2(object):
    def xorOperation(self, n, start):
        """
        """
        return reduce(operator.xor, (i for i in range(start, start+2*n, 2)))
