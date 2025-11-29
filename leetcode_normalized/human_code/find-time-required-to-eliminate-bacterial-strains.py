import heapq

class C1(object):

    def minEliminationTime(self, a1, a2):
        """
        """
        heapq.heapify(a1)
        for v1 in range(len(a1) - 1):
            heapq.heappush(a1, max(heapq.heappop(a1), heapq.heappop(a1)) + a2)
        return a1[0]
