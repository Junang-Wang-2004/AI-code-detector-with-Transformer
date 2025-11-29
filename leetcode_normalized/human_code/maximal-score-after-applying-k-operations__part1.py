import heapq

class C1(object):

    def maxKelements(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2
        v1 = 0
        for v2, v3 in enumerate(a1):
            a1[v2] = -v3
        heapq.heapify(a1)
        for v4 in range(a2):
            if not a1:
                break
            v3 = -heapq.heappop(a1)
            v1 += v3
            v5 = ceil_divide(v3, 3)
            if not v5:
                continue
            heapq.heappush(a1, -v5)
        return v1
