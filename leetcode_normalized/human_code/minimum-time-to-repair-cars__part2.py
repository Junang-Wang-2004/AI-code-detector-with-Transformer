import collections
import heapq

class C1(object):

    def repairCars(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = [(r * 1 ** 2, 1) for v3 in v1.keys()]
        heapq.heapify(v2)
        while a2 > 0:
            v4, v5 = heapq.heappop(v2)
            v3 = v4 // v5 ** 2
            a2 -= v1[v3]
            v5 += 1
            heapq.heappush(v2, (v3 * v5 ** 2, v5))
        return v4
