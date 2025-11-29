import heapq

class C1:

    def leftmostBuildingQueries(self, a1, a2):
        v1 = len(a1)
        v2 = [-1] * len(a2)
        v3 = [[] for v4 in range(v1)]
        for v5, (v6, v7) in enumerate(a2):
            v8, v9 = (min(v6, v7), max(v6, v7))
            if a1[v8] < a1[v9] or v8 == v9:
                v2[v5] = v9
            else:
                v3[v9].append((a1[v8], v5))
        v10 = []
        for v11 in range(v1):
            for v12, v5 in v3[v11]:
                heapq.heappush(v10, (v12, v5))
            while v10 and v10[0][0] < a1[v11]:
                v4, v5 = heapq.heappop(v10)
                v2[v5] = v11
        return v2
