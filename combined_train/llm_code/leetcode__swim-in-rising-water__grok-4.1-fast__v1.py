import heapq

class C1:

    def swimInWater(self, a1):
        v1 = len(a1)
        v2 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v3 = [[float('inf')] * v1 for v4 in range(v1)]
        v3[0][0] = a1[0][0]
        v5 = [(a1[0][0], 0, 0)]
        while v5:
            v6, v7, v8 = heapq.heappop(v5)
            if v6 > v3[v7][v8]:
                continue
            if v7 == v1 - 1 and v8 == v1 - 1:
                return v6
            for v9, v10 in v2:
                v11, v12 = (v7 + v9, v8 + v10)
                if 0 <= v11 < v1 and 0 <= v12 < v1:
                    v13 = max(v6, a1[v11][v12])
                    if v13 < v3[v11][v12]:
                        v3[v11][v12] = v13
                        heapq.heappush(v5, (v13, v11, v12))
