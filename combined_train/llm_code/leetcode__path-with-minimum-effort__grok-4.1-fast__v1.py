class C1:

    def minimumEffortPath(self, a1):
        v1, v2 = (len(a1), len(a1[0]))

        def idx(a1, a2):
            return a1 * v2 + a2
        v3 = []
        for v4 in range(v1):
            for v5 in range(v2):
                for v6, v7 in ((1, 0), (0, 1)):
                    v8, v9 = (v4 + v6, v5 + v7)
                    if v8 < v1 and v9 < v2:
                        v10 = abs(a1[v4][v5] - a1[v8][v9])
                        v3.append((v10, idx(v4, v5), idx(v8, v9)))
        v3.sort()
        v11 = list(range(v1 * v2))
        v12 = [0] * (v1 * v2)

        def root(a1):
            if v11[a1] != a1:
                v11[a1] = root(v11[a1])
            return v11[a1]

        def merge(a1, a2):
            v1, v2 = (root(a1), root(a2))
            if v1 == v2:
                return False
            if v12[v1] < v12[v2]:
                v11[v1] = v2
            elif v12[v1] > v12[v2]:
                v11[v2] = v1
            else:
                v11[v2] = v1
                v12[v1] += 1
            return True
        v13 = idx(0, 0)
        v14 = idx(v1 - 1, v2 - 1)
        for v15, v16, v17 in v3:
            merge(v16, v17)
            if root(v13) == root(v14):
                return v15
        return 0
