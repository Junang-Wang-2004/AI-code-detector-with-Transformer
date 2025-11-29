import collections
import random
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        v1, v2 = (10000, 0.001)
        self.__K = int(v1 / v2).bit_length()
        self.__arr = a1
        self.__inv_idx = collections.defaultdict(list)
        for v3, v4 in enumerate(self.__arr):
            self.__inv_idx[v4].append(v3)

    def query(self, a1, a2, a3):
        """
        """

        def count(a1, a2, a3, a4):
            return bisect.bisect_right(a1[a2], a4) - bisect.bisect_left(a1[a2], a3)
        for v1 in range(self.__K):
            v2 = self.__arr[random.randint(a1, a2)]
            if count(self.__inv_idx, v2, a1, a2) >= a3:
                return v2
        return -1
