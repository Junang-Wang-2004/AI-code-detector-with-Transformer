import operator
from functools import reduce

class C1(object):
    """
    """

    def singleNumber(self, a1):
        return reduce(operator.xor, a1)
