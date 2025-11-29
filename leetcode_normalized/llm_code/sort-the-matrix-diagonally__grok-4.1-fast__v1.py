class C1:

    def diagonalSort(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        for v3 in range(-(v2 - 1), v1):
            v4 = []
            for v5 in range(v1):
                v6 = v5 - v3
                if 0 <= v6 < v2:
                    v4.append((v5, v6))
            v7 = sorted((a1[v5][v6] for v5, v6 in v4))
            for v8, (v5, v6) in enumerate(v4):
                a1[v5][v6] = v7[v8]
        return a1
