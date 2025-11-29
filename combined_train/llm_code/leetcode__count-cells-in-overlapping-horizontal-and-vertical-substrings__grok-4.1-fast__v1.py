class C1:

    def countCells(self, a1, a2):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = len(a2)

        def compute_z(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3, v4 = (0, 0)
            for v5 in range(1, v1):
                if v5 < v4:
                    v2[v5] = min(v4 - v5, v2[v5 - v3])
                while v5 + v2[v5] < v1 and a1[v2[v5]] == a1[v5 + v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2

        def get_mask(a1, a2, a3):
            if not a3:
                a1, a2 = (a2, a1)
            v3 = ''.join((a1[x][y] for v4 in range(a1) for v5 in range(a2))) if a3 else ''.join((a1[v5][v4] for v4 in range(a1) for v5 in range(a2)))
            v6 = a2 + v3
            v7 = compute_z(v6)
            v8 = a1 * a2
            v9 = [False] * v8
            v10 = 0
            for v11 in range(v3, len(v6)):
                if v7[v11] >= v3:
                    v12 = v11 - v3
                    v10 = max(v10, v12)
                    v13 = v12 + v3 - 1
                    while v10 <= v13:
                        v9[v10] = True
                        v10 += 1
            v14 = [[False] * a2 for v15 in range(a1)]
            v16 = a2
            for v17 in range(v8):
                if v9[v17]:
                    v14[v17 // v16][v17 % v16] = True
            return v14
        v4 = get_mask(v1, v2, True)
        v5 = get_mask(v1, v2, False)
        return sum((v4[i][j] and v5[j][i] for v6 in range(v1) for v7 in range(v2)))
