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
        self.__bucket_size = int(round(len(a1) ** 0.5))
        self.__bucket_majorities = []
        for v3 in range(0, len(self.__arr), self.__bucket_size):
            v4 = min(v3 + self.__bucket_size - 1, len(self.__arr) - 1)
            self.__bucket_majorities.append(self.__boyer_moore_majority_vote(self.__arr, v3, v4))

    def query(self, a1, a2, a3):
        """
        """

        def count(a1, a2, a3, a4):
            return bisect.bisect_right(a1[a2], a4) - bisect.bisect_left(a1[a2], a3)
        v1, v2 = (a1 // self.__bucket_size, a2 // self.__bucket_size)
        if v1 == v2:
            v3 = self.__boyer_moore_majority_vote(self.__arr, a1, a2)
            if count(self.__inv_idx, v3, a1, a2) >= a3:
                return v3
            return -1
        else:
            v3 = self.__boyer_moore_majority_vote(self.__arr, a1, (v1 + 1) * self.__bucket_size - 1)
            if count(self.__inv_idx, v3, a1, a2) >= a3:
                return v3
            v3 = self.__boyer_moore_majority_vote(self.__arr, v2 * self.__bucket_size, a2)
            if count(self.__inv_idx, v3, a1, a2) >= a3:
                return v3
            for v4 in range(v1 + 1, v2):
                if count(self.__inv_idx, self.__bucket_majorities[v4], a1, a2) >= a3:
                    return self.__bucket_majorities[v4]
            return -1

    def __boyer_moore_majority_vote(self, a1, a2, a3):
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
