import heapq

class C1:

    def rangeSum(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7
        v2 = []
        for v3 in range(a2):
            heapq.heappush(v2, (a1[v3], v3))
        v4 = 0
        for v5 in range(a4):
            v6, v7 = heapq.heappop(v2)
            if v5 + 1 >= a3:
                v4 = (v4 + v6) % v1
            if v7 < a2 - 1:
                heapq.heappush(v2, (v6 + a1[v7 + 1], v7 + 1))
        return v4
