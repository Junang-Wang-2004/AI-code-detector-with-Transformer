import heapq

class C1(object):

    def maxTransactions(self, a1):
        """
        """
        v1 = []
        v2 = 0
        for v3 in a1:
            heapq.heappush(v1, v3)
            v2 += v3
            if v2 < 0:
                v2 -= heapq.heappop(v1)
        return len(v1)
