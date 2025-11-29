class C1:

    def minTimeToReach(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = float('inf')
        v4 = [[v3] * v2 for v5 in range(v1)]
        v4[0][0] = 0
        import heapq
        v6 = []
        heapq.heappush(v6, (0, 0, 0))
        v7 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        v8, v9 = (v1 - 1, v2 - 1)
        while v6:
            v10, v11, v12 = heapq.heappop(v6)
            if v10 > v4[v11][v12]:
                continue
            if v11 == v8 and v12 == v9:
                return v10
            v13 = 1 + (v11 + v12) % 2
            for v14, v15 in v7:
                v16, v17 = (v11 + v14, v12 + v15)
                if 0 <= v16 < v1 and 0 <= v17 < v2:
                    v18 = max(a1[v16][v17], v10) + v13
                    if v18 < v4[v16][v17]:
                        v4[v16][v17] = v18
                        heapq.heappush(v6, (v18, v16, v17))
        return v4[v8][v9]
