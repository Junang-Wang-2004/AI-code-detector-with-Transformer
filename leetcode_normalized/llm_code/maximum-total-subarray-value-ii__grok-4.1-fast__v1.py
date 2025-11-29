import heapq

class C1:

    def maxTotalValue(self, a1, a2):
        v1 = len(a1)
        if v1 == 0 or a2 == 0:
            return 0
        v2 = [0] * (v1 + 2)
        for v3 in range(2, v1 + 1):
            v2[v3] = v2[v3 // 2] + 1
        v4 = [[0] * v1 for v5 in range(v2[v1] + 1)]
        v6 = [[0] * v1 for v5 in range(v2[v1] + 1)]
        for v3 in range(v1):
            v4[0][v3] = a1[v3]
            v6[0][v3] = a1[v3]
        for v7 in range(1, v2[v1] + 1):
            for v3 in range(v1 - (1 << v7) + 1):
                v4[v7][v3] = min(v4[v7 - 1][v3], v4[v7 - 1][v3 + (1 << v7 - 1)])
                v6[v7][v3] = max(v6[v7 - 1][v3], v6[v7 - 1][v3 + (1 << v7 - 1)])

        def range_min(a1, a2):
            v1 = v2[a2 - a1 + 1]
            return min(v4[v1][a1], v4[v1][a2 - (1 << v1) + 1])

        def range_max(a1, a2):
            v1 = v2[a2 - a1 + 1]
            return max(v6[v1][a1], v6[v1][a2 - (1 << v1) + 1])
        v8 = [(-(range_max(v3, v1 - 1) - range_min(v3, v1 - 1)), v3, v1 - 1) for v3 in range(v1)]
        heapq.heapify(v8)
        v9 = 0
        v10 = 0
        while v10 < a2 and v8:
            v5, v11, v12 = heapq.heappop(v8)
            v9 += range_max(v11, v12) - range_min(v11, v12)
            v10 += 1
            if v11 < v12:
                v13 = -(range_max(v11, v12 - 1) - range_min(v11, v12 - 1))
                heapq.heappush(v8, (v13, v11, v12 - 1))
        return v9
