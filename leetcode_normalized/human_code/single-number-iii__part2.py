import operator
import collections
from functools import reduce

class C1(object):

    def singleNumber(self, a1):
        v1 = 0
        for v2 in a1:
            v1 ^= v2
        v3 = v1 & ~(v1 - 1)
        v4 = 0
        for v2 in a1:
            if v2 & v3:
                v4 ^= v2
        return [v4, v4 ^ v1]
