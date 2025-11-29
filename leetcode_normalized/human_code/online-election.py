import collections
import itertools
import bisect

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        v1 = -1
        self.__lookup, v2 = ([], collections.defaultdict(int))
        for v3, v4 in zip(a2, a1):
            v2[v4] += 1
            if v2[v4] >= v2[v1]:
                v1 = v4
                self.__lookup.append((v3, v1))

    def q(self, a1):
        """
        """
        return self.__lookup[bisect.bisect(self.__lookup, (a1, float('inf'))) - 1][1]
