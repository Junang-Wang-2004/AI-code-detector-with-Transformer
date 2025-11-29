class C1:

    def magnificentSets(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v3 -= 1
            v4 -= 1
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1
        v6 = [-1] * a1
        v7 = 0
        for v8 in range(a1):
            if v5[v8]:
                continue
            v9 = []
            v10 = [v8]
            v5[v8] = True
            v6[v8] = 0
            v9.append(v8)
            v11 = True
            v12 = 0
            while v12 < len(v10) and v11:
                v13 = v10[v12]
                v12 += 1
                for v14 in v1[v13]:
                    if v6[v14] == -1:
                        v6[v14] = 1 - v6[v13]
                        v5[v14] = True
                        v10.append(v14)
                        v9.append(v14)
                    elif v6[v14] == v6[v13]:
                        v11 = False
            if not v11:
                return -1
            v15 = 0
            for v16 in v9:
                v17 = [False] * a1
                v18 = [v16]
                v17[v16] = True
                v19 = 0
                while v18:
                    v20 = []
                    for v13 in v18:
                        for v14 in v1[v13]:
                            if not v17[v14]:
                                v17[v14] = True
                                v20.append(v14)
                    v18 = v20
                    if v18:
                        v19 += 1
                v15 = max(v15, v19 + 1)
            v7 += v15
        return v7
