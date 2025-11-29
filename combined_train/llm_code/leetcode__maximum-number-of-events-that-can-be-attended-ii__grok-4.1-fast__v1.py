class C1(object):

    def maxValue(self, a1, a2):
        a1.sort(key=lambda x: x[1])
        v1 = len(a1)
        v2 = [ev[1] for v3 in a1]
        v4 = [0] * v1
        for v5 in range(v1):
            v6, v7 = (0, v5)
            while v6 <= v7:
                v8 = v6 + (v7 - v6) // 2
                if v2[v8] < a1[v5][0]:
                    v6 = v8 + 1
                else:
                    v7 = v8 - 1
            v4[v5] = v7 + 1
        v9 = [[0] * (a2 + 1) for v10 in range(v1 + 1)]
        for v5 in range(1, v1 + 1):
            v11 = v4[v5 - 1]
            for v12 in range(a2 + 1):
                v9[v5][v12] = v9[v5 - 1][v12]
            for v12 in range(1, a2 + 1):
                v9[v5][v12] = max(v9[v5][v12], v9[v11][v12 - 1] + a1[v5 - 1][2])
        return v9[v1][a2]
