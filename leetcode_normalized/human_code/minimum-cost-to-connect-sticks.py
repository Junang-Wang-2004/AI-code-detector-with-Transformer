import heapq

class C1(object):

    def connectSticks(self, a1):
        """
        """
        heapq.heapify(a1)
        v1 = 0
        while len(a1) > 1:
            v2, v3 = (heapq.heappop(a1), heapq.heappop(a1))
            v1 += v2 + v3
            heapq.heappush(a1, v2 + v3)
        return v1
