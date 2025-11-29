import heapq

class C1:

    def mincostToHireWorkers(self, a1, a2, a3):
        v1 = len(a1)
        v2 = list(range(v1))
        v2.sort(key=lambda x: a2[x] / a1[x])
        v3 = []
        v4 = 0
        v5 = float('inf')
        for v6 in v2:
            v7 = a1[v6]
            v8 = a2[v6] / v7
            v4 += v7
            heapq.heappush(v3, -v7)
            while len(v3) > a3:
                v4 -= -heapq.heappop(v3)
            if len(v3) == a3:
                v5 = min(v5, v4 * v8)
        return v5
