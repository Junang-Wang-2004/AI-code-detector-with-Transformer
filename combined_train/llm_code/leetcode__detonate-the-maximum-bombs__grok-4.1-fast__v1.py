class C1:

    def maximumDetonation(self, a1):
        v1 = len(a1)
        v2 = [[] for v3 in range(v1)]
        for v4 in range(v1):
            v5, v6, v7 = a1[v4]
            for v8 in range(v1):
                if v4 == v8:
                    continue
                v9, v10 = (a1[v8][0], a1[v8][1])
                v11, v12 = (v5 - v9, v6 - v10)
                if v11 * v11 + v12 * v12 <= v7 * v7:
                    v2[v4].append(v8)

        def dfs(a1, a2):
            a2[a1] = True
            for v1 in v2[a1]:
                if not a2[v1]:
                    dfs(v1, a2)
        v13 = 0
        for v14 in range(v1):
            v15 = [False] * v1
            dfs(v14, v15)
            v16 = sum(v15)
            if v16 > v13:
                v13 = v16
            if v13 == v1:
                return v1
        return v13
