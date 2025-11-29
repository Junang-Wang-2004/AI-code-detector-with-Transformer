import heapq

class C1:

    def minTimeToReach(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = float('inf')
        v4 = [[v3] * v2 for v5 in range(v1)]
        v4[0][0] = 0
        v6 = []
        heapq.heappush(v6, (0, 0, 0))
        v7 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while v6:
            v8, v9, v10 = heapq.heappop(v6)
            if v8 > v4[v9][v10]:
                continue
            if v9 == v1 - 1 and v10 == v2 - 1:
                return v8
            for v11, v12 in v7:
                v13, v14 = (v9 + v11, v10 + v12)
                if 0 <= v13 < v1 and 0 <= v14 < v2:
                    v15 = max(a1[v13][v14], v8) + 1
                    if v15 < v4[v13][v14]:
                        v4[v13][v14] = v15
                        heapq.heappush(v6, (v15, v13, v14))
        return v4[v1 - 1][v2 - 1]
