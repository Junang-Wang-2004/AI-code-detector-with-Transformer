class C1(object):

    def subsequencePairCount(self, a1):
        if not a1:
            return 0
        v1 = 10 ** 9 + 7
        v2 = max(a1)
        v3 = len(a1)
        v4 = 2 * v3 + 5
        v5 = [1] * (v4 + 1)
        for v6 in range(1, v4 + 1):
            v5[v6] = v5[v6 - 1] * 2 % v1
        v7 = [1] * (v3 + 5)
        for v6 in range(1, v3 + 5):
            v7[v6] = v7[v6 - 1] * 3 % v1
        v8 = [0] * (v2 + 1)
        v8[1] = 1
        v9 = [False] * (v2 + 1)
        v10 = []
        for v11 in range(2, v2 + 1):
            if not v9[v11]:
                v10.append(v11)
                v8[v11] = -1
            for v12 in v10:
                if v11 * v12 > v2:
                    break
                v9[v11 * v12] = True
                if v11 % v12 == 0:
                    v8[v11 * v12] = 0
                    break
                else:
                    v8[v11 * v12] = -v8[v11]
        v13 = [0] * (v2 + 1)
        for v14 in a1:
            v13[v14] += 1
        v15 = [v13[jj] for v16 in range(v2 + 1)]
        for v17 in range(1, v2 + 1):
            for v18 in range(v17 * 2, v2 + 1, v17):
                v15[v17] += v15[v18]
        v19 = [[0] * (v2 + 1) for v20 in range(v2 + 1)]

        def gc(a1, a2):
            while a2 != 0:
                a1, a2 = (a2, a1 % a2)
            return a1
        for v21 in range(1, v2 + 1):
            for v22 in range(v21, v2 + 1):
                v23 = v21 * v22 // gc(v21, v22)
                v24 = v15[v23] if v23 <= v2 else 0
                v25 = v15[v21]
                v26 = v15[v22]
                v27 = v25 - v24 + v26 - v24
                v28 = v7[v24] * v5[v27] % v1
                v28 = (v28 - v5[v25] - v5[v26] + 1 + 2 * v1) % v1
                v19[v21][v22] = v19[v22][v21] = v28
        v29 = 0
        for v30 in range(1, v2 + 1):
            v31 = v2 // v30
            for v32 in range(1, v31 + 1):
                v33 = v8[v32]
                if v33 == 0:
                    continue
                v34 = v30 * v32
                for v35 in range(1, v31 + 1):
                    v36 = v8[v35]
                    v37 = v30 * v35
                    v38 = v33 * v36 * v19[v34][v37]
                    v29 = (v29 + v38) % v1
        return v29
