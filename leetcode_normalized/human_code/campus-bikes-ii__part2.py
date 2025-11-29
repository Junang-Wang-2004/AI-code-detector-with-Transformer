import heapq

class C1(object):

    def assignBikes(self, a1, a2):
        """
        """

        def manhattan(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
        v1 = [(0, 0, 0)]
        v2 = set()
        while v1:
            v3, v4, v5 = heapq.heappop(v1)
            if (v4, v5) in v2:
                continue
            v2.add((v4, v5))
            if v4 == len(a1):
                return v3
            for v6 in range(len(a2)):
                if v5 & 1 << v6:
                    continue
                heapq.heappush(v1, (v3 + manhattan(a1[v4], a2[v6]), v4 + 1, v5 | 1 << v6))
