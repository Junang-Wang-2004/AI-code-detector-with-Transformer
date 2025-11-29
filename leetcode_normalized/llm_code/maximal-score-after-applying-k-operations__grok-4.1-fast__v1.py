import heapq

class C1:

    def maxKelements(self, a1, a2):
        v1 = [-x for v2 in a1]
        heapq.heapify(v1)
        v3 = 0
        v4 = a2
        while v4 > 0:
            if not v1:
                break
            v5 = -heapq.heappop(v1)
            v3 += v5
            v6 = (v5 + 2) // 3
            if v6 > 0:
                heapq.heappush(v1, -v6)
            v4 -= 1
        return v3
