import itertools
import re

class C1(object):

    def canWin(self, a1):
        v1, v2 = ([0], 0)
        for v3 in map(len, re.split('-+', a1)):
            while len(v1) <= v3:
                v1 += (min(set(range(v3)) - {x ^ y for v4, v5 in zip(v1[:len(v1) / 2], v1[-2:-len(v1) / 2 - 2:-1])}),)
            v2 ^= v1[v3]
        return v2 > 0
