import heapq

class C1(object):

    def kBigIndices(self, a1, a2):
        """
        """
        v1 = [False] * len(a1)
        v2 = []
        for v3 in reversed(range(len(a1))):
            if len(v2) == a2 and a1[v3] > -v2[0]:
                v1[v3] = True
            heapq.heappush(v2, -a1[v3])
            if len(v2) == a2 + 1:
                heapq.heappop(v2)
        v4 = 0
        v5 = []
        for v3 in range(len(a1)):
            if len(v5) == a2 and a1[v3] > -v5[0] and v1[v3]:
                v4 += 1
            heapq.heappush(v5, -a1[v3])
            if len(v5) == a2 + 1:
                heapq.heappop(v5)
        return v4
