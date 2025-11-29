class C1:

    def findMaxForm(self, a1, a2, a3):
        v1 = []
        for v2 in a1:
            v3 = v2.count('0')
            v4 = v2.count('1')
            v1.append((v3, v4))
        v5 = [[0] * (a3 + 1) for v6 in range(a2 + 1)]
        for v3, v4 in v1:
            for v7 in range(a2, v3 - 1, -1):
                for v8 in range(a3, v4 - 1, -1):
                    v5[v7][v8] = max(v5[v7][v8], v5[v7 - v3][v8 - v4] + 1)
        return v5[a2][a3]
