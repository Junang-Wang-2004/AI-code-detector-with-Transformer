import collections
import heapq

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6, v7 = (0, a1 - 1)
        v8 = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        v8[v6][a3] = 0
        v9 = [(0, v6, a3)]
        while v9:
            v10, v3, v11 = heapq.heappop(v9)
            if v8[v3][v11] < v10:
                continue
            if v3 == v7:
                return v10
            for v4, v5 in v1[v3]:
                if v10 + v5 < v8[v4][v11]:
                    v8[v4][v11] = v10 + v5
                    heapq.heappush(v9, (v10 + v5, v4, v11))
                if v11 > 0 and v10 + v5 // 2 < v8[v4][v11 - 1]:
                    v8[v4][v11 - 1] = v10 + v5 // 2
                    heapq.heappush(v9, (v10 + v5 // 2, v4, v11 - 1))
        return -1
