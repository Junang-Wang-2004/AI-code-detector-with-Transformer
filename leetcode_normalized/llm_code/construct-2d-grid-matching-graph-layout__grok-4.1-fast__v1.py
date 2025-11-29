class C1:

    def constructGridLayout(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = min(map(len, v1))
        v6 = [i for v7 in range(a1) if len(v1[v7]) == v5]
        v8 = v6[0]

        def get_dist(a1, a2, a3):
            v1 = [-1] * a2
            v1[a3] = 0
            v2 = [a3]
            while v2:
                v3 = []
                for v4 in v2:
                    for v5 in a1[v4]:
                        if v1[v5] != -1:
                            continue
                        v1[v5] = v1[v4] + 1
                        v3.append(v5)
                v2 = v3
            return v1
        v9 = get_dist(v1, a1, v8)
        v10 = float('inf')
        v11 = -1
        for v12 in v6:
            if v12 != v8 and v9[v12] < v10:
                v10 = v9[v12]
                v11 = v12
        v13 = v9[v11] + 1
        v14 = a1 // v13
        v15 = get_dist(v1, a1, v11)
        v16 = [[0] * v13 for v2 in range(v14)]
        v17 = v13 - 1
        for v18 in range(a1):
            v19 = v9[v18]
            v20 = v15[v18]
            v21 = (v19 + v20 - v17) // 2
            v22 = v19 - v21
            v16[v21][v22] = v18
        return v16
