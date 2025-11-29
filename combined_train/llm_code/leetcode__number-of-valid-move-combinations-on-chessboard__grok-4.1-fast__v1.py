class C1(object):

    def countCombinations(self, a1, a2):
        v1 = {'rook': [(0, 1), (0, -1), (1, 0), (-1, 0)], 'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)], 'queen': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]}
        v2 = (1 << 7) - 1
        v3 = len(a1)
        v4 = [[] for v5 in range(v3)]
        for v6 in range(v3):
            v7, v8 = (a2[v6][0] - 1, a2[v6][1] - 1)
            v9 = v7 * 8 + v8
            v4[v6].append({v9: v2})
            for v10, v11 in v1[a1[v6]]:
                v12, v13 = (v7, v8)
                for v14 in range(1, 8):
                    v12 += v10
                    v13 += v11
                    if not (0 <= v12 < 8 and 0 <= v13 < 8):
                        break
                    v15 = {}
                    v16, v17 = (v7, v8)
                    for v18 in range(1, v14):
                        v16 += v10
                        v17 += v11
                        v15[v16 * 8 + v17] = 1 << v18 - 1
                    v19 = v12 * 8 + v13
                    v20 = 8 - v14
                    v21 = (1 << v20) - 1 << v14 - 1
                    v15[v19] = v21
                    v4[v6].append(v15)
        v22 = [0] * 64

        def search(a1):
            if a1 == v3:
                return 1
            v1 = 0
            for v2 in v4[a1]:
                v3 = []
                v4 = any((v22[s] & m for v5, v6 in v2.items()))
                if not v4:
                    for v5, v6 in v2.items():
                        v22[v5] |= v6
                        v3.append((v5, v6))
                    v1 += search(a1 + 1)
                    for v5, v6 in v3:
                        v22[v5] ^= v6
            return v1
        return search(0)
