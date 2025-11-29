import heapq

class C1:

    def kthSmallestPrimeFraction(self, a1, a2):
        v1 = len(a1)
        v2 = []
        for v3 in range(v1 - 1):
            heapq.heappush(v2, (a1[v3] / a1[v1 - 1], v3, v1 - 1))
        v4 = 0
        while True:
            v5, v6, v7 = heapq.heappop(v2)
            v4 += 1
            if v4 == a2:
                return [a1[v6], a1[v7]]
            if v7 > v6 + 1:
                heapq.heappush(v2, (a1[v6] / a1[v7 - 1], v6, v7 - 1))
