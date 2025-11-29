import collections
import bisect

class C1(object):

    def __init__(self, a1):
        """
        """
        self.__arr = a1
        self.__inv_idx = collections.defaultdict(list)
        for v1, v2 in enumerate(self.__arr):
            self.__inv_idx[v2].append(v1)
        self.__bound = int(round(len(a1) ** 0.5))
        self.__majorities = [v1 for v1, v3 in self.__inv_idx.items() if len(v3) >= self.__bound]

    def query(self, a1, a2, a3):
        """
        """

        def count(a1, a2, a3, a4):
            return bisect.bisect_right(a1[a2], a4) - bisect.bisect_left(a1[a2], a3)

        def boyer_moore_majority_vote(a1, a2, a3):
            v1, v2 = (a1[a2], 1)
            for v3 in range(a2 + 1, a3 + 1):
                if v1 == a1[v3]:
                    v2 += 1
                else:
                    v2 -= 1
                    if v2 == 0:
                        v1 = a1[v3]
                        v2 = 1
            return v1
        if a2 - a1 + 1 < self.__bound:
            v1 = boyer_moore_majority_vote(self.__arr, a1, a2)
            if count(self.__inv_idx, v1, a1, a2) >= a3:
                return v1
        else:
            for v1 in self.__majorities:
                if count(self.__inv_idx, v1, a1, a2) >= a3:
                    return v1
        return -1
