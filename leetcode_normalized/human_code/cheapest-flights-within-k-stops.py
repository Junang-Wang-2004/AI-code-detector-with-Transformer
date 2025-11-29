import collections
import heapq

class C1(object):

    def findCheapestPrice(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3, v4 in a2:
            v1[v2].append((v3, v4))
        v5 = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        v5[a3][a5 + 1] = 0
        v6 = [(0, a3, a5 + 1)]
        while v6:
            v7, v2, v8 = heapq.heappop(v6)
            if v8 < 0 or v5[v2][v8] < v7:
                continue
            if v2 == a4:
                return v7
            for v3, v4 in v1[v2]:
                if v7 + v4 < v5[v3][v8 - 1]:
                    v5[v3][v8 - 1] = v7 + v4
                    heapq.heappush(v6, (v7 + v4, v3, v8 - 1))
        return -1
