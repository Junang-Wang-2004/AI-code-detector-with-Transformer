import heapq

class C1(object):

    def minStoneSum(self, a1, a2):
        """
        """
        for v1, v2 in enumerate(a1):
            a1[v1] = -v2
        heapq.heapify(a1)
        for v1 in range(a2):
            heapq.heappush(a1, heapq.heappop(a1) // 2)
        return -sum(a1)
