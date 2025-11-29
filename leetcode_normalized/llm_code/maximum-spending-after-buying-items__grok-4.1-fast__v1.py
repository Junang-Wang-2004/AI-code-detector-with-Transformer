import heapq

class C1:

    def maxSpending(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in range(v1):
            heapq.heappush(v3, (-a1[v4][0], v4, 0))
        v5 = 0
        v6 = v1 * v2
        while v3:
            v7, v8, v9 = heapq.heappop(v3)
            v10 = -v7
            v5 += v10 * v6
            v6 -= 1
            if v9 + 1 < v2:
                v11 = a1[v8][v9 + 1]
                heapq.heappush(v3, (-v11, v8, v9 + 1))
        return v5
