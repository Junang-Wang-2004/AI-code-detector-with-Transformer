class C1(object):

    def largestVariance(self, a1):
        v1 = list(set(a1))
        if len(v1) < 2:
            return 0
        v2 = len(a1)
        v3 = -2000000
        v4 = 0
        for v5 in v1:
            for v6 in v1:
                if v5 == v6:
                    continue
                v7 = [v3] * 4
                v8 = v3
                for v9 in range(v2):
                    v10 = 1 if a1[v9] == v5 else -1 if a1[v9] == v6 else 0
                    v11 = 1 if a1[v9] == v5 else 0
                    v12 = 1 if a1[v9] == v6 else 0
                    v13 = [v3] * 4
                    v14 = v11 * 2 + v12
                    v13[v14] = max(v13[v14], v10)
                    for v15 in range(4):
                        if v7[v15] == v3:
                            continue
                        v16 = v15 // 2
                        v17 = v15 % 2
                        v18 = v16 | v11
                        v19 = v17 | v12
                        v20 = v18 * 2 + v19
                        v21 = v7[v15] + v10
                        v13[v20] = max(v13[v20], v21)
                    v7 = v13
                    v8 = max(v8, v7[3])
                v4 = max(v4, v8)
        return v4
