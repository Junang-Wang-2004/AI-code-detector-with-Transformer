class C1:

    def reachableNodes(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1
        for v6 in a3:
            v5[v6] = True
        v7 = [0]

        def explore(a1):
            v5[a1] = True
            v7[0] += 1
            for v1 in v1[a1]:
                if not v5[v1]:
                    explore(v1)
        v5[0] = True
        explore(0)
        return v7[0]
