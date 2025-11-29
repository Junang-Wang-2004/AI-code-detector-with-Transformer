from sortedcontainers import SortedList
import itertools

class C1(object):

    def numberOfPairs(self, a1, a2, a3):
        """
        """
        v1 = SortedList()
        v2 = 0
        for v3, v4 in zip(a1, a2):
            v2 += v1.bisect_right(v3 - v4 + a3)
            v1.add(v3 - v4)
        return v2
