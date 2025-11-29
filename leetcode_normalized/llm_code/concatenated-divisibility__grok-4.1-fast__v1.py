class C1:

    def concatenatedDivisibility(self, a1, a2):
        if not a1:
            return []
        v1 = len(a1)
        v2 = [len(str(x)) for v3 in a1]
        v4 = max(v2)
        v5 = [1 % a2]
        for v6 in range(v4):
            v5.append(v5[-1] * 10 % a2)
        v7 = (1 << v1) - 1
        v8 = [[False] * a2 for v6 in range(1 << v1)]
        v8[v7][0] = True
        for v9 in range(v7 - 1, -1, -1):
            for v10 in range(a2):
                for v11 in range(v1):
                    if v9 & 1 << v11:
                        continue
                    v12 = v2[v11]
                    v13 = v5[v12]
                    v14 = (v10 * v13 + a1[v11]) % a2
                    v15 = v9 | 1 << v11
                    if v8[v15][v14]:
                        v8[v9][v10] = True
                        break
        if not v8[0][0]:
            return []
        v16 = sorted(((a1[j], j) for v17 in range(v1)))
        v18 = []
        v19 = 0
        v20 = 0
        for v6 in range(v1):
            for v6, v11 in v16:
                if v19 & 1 << v11:
                    continue
                v12 = v2[v11]
                v13 = v5[v12]
                v14 = (v20 * v13 + a1[v11]) % a2
                v15 = v19 | 1 << v11
                if v8[v15][v14]:
                    v18.append(a1[v11])
                    v19 = v15
                    v20 = v14
                    break
        return v18
