import heapq

class C1:

    def minCostConnectPoints(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = [False] * v1
        v3 = []
        heapq.heappush(v3, (0, 0))
        v4 = 0
        while v3:
            v5, v6 = heapq.heappop(v3)
            if v2[v6]:
                continue
            v2[v6] = True
            v4 += v5
            v7, v8 = a1[v6]
            for v9 in range(v1):
                if not v2[v9]:
                    v10, v11 = a1[v9]
                    v12 = abs(v7 - v10) + abs(v8 - v11)
                    heapq.heappush(v3, (v12, v9))
        return v4
