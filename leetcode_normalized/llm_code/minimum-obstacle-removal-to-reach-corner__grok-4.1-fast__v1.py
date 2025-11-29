import heapq

class C1:

    def minimumObstacles(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3, v4 = (v1 - 1, v2 - 1)
        v5 = [[float('inf')] * v2 for v6 in range(v1)]
        v5[0][0] = 0
        v7 = [(0, 0, 0)]
        v8 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while v7:
            v9, v10, v11 = heapq.heappop(v7)
            if v9 > v5[v10][v11]:
                continue
            if v10 == v3 and v11 == v4:
                return v9
            for v12, v13 in v8:
                v14 = v10 + v12
                v15 = v11 + v13
                if 0 <= v14 < v1 and 0 <= v15 < v2:
                    v16 = a1[v14][v15]
                    v17 = v9 + v16
                    if v17 < v5[v14][v15]:
                        v5[v14][v15] = v17
                        heapq.heappush(v7, (v17, v14, v15))
        return -1
