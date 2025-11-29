import heapq

class C1(object):

    def maxTwoEvents(self, a1):
        """
        """
        a1.sort()
        v1 = v2 = 0
        v3 = []
        for v4, v5, v6 in a1:
            heapq.heappush(v3, (v5, v6))
            while v3 and v3[0][0] < v4:
                v2 = max(v2, heapq.heappop(v3)[1])
            v1 = max(v1, v2 + v6)
        return v1
