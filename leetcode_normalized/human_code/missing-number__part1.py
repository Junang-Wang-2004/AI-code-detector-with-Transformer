import operator
from functools import reduce

class C1(object):

    def missingNumber(self, a1):
        """
        """
        return reduce(operator.xor, a1, reduce(operator.xor, range(len(a1) + 1)))
