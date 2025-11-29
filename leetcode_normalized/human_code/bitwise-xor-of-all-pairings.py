import operator
from functools import reduce

class C1(object):

    def xorAllNums(self, a1, a2):
        """
        """
        return (reduce(operator.xor, a1) if len(a2) % 2 else 0) ^ (reduce(operator.xor, a2) if len(a1) % 2 else 0)
