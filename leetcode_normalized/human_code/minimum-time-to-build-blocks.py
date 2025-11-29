import heapq

class C1(object):

    def minBuildTime(self, a1, a2):
        """
        """
        heapq.heapify(a1)
        while len(a1) != 1:
            v1, v2 = (heapq.heappop(a1), heapq.heappop(a1))
            heapq.heappush(a1, v2 + a2)
        return heapq.heappop(a1)
