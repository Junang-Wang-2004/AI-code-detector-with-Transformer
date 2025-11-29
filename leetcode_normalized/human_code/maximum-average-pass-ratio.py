import heapq

class C1(object):

    def maxAverageRatio(self, a1, a2):
        """
        """

        def profit(a1, a2):
            return float(a1 + 1) / (a2 + 1) - float(a1) / a2
        v1 = [(-profit(a, b), a, b) for v2, v3 in a1]
        heapq.heapify(v1)
        while a2:
            v4, v2, v3 = heapq.heappop(v1)
            v2, v3 = (v2 + 1, v3 + 1)
            heapq.heappush(v1, (-profit(v2, v3), v2, v3))
            a2 -= 1
        return sum((float(v2) / v3 for v4, v2, v3 in v1)) / len(a1)
