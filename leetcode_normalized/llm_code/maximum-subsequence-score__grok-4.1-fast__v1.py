import heapq

class C1:

    def maxScore(self, a1, a2, a3):
        v1 = len(a1)
        v2 = sorted(range(v1), key=lambda i: -a2[i])
        v3 = []
        v4 = 0
        v5 = 0
        for v6 in v2:
            heapq.heappush(v3, a1[v6])
            v4 += a1[v6]
            if len(v3) > a3:
                v4 -= heapq.heappop(v3)
            if len(v3) == a3:
                v5 = max(v5, v4 * a2[v6])
        return v5
