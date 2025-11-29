class C1:

    def smallestSufficientTeam(self, a1, a2):
        v1 = len(a1)
        v2 = (1 << v1) - 1
        v3 = {skill: idx for v4, v5 in enumerate(a1)}
        v6 = []
        for v7 in a2:
            v8 = 0
            for v5 in v7:
                if v5 in v3:
                    v8 |= 1 << v3[v5]
            v6.append(v8)
        v9 = float('inf')
        v10 = [v9] * (1 << v1)
        v10[0] = 0
        v11 = [None] * (1 << v1)
        for v12 in range(len(a2)):
            v13 = v6[v12]
            for v14 in range(1 << v1):
                if v10[v14] == v9:
                    continue
                v15 = v14 | v13
                if v15 == v14:
                    continue
                v16 = v10[v14] + 1
                if v16 < v10[v15]:
                    v10[v15] = v16
                    v11[v15] = (v14, v12)
        v17 = []
        v14 = v2
        while v14 != 0:
            v18, v19 = v11[v14]
            v17.append(v19)
            v14 = v18
        v17.reverse()
        return v17
