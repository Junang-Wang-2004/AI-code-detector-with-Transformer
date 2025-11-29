import heapq

class C1:

    def makePrefSumNonNegative(self, a1):
        v1 = []
        v2 = 0
        v3 = 0
        for v4 in a1:
            heapq.heappush(v1, v4)
            v2 += v4
            if v2 < 0:
                v2 -= heapq.heappop(v1)
                v3 += 1
        return v3
