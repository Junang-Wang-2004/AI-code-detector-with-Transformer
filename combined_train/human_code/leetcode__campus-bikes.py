import heapq

class C1(object):

    def assignBikes(self, a1, a2):
        """
        """

        def manhattan(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
        v1 = [[] for v2 in range(len(a1))]
        for v3 in range(len(a1)):
            for v4 in range(len(a2)):
                v1[v3].append((manhattan(a1[v3], a2[v4]), v3, v4))
            v1[v3].sort(reverse=True)
        v5 = [None] * len(a1)
        v6 = set()
        v7 = []
        for v3 in range(len(a1)):
            heapq.heappush(v7, v1[v3].pop())
        while len(v6) < len(a1):
            v2, v8, v9 = heapq.heappop(v7)
            if v9 not in v6:
                v5[v8] = v9
                v6.add(v9)
            else:
                heapq.heappush(v7, v1[v8].pop())
        return v5
