import heapq

class C1(object):

    def maxEvents(self, a1):
        """
        """
        a1.sort(reverse=True)
        v1 = []
        v2 = 0
        for v3 in range(1, max(a1, key=lambda x: x[1])[1] + 1):
            while a1 and a1[-1][0] == v3:
                heapq.heappush(v1, a1.pop()[1])
            while v1 and v1[0] == v3 - 1:
                heapq.heappop(v1)
            if not v1:
                continue
            heapq.heappop(v1)
            v2 += 1
        return v2
