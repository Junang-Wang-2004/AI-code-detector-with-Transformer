class C1(object):

    def solveQueries(self, a1, a2):
        v1 = len(a1)
        v2 = {}
        for v3 in range(v1):
            v4 = a1[v3]
            if v4 not in v2:
                v2[v4] = []
            v2[v4].append(v3)
        v5 = [v1] * v1
        for v4, v6 in v2.items():
            v7 = len(v6)
            if v7 < 2:
                continue
            for v8 in range(v7):
                v9 = v6[(v8 - 1) % v7]
                v10 = v6[(v8 + 1) % v7]
                v11 = (v6[v8] - v9 + v1) % v1
                v12 = (v10 - v6[v8] + v1) % v1
                v5[v6[v8]] = min(v5[v6[v8]], min(v11, v12))
        v13 = []
        for v14 in a2:
            v13.append(v5[v14] if v5[v14] < v1 else -1)
        return v13
