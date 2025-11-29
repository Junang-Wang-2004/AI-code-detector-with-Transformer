import heapq
from functools import reduce

class C1(object):

    def getNumberOfBacklogOrders(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = ([], [])
        for v4, v5, v6 in a1:
            if v6 == 0:
                heapq.heappush(v2, [-v4, v5])
            else:
                heapq.heappush(v3, [v4, v5])
            while v3 and v2 and (v3[0][0] <= -v2[0][0]):
                v7 = min(v2[0][1], v3[0][1])
                v8 = heapq.heappop(v2)
                v8[1] -= v7
                if v8[1]:
                    heapq.heappush(v2, v8)
                v8 = heapq.heappop(v3)
                v8[1] -= v7
                if v8[1]:
                    heapq.heappush(v3, v8)
        return reduce(lambda x, y: (x + y) % v1, (v5 for v9, v5 in v2 + v3))
