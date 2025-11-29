import heapq

class C1:

    def findCheapestPrice(self, a1, a2, a3, a4, a5):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
        v6 = float('inf')
        v7 = [[v6] * (a5 + 2) for v2 in range(a1)]
        v7[a3][0] = 0
        v8 = [(0, a3, 0)]
        while v8:
            v9, v10, v11 = heapq.heappop(v8)
            if v9 > v7[v10][v11]:
                continue
            if v10 == a4:
                return v9
            for v12, v13 in v1[v10]:
                v14 = v11 + 1
                if v14 > a5 + 1:
                    continue
                v15 = v9 + v13
                if v15 < v7[v12][v14]:
                    v7[v12][v14] = v15
                    heapq.heappush(v8, (v15, v12, v14))
        return -1
