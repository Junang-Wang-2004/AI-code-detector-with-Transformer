import heapq

class C1(object):

    def minimumDifference(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1) // 3):
            heapq.heappush(v1, -a1[v2])
        v3 = [0] * (len(a1) // 3 + 1)
        v3[0] = -sum(v1)
        for v2 in range(len(a1) // 3):
            v4 = -heapq.heappushpop(v1, -a1[v2 + len(a1) // 3])
            v3[v2 + 1] = v3[v2] - v4 + a1[v2 + len(a1) // 3]
        v5 = []
        for v2 in reversed(range(len(a1) // 3 * 2, len(a1))):
            heapq.heappush(v5, a1[v2])
        v6 = sum(v5)
        v7 = v3[len(a1) // 3] - v6
        for v2 in reversed(range(len(a1) // 3)):
            v4 = heapq.heappushpop(v5, a1[v2 + len(a1) // 3])
            v6 += -v4 + a1[v2 + len(a1) // 3]
            v7 = min(v7, v3[v2] - v6)
        return v7
