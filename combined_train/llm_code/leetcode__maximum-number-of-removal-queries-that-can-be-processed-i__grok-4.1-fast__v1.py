class C1(object):

    def maximumProcessableQueries(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = [[-1] * v1 for v4 in range(v1)]
        v3[0][v1 - 1] = 0
        for v5 in range(v1 - 1, 0, -1):
            for v6 in range(v1 - v5 + 1):
                v7 = v6 + v5 - 1
                v8 = []
                if v6 > 0 and v3[v6 - 1][v7] >= 0:
                    v9 = v3[v6 - 1][v7]
                    v10 = 1 if a1[v6 - 1] >= a2[v9] else 0
                    v8.append(v9 + v10)
                if v7 < v1 - 1 and v3[v6][v7 + 1] >= 0:
                    v9 = v3[v6][v7 + 1]
                    v10 = 1 if a1[v7 + 1] >= a2[v9] else 0
                    v8.append(v9 + v10)
                if v8:
                    v3[v6][v7] = max(v8)
                if v3[v6][v7] == v2:
                    return v2
        v11 = 0
        for v12 in range(v1):
            if v3[v12][v12] >= 0:
                v9 = v3[v12][v12]
                v10 = 1 if v9 < v2 and a1[v12] >= a2[v9] else 0
                v11 = max(v11, v9 + v10)
        return v11
