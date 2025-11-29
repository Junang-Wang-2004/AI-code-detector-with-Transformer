import heapq

class C1:

    def minCost(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5 * 2))
        v6 = [float('inf')] * a1
        v6[0] = 0
        v7 = [(0, 0)]
        while v7:
            v8, v9 = heapq.heappop(v7)
            if v8 > v6[v9]:
                continue
            for v10, v11 in v1[v9]:
                v12 = v8 + v11
                if v12 < v6[v10]:
                    v6[v10] = v12
                    heapq.heappush(v7, (v12, v10))
        v13 = v6[a1 - 1]
        return v13 if v13 != float('inf') else -1
