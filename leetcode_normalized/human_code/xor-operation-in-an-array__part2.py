import operator
from functools import reduce

class C1(object):

    def xorOperation(self, a1, a2):
        """
        """
        return reduce(operator.xor, (i for v1 in range(a2, a2 + 2 * a1, 2)))
