import heapq

class C1:

    def minimumCost(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = float('inf')
        v7 = [[v6] * (a3 + 1) for v2 in range(a1)]
        v7[0][a3] = 0
        v8 = [(0, 0, a3)]
        v9 = a1 - 1
        while v8:
            v10, v11, v12 = heapq.heappop(v8)
            if v10 > v7[v11][v12]:
                continue
            if v11 == v9:
                return v10
            for v13, v14 in v1[v11]:
                v15 = v10 + v14
                if v15 < v7[v13][v12]:
                    v7[v13][v12] = v15
                    heapq.heappush(v8, (v15, v13, v12))
                if v12 > 0:
                    v16 = v10 + v14 // 2
                    if v16 < v7[v13][v12 - 1]:
                        v7[v13][v12 - 1] = v16
                        heapq.heappush(v8, (v16, v13, v12 - 1))
        return -1
