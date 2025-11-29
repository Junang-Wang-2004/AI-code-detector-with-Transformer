import heapq

class C1:

    def shortestPathWithHops(self, a1, a2, a3, a4, a5):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = float('inf')
        v7 = [[v6] * (a5 + 1) for v2 in range(a1)]
        v7[a3][0] = 0
        v8 = [(0, a3, 0)]
        while v8:
            v9, v3, v10 = heapq.heappop(v8)
            if v9 > v7[v3][v10]:
                continue
            if v3 == a4:
                return v9
            for v4, v5 in v1[v3]:
                if v9 + v5 < v7[v4][v10]:
                    v7[v4][v10] = v9 + v5
                    heapq.heappush(v8, (v7[v4][v10], v4, v10))
                if v10 < a5 and v9 < v7[v4][v10 + 1]:
                    v7[v4][v10 + 1] = v9
                    heapq.heappush(v8, (v7[v4][v10 + 1], v4, v10 + 1))
        return -1
