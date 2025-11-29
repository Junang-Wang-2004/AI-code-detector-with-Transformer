import collections

class C1:

    def subsequencesWithMiddleMode(self, a1):
        v1 = 10 ** 9 + 7

        def c(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            if a2 == 0:
                return 1
            if a2 == 1:
                return a1
            return a1 * (a1 - 1) // 2
        v2 = len(a1)
        v3 = collections.Counter(a1)
        v4 = collections.Counter()
        v5 = 0
        v6 = 0
        v7 = 0
        v8 = 0
        v9 = 0
        v6 = sum((f * f for v10 in v3.values()))
        v11 = 0
        for v12 in range(v2):
            v13 = a1[v12]
            v5 -= v4[v13] * v4[v13]
            v6 -= v3[v13] * v3[v13]
            v7 -= v4[v13] * v3[v13]
            v8 -= v4[v13] * v4[v13] * v3[v13]
            v9 -= v4[v13] * v3[v13] * v3[v13]
            v3[v13] -= 1
            v14 = v4[v13]
            v15 = v3[v13]
            v16 = v12
            v17 = v2 - v12 - 1
            v18 = v16 - v14
            v19 = v17 - v15
            v20 = 0
            for v21 in range(3):
                v22 = c(v14, v21) * c(v18, 2 - v21)
                for v23 in range(3):
                    if v21 + v23 < 2:
                        continue
                    v24 = c(v15, v23) * c(v19, 2 - v23)
                    v20 = (v20 + v22 * v24) % v1
            v11 = (v11 + v20) % v1
            v25 = v18 * c(v19, 2)
            v26 = (v6 - v19) // 2
            v27 = v19 * v7 - v9
            v28 = v25 - v18 * v26 - v27
            if v28 > 0:
                v29 = c(v14, 1) * c(v15, 0) * v28 % v1
                v11 = (v11 + v29) % v1
            v30 = v19 * c(v18, 2)
            v31 = (v5 - v18) // 2
            v32 = v18 * v7 - v8
            v33 = v30 - v19 * v31 - v32
            if v33 > 0:
                v29 = c(v14, 0) * c(v15, 1) * v33 % v1
                v11 = (v11 + v29) % v1
            v4[v13] += 1
            v5 += v4[v13] * v4[v13]
            v6 += v3[v13] * v3[v13]
            v7 += v4[v13] * v3[v13]
            v8 += v4[v13] * v4[v13] * v3[v13]
            v9 += v4[v13] * v3[v13] * v3[v13]
        return v11
