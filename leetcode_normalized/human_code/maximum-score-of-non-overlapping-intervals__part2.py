import bisect

class C1(object):

    def maximumWeight(self, a1):
        """
        """
        v1 = 4
        v2 = {}
        for v3, (v4, v5, v6) in enumerate(a1):
            if (v4, v5, v6) not in v2:
                v2[v4, v5, v6] = v3
        v7 = sorted(iter(v2.keys()), key=lambda x: x[0])
        v8 = [[[0, []] for v9 in range(v1 + 1)] for v9 in range(len(v7) + 1)]
        for v3 in reversed(range(len(v8) - 1)):
            v10 = bisect.bisect_right(v7, (v7[v3][1] + 1, 0, 0))
            v11 = v2[v7[v3]]
            for v12 in range(1, len(v8[v3])):
                v13 = [v8[v10][v12 - 1][0] - v7[v3][2], v8[v10][v12 - 1][1][:]]
                insort(v13[1], v11)
                v8[v3][v12] = min(v8[v3 + 1][v12], v13)
        return v8[0][v1][1]
