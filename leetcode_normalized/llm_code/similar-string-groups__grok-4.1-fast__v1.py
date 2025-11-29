class C1:

    def numSimilarGroups(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = list(range(v1))
        v4 = [0] * v1

        def get(a1):
            if v3[a1] != a1:
                v3[a1] = get(v3[a1])
            return v3[a1]

        def merge(a1, a2):
            v1 = get(a1)
            v2 = get(a2)
            if v1 == v2:
                return
            if v4[v1] < v4[v2]:
                v3[v1] = v2
            elif v4[v1] > v4[v2]:
                v3[v2] = v1
            else:
                v3[v2] = v1
                v4[v1] += 1
        for v5 in range(v1):
            for v6 in range(v5 + 1, v1):
                v7 = 0
                for v8 in range(v2):
                    if a1[v5][v8] != a1[v6][v8]:
                        v7 += 1
                        if v7 > 2:
                            break
                if v7 == 2:
                    merge(v5, v6)
        v9 = set((get(v5) for v5 in range(v1)))
        return len(v9)
