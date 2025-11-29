class C1:

    def minDeletionSize(self, a1):
        if not a1 or len(a1) < 2:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [True] * (v1 - 1)
        v4 = 0
        for v5 in range(v2):
            v6 = any((v3[i] and a1[i][v5] > a1[i + 1][v5] for v7 in range(v1 - 1)))
            if v6:
                v4 += 1
                continue
            for v7 in range(v1 - 1):
                if v3[v7] and a1[v7][v5] < a1[v7 + 1][v5]:
                    v3[v7] = False
        return v4
