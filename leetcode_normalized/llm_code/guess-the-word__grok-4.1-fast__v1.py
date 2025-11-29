class C1:

    def findSecretWord(self, a1, a2):
        v1 = len(a1)
        v2 = [[0] * v1 for v3 in range(v1)]
        for v4 in range(v1):
            for v5 in range(v4 + 1, v1):
                v6 = sum((a1[v4][k] == a1[v5][k] for v7 in range(6)))
                v2[v4][v5] = v2[v5][v4] = v6
        for v4 in range(v1):
            v2[v4][v4] = 6
        v8 = set(range(v1))
        for v3 in range(6):
            if len(v8) <= 1:
                return
            v9 = None
            v10 = float('inf')
            for v11 in v8:
                v12 = [[] for v3 in range(7)]
                for v5 in v8:
                    if v5 != v11:
                        v12[v2[v11][v5]].append(v5)
                v13 = max((len(group) for v14 in v12))
                if v13 < v10:
                    v10 = v13
                    v9 = v11
            v15 = a2.guess(a1[v9])
            if v15 == 6:
                return
            v8 = {v5 for v5 in v8 if v2[v9][v5] == v15}
