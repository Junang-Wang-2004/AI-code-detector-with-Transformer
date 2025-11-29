import operator
from functools import reduce

class C1(object):

    def subtractProductAndSum(self, a1):
        """
        """
        v1 = list(map(int, str(a1)))
        return reduce(operator.mul, v1) - sum(v1)
