import collections

class C1(object):

    def subsequencesWithMiddleMode(self, a1):
        v1 = 10 ** 9 + 7

        def comb2(a1):
            return a1 * (a1 - 1) // 2
        v2 = len(a1)
        v3 = collections.defaultdict(int)
        v4 = collections.defaultdict(int)
        for v5 in a1:
            v4[v5] += 1
        v6 = 0
        v7 = sum((c * c for v8 in v4.values()))
        v9 = 0
        v10 = 0
        v11 = 0
        v12 = 0
        for v13 in range(v2):
            v14 = a1[v13]
            v6 -= v3[v14] * v3[v14]
            v7 -= v4[v14] * v4[v14]
            v9 -= v3[v14] * v4[v14]
            v10 -= v3[v14] * v3[v14] * v4[v14]
            v11 -= v3[v14] * v4[v14] * v4[v14]
            v4[v14] -= 1
            v15 = v13
            v16 = v2 - v13 - 1
            v17 = v3[v14]
            v18 = v4[v14]
            v19 = v15 - v17
            v20 = v16 - v18
            v21 = comb2(v15) * comb2(v16)
            v22 = comb2(v19) * comb2(v20)
            v23 = v17 * v19 * comb2(v20)
            v24 = comb2(v19) * v18 * v20
            v25 = (v21 - v22 - v23 - v24) % v1
            v26 = (v6 - v19) // 2
            v27 = (v7 - v20) // 2
            v28 = v19 * comb2(v20) - v20 * v9 + v11 - v27 * v19
            v29 = v17 * v28 % v1
            v30 = v20 * comb2(v19) - v19 * v9 + v10 - v26 * v20
            v31 = v18 * v30 % v1
            v12 = (v12 + v25 + v29 + v31) % v1
            v3[v14] += 1
            v6 += v3[v14] * v3[v14]
            v7 += v4[v14] * v4[v14]
            v9 += v3[v14] * v4[v14]
            v10 += v3[v14] * v3[v14] * v4[v14]
            v11 += v3[v14] * v4[v14] * v4[v14]
        return v12
