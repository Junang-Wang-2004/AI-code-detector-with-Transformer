import heapq

class C1(object):

    def furthestBuilding(self, a1, a2, a3):
        """
        """
        v1 = []
        for v2 in range(len(a1) - 1):
            v3 = a1[v2 + 1] - a1[v2]
            if v3 > 0:
                heapq.heappush(v1, v3)
            if len(v1) <= a3:
                continue
            a2 -= heapq.heappop(v1)
            if a2 < 0:
                return v2
        return len(a1) - 1
