import heapq

class C1(object):

    def minRefuelStops(self, a1, a2, a3):
        """
        """
        v1 = []
        a3.append((a1, float('inf')))
        v2 = v3 = 0
        for v4, v5 in a3:
            a2 -= v4 - v3
            while v1 and a2 < 0:
                a2 += -heapq.heappop(v1)
                v2 += 1
            if a2 < 0:
                return -1
            heapq.heappush(v1, -v5)
            v3 = v4
        return v2
