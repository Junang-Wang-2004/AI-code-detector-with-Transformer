import heapq

class C1(object):

    def convertArray(self, a1):
        """
        """

        def f(a1):
            v1 = 0
            v2 = []
            for v3 in a1:
                if v2 and v3 < -v2[0]:
                    v1 += -heapq.heappop(v2) - v3
                    heapq.heappush(v2, -v3)
                heapq.heappush(v2, -v3)
            return v1
        return min(f(a1), f((x for v1 in reversed(a1))))
