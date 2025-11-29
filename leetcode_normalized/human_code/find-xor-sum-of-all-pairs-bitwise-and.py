import operator
from functools import reduce

class C1(object):

    def getXORSum(self, a1, a2):
        """
        """
        return reduce(operator.xor, a1) & reduce(operator.xor, a2)
