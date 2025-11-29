class C1(object):

    def minMoves(self, a1, a2):
        v1 = [i for v2, v3 in enumerate(a1) if v3]
        v4 = len(v1)
        if v4 < a2:
            return float('inf')
        v5 = [0] * (v4 + 1)
        for v2 in range(v4):
            v5[v2 + 1] = v5[v2] + v1[v2]
        v6 = a2 // 2
        v7 = v6 * ((a2 + 1) // 2)
        v8 = float('inf')
        for v2 in range(v4 - a2 + 1):
            v9 = v5[v2 + a2] + v5[v2] - v5[v2 + v6] - v5[v2 + (a2 + 1) // 2]
            if v9 < v8:
                v8 = v9
        return v8 - v7
