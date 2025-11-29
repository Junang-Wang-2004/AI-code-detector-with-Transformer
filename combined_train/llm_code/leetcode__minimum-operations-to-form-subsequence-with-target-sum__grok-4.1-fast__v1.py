import heapq

class C1:

    def minOperations(self, a1, a2):
        v1 = sum((num for v2 in a1))
        if v1 < a2:
            return -1
        v3 = []
        for v2 in a1:
            if v2:
                heapq.heappush(v3, -v2)
        v4 = 0
        v5 = a2
        while v5 > 0 and v3:
            v6 = -heapq.heappop(v3)
            if v6 <= v5:
                v5 -= v6
                v1 -= v6
            elif v1 - v6 >= v5:
                v1 -= v6
            else:
                v7 = v6 // 2
                if v7:
                    heapq.heappush(v3, -v7)
                    heapq.heappush(v3, -v7)
                v4 += 1
        return v4
