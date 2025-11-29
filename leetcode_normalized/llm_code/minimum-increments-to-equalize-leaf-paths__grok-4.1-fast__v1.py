class C1:

    def minIncrease(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0]

        def dfs(a1, a2):
            v1 = []
            for v2 in v1[a1]:
                if v2 != a2:
                    v1.append(dfs(v2, a1))
            if v1:
                v3 = max(v1)
                v5[0] += v1.count(v3)
                return a3[a1] + v3
            return a3[a1]
        dfs(0, -1)
        return a1 - 1 - v5[0]
