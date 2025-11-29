import heapq

class C1:

    def shortestDistance(self, a1, a2, a3):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v4, v5 = a3
        v6 = [[float('inf')] * v2 for v7 in range(v1)]
        v8, v9 = a2
        v6[v8][v9] = 0
        v10 = [(0, v8, v9)]
        while v10:
            v11, v12, v13 = heapq.heappop(v10)
            if v12 == v4 and v13 == v5:
                return v11
            if v11 > v6[v12][v13]:
                continue
            for v14, v15 in v3:
                v16, v17 = (v12, v13)
                v18 = 0
                while True:
                    v19 = v16 + v14
                    v20 = v17 + v15
                    if not (0 <= v19 < v1 and 0 <= v20 < v2 and (a1[v19][v20] == 0)):
                        break
                    v16, v17 = (v19, v20)
                    v18 += 1
                v21 = v11 + v18
                if v21 < v6[v16][v17]:
                    v6[v16][v17] = v21
                    heapq.heappush(v10, (v21, v16, v17))
        return -1
