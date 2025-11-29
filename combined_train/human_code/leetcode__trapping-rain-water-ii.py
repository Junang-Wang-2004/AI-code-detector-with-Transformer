from heapq import heappush, heappop

class C1(object):

    def trapRainWater(self, a1):
        """
        """
        v1 = len(a1)
        if not v1:
            return 0
        v2 = len(a1[0])
        if not v2:
            return 0
        v3 = [[False for v4 in range(v2)] for v5 in range(v1)]
        v6 = []
        for v4 in range(v1):
            heappush(v6, [a1[v4][0], v4, 0])
            v3[v4][0] = True
            heappush(v6, [a1[v4][v2 - 1], v4, v2 - 1])
            v3[v4][v2 - 1] = True
        for v5 in range(1, v2 - 1):
            heappush(v6, [a1[0][v5], 0, v5])
            v3[0][v5] = True
            heappush(v6, [a1[v1 - 1][v5], v1 - 1, v5])
            v3[v1 - 1][v5] = True
        v7 = 0
        while v6:
            v8, v4, v5 = heappop(v6)
            for v9, v10 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                v11, v12 = (v4 + v9, v5 + v10)
                if 0 <= v11 < v1 and 0 <= v12 < v2 and (not v3[v11][v12]):
                    v7 += max(0, v8 - a1[v11][v12])
                    heappush(v6, [max(v8, a1[v11][v12]), v11, v12])
                    v3[v11][v12] = True
        return v7
