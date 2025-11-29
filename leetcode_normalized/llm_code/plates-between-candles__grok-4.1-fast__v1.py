class C1:

    def platesBetweenCandles(self, a1, a2):
        v1 = len(a1)
        v2 = [-1] * v1
        v3 = -1
        for v4 in range(v1):
            if a1[v4] == '|':
                v3 = v4
            v2[v4] = v3
        v5 = [v1] * v1
        v3 = v1
        for v4 in range(v1 - 1, -1, -1):
            if a1[v4] == '|':
                v3 = v4
            v5[v4] = v3
        v6 = [0] * (v1 + 1)
        for v4 in range(v1):
            v6[v4 + 1] = v6[v4] + (a1[v4] == '*')
        v7 = []
        for v8, v9 in a2:
            v10 = v5[v8]
            if v10 > v9:
                v7.append(0)
                continue
            v11 = v2[v9]
            if v11 < v10:
                v7.append(0)
                continue
            v7.append(v6[v11] - v6[v10 + 1])
        return v7
