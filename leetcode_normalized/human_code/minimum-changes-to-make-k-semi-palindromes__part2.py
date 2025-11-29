class C1(object):

    def minimumChanges(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3 in range(1, len(v1)):
            for v4 in range(v3, len(v1), v3):
                v1[v4].append(v3)
        v5 = [[{} for v2 in range(len(a1))] for v2 in range(len(a1))]
        for v6 in range(1, len(a1) + 1):
            for v7 in range(len(a1) - v6 + 1):
                v8 = v7 + v6 - 1
                for v9 in v1[v6]:
                    v5[v7][v8][v9] = (v5[v7 + v9][v8 - v9][v9] if v7 + v9 < v8 - v9 else 0) + sum((a1[v7 + v3] != a1[v8 - (v9 - 1) + v3] for v3 in range(v9)))
        v10 = [[len(a1)] * (a2 + 1) for v2 in range(len(a1) + 1)]
        v10[0][0] = 0
        for v3 in range(len(a1)):
            for v4 in range(v3):
                v11 = min((v5[v4][v3][v9] for v9 in v1[v3 - v4 + 1] if v9 != v3 - v4 + 1))
                for v6 in range(a2):
                    v10[v3 + 1][v6 + 1] = min(v10[v3 + 1][v6 + 1], v10[v4][v6] + v11)
        return v10[len(a1)][a2]
