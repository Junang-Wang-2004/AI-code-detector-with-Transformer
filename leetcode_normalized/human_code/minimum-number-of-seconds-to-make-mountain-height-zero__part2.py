import heapq

class C1(object):

    def minNumberOfSeconds(self, a1, a2):
        """
        """
        v1 = [(0 + 1 * t, i, 1) for v2, v3 in enumerate(a2)]
        heapq.heapify(v1)
        for v4 in range(a1):
            v5, v2, v6 = heapq.heappop(v1)
            heapq.heappush(v1, (v5 + (v6 + 1) * a2[v2], v2, v6 + 1))
        return v5
