import heapq

class C1(object):

    def minimumEffortPath(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = (len(a1) - 1, len(a1[0]) - 1)
        v3 = [[float('inf')] * len(a1[0]) for v4 in range(len(a1))]
        v3[0][0] = 0
        v5 = [(0, 0, 0)]
        v6 = [[False] * len(a1[0]) for v4 in range(len(a1))]
        while v5:
            v7, v8, v9 = heapq.heappop(v5)
            if v6[v8][v9]:
                continue
            v6[v8][v9] = True
            if (v8, v9) == v2:
                return v7
            for v10, v11 in v1:
                v12, v13 = (v8 + v10, v9 + v11)
                if not (0 <= v12 < len(a1) and 0 <= v13 < len(a1[0]) and (not v6[v12][v13])):
                    continue
                v14 = max(v7, abs(a1[v12][v13] - a1[v8][v9]))
                if v14 < v3[v12][v13]:
                    v3[v12][v13] = v14
                    heapq.heappush(v5, (v14, v12, v13))
        return -1
