import heapq

class C1:

    def findMaximizedCapital(self, a1, a2, a3, a4):
        v1 = []
        v2 = []
        for v3, v4 in zip(a4, a3):
            heapq.heappush(v2, (v3, v4))
        v5 = a2
        for v6 in range(a1):
            while v2 and v2[0][0] <= v5:
                v6, v4 = heapq.heappop(v2)
                heapq.heappush(v1, -v4)
            if v1:
                v5 -= heapq.heappop(v1)
        return v5
