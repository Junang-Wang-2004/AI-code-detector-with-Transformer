import heapq

class C1(object):

    def jobScheduling(self, a1, a2, a3):
        """
        """
        v1 = list(zip(a1, a2, a3))
        heapq.heapify(v1)
        v2 = 0
        while v1:
            v3, v4, v5 = heapq.heappop(v1)
            if v3 < v4:
                heapq.heappush(v1, (v4, v3, v2 + v5))
            else:
                v2 = max(v2, v5)
        return v2
