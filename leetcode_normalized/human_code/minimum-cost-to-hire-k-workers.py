import itertools
import heapq

class C1(object):

    def mincostToHireWorkers(self, a1, a2, a3):
        """
        """
        v1, v2 = (float('inf'), 0)
        v3 = []
        for v4, v5 in sorted(([float(w) / v5, v5] for v6, v5 in zip(a2, a1))):
            v2 += v5
            heapq.heappush(v3, -v5)
            if len(v3) > a3:
                v2 -= -heapq.heappop(v3)
            if len(v3) == a3:
                v1 = min(v1, v2 * v4)
        return v1
