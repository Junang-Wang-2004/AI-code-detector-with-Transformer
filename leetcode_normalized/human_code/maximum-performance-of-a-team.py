import itertools
import heapq

class C1(object):

    def maxPerformance(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (0, 0)
        v4 = []
        for v5, v6 in sorted(zip(a3, a2), reverse=True):
            v3 += v6
            heapq.heappush(v4, v6)
            if len(v4) > a4:
                v3 -= heapq.heappop(v4)
            v2 = max(v2, v3 * v5)
        return v2 % v1
