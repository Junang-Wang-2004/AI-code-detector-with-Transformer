class C1:

    def firstCompleteIndex(self, a1, a2):
        v1 = len(a2)
        v2 = len(a2[0])
        v3 = {}
        for v4 in range(v1):
            for v5 in range(v2):
                v3[a2[v4][v5]] = (v4, v5)
        v6 = [0] * v1
        v7 = [0] * v2
        for v8, v9 in enumerate(a1):
            v10, v11 = v3[v9]
            v6[v10] += 1
            v7[v11] += 1
            if v6[v10] == v2 or v7[v11] == v1:
                return v8
        return -1
