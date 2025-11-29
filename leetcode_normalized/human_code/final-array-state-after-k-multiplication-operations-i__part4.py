import heapq

class C1(object):

    def getFinalState(self, a1, a2, a3):
        """
        """
        if a3 == 1:
            return a1
        v1 = [(x, i) for v2, v3 in enumerate(a1)]
        heapq.heapify(v1)
        for v4 in range(a2):
            v2 = heapq.heappop(v1)[1]
            a1[v2] *= a3
            heapq.heappush(v1, (a1[v2], v2))
        return a1
