# Time:  O(logn)
# Space: O(logn)
import operator
from functools import reduce


class Solution2(object):
    def subtractProductAndSum(self, n):
        """
        """
        A = list(map(int, str(n)))
        return reduce(operator.mul, A) - sum(A)
