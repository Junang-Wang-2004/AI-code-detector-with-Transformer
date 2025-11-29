import heapq

class C1(object):

    def lastStoneWeight(self, a1):
        """
        """
        v1 = [-x for v2 in a1]
        heapq.heapify(v1)
        for v3 in range(len(a1) - 1):
            v2, v4 = (-heapq.heappop(v1), -heapq.heappop(v1))
            heapq.heappush(v1, -abs(v2 - v4))
        return -v1[0]
