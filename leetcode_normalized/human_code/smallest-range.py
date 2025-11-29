import heapq

class C1(object):

    def smallestRange(self, a1):
        """
        """
        v1, v2 = (float('inf'), float('-inf'))
        v3 = []
        for v4 in a1:
            v1 = min(v1, v4[0])
            v2 = max(v2, v4[0])
            v5 = iter(v4)
            heapq.heappush(v3, (next(v5, None), v5))
        v6 = (v1, v2)
        while v3:
            v7, v5 = heapq.heappop(v3)
            v7 = next(v5, None)
            if v7 is None:
                break
            heapq.heappush(v3, (v7, v5))
            v1, v2 = (v3[0][0], max(v2, v7))
            if v2 - v1 < v6[1] - v6[0]:
                v6 = (v1, v2)
        return v6
