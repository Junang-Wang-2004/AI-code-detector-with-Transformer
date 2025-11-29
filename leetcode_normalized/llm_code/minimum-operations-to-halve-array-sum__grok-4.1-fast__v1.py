import heapq

class C1:

    def halveArray(self, a1):
        v1 = [-val for v2 in a1]
        heapq.heapify(v1)
        v3 = sum(a1) / 2
        v4 = 0.0
        v5 = 0
        while v4 < v3:
            v6 = -heapq.heappop(v1)
            v7 = v6 / 2
            v4 += v7
            if v4 < v3:
                heapq.heappush(v1, -v7)
            v5 += 1
        return v5
