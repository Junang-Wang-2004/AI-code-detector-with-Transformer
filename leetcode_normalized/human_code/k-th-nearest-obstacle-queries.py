import heapq

class C1(object):

    def resultsArray(self, a1, a2):
        """
        """
        v1 = []
        v2 = []
        for v3, v4 in a1:
            heapq.heappush(v2, -(abs(v3) + abs(v4)))
            if len(v2) == a2 + 1:
                heapq.heappop(v2)
            v1.append(-v2[0] if len(v2) == a2 else -1)
        return v1
