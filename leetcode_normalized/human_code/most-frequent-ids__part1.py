import collections
import itertools
import heapq

class C1(object):

    def mostFrequentIDs(self, a1, a2):
        """
        """
        v1 = []
        v2 = collections.Counter()
        v3 = []
        for v4, v5 in zip(a1, a2):
            v2[v4] += v5
            heapq.heappush(v3, (-v2[v4], v4))
            while v3 and -v3[0][0] != v2[v3[0][1]]:
                heapq.heappop(v3)
            v1.append(-v3[0][0] if v3 else 0)
        return v1
