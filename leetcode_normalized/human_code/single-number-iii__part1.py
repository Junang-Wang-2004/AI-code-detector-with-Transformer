import operator
import collections
from functools import reduce

class C1(object):

    def singleNumber(self, a1):
        v1 = reduce(operator.xor, a1)
        v2 = v1 & -v1
        v3 = [0, 0]
        for v4 in a1:
            v3[bool(v4 & v2)] ^= v4
        return v3
