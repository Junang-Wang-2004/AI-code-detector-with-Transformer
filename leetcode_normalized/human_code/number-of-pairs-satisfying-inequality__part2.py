import itertools
import bisect

class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * (a1 + 1)

    def add(self, a1, a2):
        a1 += 1
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.__bit[a1]
            a1 -= a1 & -a1
        return v2

class C2(object):

    def numberOfPairs(self, a1, a2, a3):
        """
        """
        v1 = sorted(set((x - y for v2, v3 in zip(a1, a2))))
        v4 = {v2: i for v5, v2 in enumerate(v1)}
        v6 = 0
        v7 = C1(len(v4))
        for v2, v3 in zip(a1, a2):
            v6 += v7.query(bisect.bisect_right(v1, v2 - v3 + a3) - 1)
            v7.add(v4[v2 - v3], 1)
        return v6
