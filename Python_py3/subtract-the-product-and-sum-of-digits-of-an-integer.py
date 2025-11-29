# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        """
        product, total = 1, 0
        while n:
            n, r = divmod(n, 10)
            product *= r
            total += r
        return product-total


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
