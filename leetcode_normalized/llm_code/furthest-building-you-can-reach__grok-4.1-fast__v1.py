import heapq

class C1(object):

    def furthestBuilding(self, a1, a2, a3):
        v1 = []
        v2 = a2
        v3 = a3
        v4 = len(a1)
        for v5 in range(v4 - 1):
            v6 = a1[v5 + 1] - a1[v5]
            if v6 > 0:
                heapq.heappush(v1, -v6)
                v2 -= v6
                while v2 < 0 and v3 > 0:
                    v2 -= heapq.heappop(v1)
                    v3 -= 1
                if v2 < 0:
                    return v5
        return v4 - 1
