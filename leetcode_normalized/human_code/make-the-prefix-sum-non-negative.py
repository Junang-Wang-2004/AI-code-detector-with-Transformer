import heapq

class C1(object):

    def makePrefSumNonNegative(self, a1):
        """
        """
        v1 = v2 = 0
        v3 = []
        for v4 in a1:
            heapq.heappush(v3, v4)
            v2 += v4
            if v2 < 0:
                v2 -= heapq.heappop(v3)
                v1 += 1
        return v1
