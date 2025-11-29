import heapq

class C1(object):

    def pickGifts(self, a1, a2):
        """
        """
        for v1, v2 in enumerate(a1):
            a1[v1] = -v2
        heapq.heapify(a1)
        for v3 in range(a2):
            v2 = heapq.heappop(a1)
            heapq.heappush(a1, -int((-v2) ** 0.5))
        return -sum(a1)
