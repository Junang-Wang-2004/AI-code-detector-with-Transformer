import heapq

class C1:

    def minRefuelStops(self, a1, a2, a3):
        v1 = []
        v2 = a2
        v3 = 0
        v4 = 0
        v5 = len(a3)
        while v2 < a1:
            while v3 < v5 and a3[v3][0] <= v2:
                heapq.heappush(v1, -a3[v3][1])
                v3 += 1
            if not v1:
                return -1
            v2 += -heapq.heappop(v1)
            v4 += 1
        return v4
