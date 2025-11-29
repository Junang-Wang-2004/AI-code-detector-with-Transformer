class C1:

    def minScore(self, a1, a2):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)
        v6 = [False] * a1
        v7 = [0]
        v6[0] = True
        while v7:
            v8 = []
            for v9 in v7:
                for v10 in v1[v9]:
                    if not v6[v10]:
                        v6[v10] = True
                        v8.append(v10)
            v7 = v8
        return min((v5 for v3, v4, v5 in a2 if v6[v3 - 1] or v6[v4 - 1]))
