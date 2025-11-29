import heapq

class C1(object):

    def maxPoints(self, a1, a2):
        """
        """
        v1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        v2 = [(a1[0][0], 0, 0)]
        v3 = [[False] * len(a1[0]) for v4 in range(len(a1))]
        v3[0][0] = True
        v5 = 0
        v6 = collections.Counter()
        while v2:
            v7, v8, v9 = heapq.heappop(v2)
            v5 = max(v5, v7)
            v6[v5] += 1
            for v10, v11 in v1:
                v12, v13 = (v8 + v10, v9 + v11)
                if not (0 <= v12 < len(a1) and 0 <= v13 < len(a1[0]) and (not v3[v12][v13])):
                    continue
                v3[v12][v13] = True
                heapq.heappush(v2, (a1[v12][v13], v12, v13))
        v14 = sorted(v6.keys())
        v15 = [0] * (len(v14) + 1)
        for v8 in range(len(v14)):
            v15[v8 + 1] += v15[v8] + v6[v14[v8]]
        return [v15[bisect.bisect_left(v14, x)] for v16 in a2]
