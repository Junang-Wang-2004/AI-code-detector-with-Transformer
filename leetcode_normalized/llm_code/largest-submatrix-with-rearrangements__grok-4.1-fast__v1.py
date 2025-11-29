class C1:

    def largestSubmatrix(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [0] * v2
        v4 = 0
        for v5 in range(v1):
            for v6 in range(v2):
                v3[v6] = v3[v6] + 1 if a1[v5][v6] else 0
            v7 = sorted(v3)
            for v8 in range(v2):
                v9 = (v2 - v8) * v7[v8]
                if v9 > v4:
                    v4 = v9
        return v4
