class C1:

    def minimumCost(self, a1, a2, a3, a4, a5):
        v1 = float('inf')
        v2 = 26
        v3 = [[v1] * v2 for v4 in range(v2)]
        for v5 in range(v2):
            v3[v5][v5] = 0
        for v6 in range(len(a3)):
            v7 = ord(a3[v6]) - ord('a')
            v8 = ord(a4[v6]) - ord('a')
            v3[v7][v8] = min(v3[v7][v8], a5[v6])
        for v9 in range(v2):
            for v10 in range(v2):
                for v11 in range(v2):
                    v3[v10][v11] = min(v3[v10][v11], v3[v10][v9] + v3[v9][v11])
        v12 = sum((v3[ord(a1[p]) - ord('a')][ord(a2[p]) - ord('a')] for v13 in range(len(a1))))
        return v12 if v12 != v1 else -1
