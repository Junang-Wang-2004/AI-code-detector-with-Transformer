import collections
import heapq

class C1(object):

    def cutOffTree(self, a1):
        """
        """

        def dot(a1, a2):
            return a1[0] * a2[0] + a1[1] * a2[1]

        def minStep(a1, a2):
            v1 = abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])
            v2, v3 = ([a1], [])
            v4 = set()
            while True:
                if not v2:
                    if not v3:
                        return -1
                    v1 += 2
                    v2, v3 = (v3, v2)
                v5, v6 = v2.pop()
                if (v5, v6) == a2:
                    return v1
                if (v5, v6) not in v4:
                    v4.add((v5, v6))
                    for v7, v8 in ((v5 + 1, v6), (v5 - 1, v6), (v5, v6 + 1), (v5, v6 - 1)):
                        if 0 <= v7 < m and 0 <= v8 < n and a1[v7][v8] and ((v7, v8) not in v4):
                            v9 = dot((v7 - v5, v8 - v6), (a2[0] - v5, a2[1] - v6)) > 0
                            (v2 if v9 else v3).append((v7, v8))
            return v1
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        for v4 in range(v1):
            for v5 in range(v2):
                if a1[v4][v5] > 1:
                    heapq.heappush(v3, (a1[v4][v5], (v4, v5)))
        v6 = (0, 0)
        v7 = 0
        while v3:
            v8 = heapq.heappop(v3)
            v9 = minStep(v6, v8[1])
            if v9 < 0:
                return -1
            v7 += v9
            v6 = v8[1]
        return v7
