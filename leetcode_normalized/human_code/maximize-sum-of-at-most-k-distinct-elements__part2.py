import heapq

class C1(object):

    def maxKDistinct(self, a1, a2):
        """
        """
        v1 = []
        for v2 in set(a1):
            heapq.heappush(v1, v2)
            if len(v1) == a2 + 1:
                heapq.heappop(v1)
        v3 = []
        while v1:
            v3.append(heapq.heappop(v1))
        v3.reverse()
        return v3
