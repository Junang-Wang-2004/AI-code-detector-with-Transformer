class C1:

    def minDays(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def num_components():
            v1 = [[False] * v2 for v2 in range(v1)]
            v3 = 0
            for v4 in range(v1):
                for v5 in range(v2):
                    if a1[v4][v5] and (not v1[v4][v5]):
                        v3 += 1
                        v6 = [(v4, v5)]
                        v1[v4][v5] = True
                        while v6:
                            v7, v8 = v6.pop()
                            for v9, v10 in v3:
                                v11, v12 = (v7 + v9, v8 + v10)
                                if 0 <= v11 < v1 and 0 <= v12 < v2 and a1[v11][v12] and (not v1[v11][v12]):
                                    v1[v11][v12] = True
                                    v6.append((v11, v12))
            return v3
        if num_components() != 1:
            return 0
        v4 = sum((sum(row) for v5 in a1))
        if v4 == 1:
            return 1

        def node(a1, a2):
            return a1 * v2 + a2
        v6 = [[] for v7 in range(v1 * v2)]
        for v8 in range(v1):
            for v9 in range(v2):
                if a1[v8][v9] == 0:
                    continue
                for v10, v11 in v3:
                    v12, v13 = (v8 + v10, v9 + v11)
                    if 0 <= v12 < v1 and 0 <= v13 < v2 and a1[v12][v13]:
                        v6[node(v8, v9)].append(node(v12, v13))
        v14 = [-1] * (v1 * v2)
        v15 = [-1] * (v1 * v2)
        v16 = [-1] * (v1 * v2)
        v17 = [False] * (v1 * v2)
        v18 = 0

        def explore(a1):
            nonlocal timer
            v1 = 0
            v14[a1] = v15[a1] = v18
            v2 += 1
            for v3 in v6[a1]:
                if v14[v3] == -1:
                    v16[v3] = a1
                    v1 += 1
                    explore(v3)
                    v15[a1] = min(v15[a1], v15[v3])
                    if v16[a1] != -1 and v15[v3] >= v14[a1]:
                        v17[a1] = True
                    if v16[a1] == -1 and v1 > 1:
                        v17[a1] = True
                elif v3 != v16[a1]:
                    v15[a1] = min(v15[a1], v14[v3])
        v19 = next((node(v8, v9) for v8 in range(v1) for v9 in range(v2) if a1[v8][v9]))
        explore(v19)
        for v20 in v17:
            if v20:
                return 1
        return 2
