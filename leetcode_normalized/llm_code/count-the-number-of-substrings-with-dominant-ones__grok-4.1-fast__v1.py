class C1:

    def numberOfSubstrings(self, a1: str) -> int:
        v1 = len(a1)
        v2 = [-1]
        for v3 in range(v1):
            if a1[v3] == '0':
                v2.append(v3)
        v2.append(v1)
        v4 = len(v2) - 2
        v5 = 0
        for v6 in range(len(v2) - 1):
            v7 = v2[v6] + 1
            v8 = v2[v6 + 1] - 1
            v9 = v8 - v7 + 1
            if v9 > 0:
                v5 += v9 * (v9 + 1) // 2
        v10 = 0
        while v10 * (v10 + 1) <= v1:
            v10 += 1
        v10 -= 1
        for v11 in range(1, min(v4, v10) + 1):
            v12 = v11 * v11 + v11
            v13 = v12 - 1
            for v14 in range(1, v4 - v11 + 2):
                v15 = v2[v14 - 1] + 1
                v16 = v2[v14]
                v17 = v2[v14 + v11 - 1]
                v18 = v2[v14 + v11] - 1
                v19 = v16 - v15 + 1
                v20 = v18 - v17 + 1
                if v19 <= 0 or v20 <= 0:
                    continue
                v21 = v17 - v13
                v22 = min(v16, v21)
                v23 = v15
                v24 = max(0, v22 - v23 + 1)
                v5 += v24 * v20
                v25 = max(v15, v21 + 1)
                v26 = v16
                if v25 <= v26:
                    v27 = v18 - v13 + 1
                    v28 = min(v26, v27)
                    if v28 >= v25:
                        v29 = v28 - v25 + 1
                        v30 = v27 - v25
                        v31 = v27 - v28
                        v5 += v29 * (v30 + v31) // 2
        return v5
