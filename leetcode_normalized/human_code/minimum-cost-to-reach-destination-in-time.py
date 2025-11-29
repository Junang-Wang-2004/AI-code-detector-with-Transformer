import collections
import heapq

class C1(object):

    def minCost(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(len(a3))]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = collections.defaultdict(lambda: float('inf'))
        v6[0] = 0
        v7 = [(a3[0], 0, 0)]
        while v7:
            v8, v3, v5 = heapq.heappop(v7)
            if v5 > a1:
                continue
            if v3 == len(a3) - 1:
                return v8
            for v4, v9 in v1[v3]:
                if v5 + v9 < v6[v4]:
                    v6[v4] = v5 + v9
                    heapq.heappush(v7, (v8 + a3[v4], v4, v5 + v9))
        return -1
