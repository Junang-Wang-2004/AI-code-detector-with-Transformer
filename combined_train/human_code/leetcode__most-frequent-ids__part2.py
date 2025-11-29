import collections
import itertools
from sortedcontainers import SortedList

class C1(object):

    def mostFrequentIDs(self, a1, a2):
        """
        """
        v1 = []
        v2 = collections.Counter()
        v3 = collections.Counter()
        v4 = SortedList()
        for v5, v6 in zip(a1, a2):
            v4.discard((v2[v5], v3[v2[v5]]))
            v3[v2[v5]] -= 1
            if v3[v2[v5]]:
                v4.add((v2[v5], v3[v2[v5]]))
            v2[v5] += v6
            v4.discard((v2[v5], v3[v2[v5]]))
            v3[v2[v5]] += 1
            v4.add((v2[v5], v3[v2[v5]]))
            v1.append(v4[-1][0])
        return v1
