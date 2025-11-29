import heapq

class C1:

    def minimumTime(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        if a1[0][1] > 1 and a1[1][0] > 1:
            return -1
        v3 = [[float('inf')] * v2 for v4 in range(v1)]
        v3[0][0] = 0
        v5 = [(0, 0, 0)]
        v6 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while v5:
            v7, v8, v9 = heapq.heappop(v5)
            if v7 > v3[v8][v9]:
                continue
            for v10, v11 in v6:
                v12, v13 = (v8 + v10, v9 + v11)
                if 0 <= v12 < v1 and 0 <= v13 < v2:
                    v14 = 1 if a1[v12][v13] % 2 == v7 % 2 else 0
                    v15 = max(a1[v12][v13] + v14, v7 + 1)
                    if v15 < v3[v12][v13]:
                        v3[v12][v13] = v15
                        heapq.heappush(v5, (v15, v12, v13))
        return v3[v1 - 1][v2 - 1]
