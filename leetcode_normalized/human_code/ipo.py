import heapq

class C1(object):

    def findMaximizedCapital(self, a1, a2, a3, a4):
        """
        """
        v1 = []
        v2 = sorted(zip(a4, a3), reverse=True)
        for v3 in range(a1):
            while v2 and v2[-1][0] <= a2:
                heapq.heappush(v1, -v2.pop()[1])
            if v1:
                a2 -= heapq.heappop(v1)
        return a2
