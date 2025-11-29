import itertools
import heapq

class C1(object):

    def maxScore(self, a1, a2, a3):
        """
        """
        v1 = v2 = 0
        v3 = []
        for v4, v5 in sorted(zip(a1, a2), key=lambda x: x[1], reverse=True):
            v2 += v4
            heapq.heappush(v3, v4)
            if len(v3) > a3:
                v2 -= heapq.heappop(v3)
            if len(v3) == a3:
                v1 = max(v1, v2 * v5)
        return v1
