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
        v10 = [[min((v5[v3][v4][v9] for v9 in v1[v4 - v3 + 1] if v9 != v4 - v3 + 1)) if v3 < v4 else 0 for v4 in range(len(a1))] for v3 in range(len(a1))]
        v11 = [len(a1)] * (len(a1) + 1)
        v11[0] = 0
        for v6 in range(a2):
            v12 = [len(a1)] * (len(a1) + 1)
            for v3 in range(len(a1)):
                for v4 in range(v6 * 2, v3):
                    v12[v3 + 1] = min(v12[v3 + 1], v11[v4] + v10[v4][v3])
            v11 = v12
        return v11[len(a1)]
