class C1(object):

    def maxWalls(self, a1, a2, a3):
        """
        """
        v1 = [(0, 0)] + sorted(zip(a1, a2), key=lambda x: x[0]) + [(float('inf'), 0)]
        a3.sort()
        v2 = v3 = v4 = v5 = 0
        v6, v7 = ([0] * 2, [0] * 2)
        for v8 in range(1, len(v1) - 1):
            while v5 < len(a3) and a3[v5] < v1[v8][0]:
                v5 += 1
            v9 = min(v1[v8][0] + v1[v8][1], v1[v8 + 1][0] - 1)
            while v4 < len(a3) and a3[v4] <= v9:
                v4 += 1
            v7[1] = max(v6[0], v6[1]) + (v4 - v5)
            if v5 < len(a3) and a3[v5] == v1[v8][0]:
                v5 += 1
            v10 = max(v1[v8][0] - v1[v8][1], v1[v8 - 1][0] + 1)
            while v2 < len(a3) and a3[v2] < v10:
                v2 += 1
            v11 = max(min(v1[v8 - 1][0] + v1[v8 - 1][1], v1[v8][0] - 1) + 1, max(v1[v8][0] - v1[v8][1], v1[v8 - 1][0] + 1))
            while v3 < len(a3) and a3[v3] < v11:
                v3 += 1
            v7[0] = max(v6[0] + (v5 - v2), v6[1] + (v5 - v3))
            v6, v7 = (v7, v6)
        return max(v6[0], v6[1])
