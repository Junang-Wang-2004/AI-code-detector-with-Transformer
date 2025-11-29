class C1:

    def minTime(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)

        def dfs(a1, a2):
            v1 = 0
            for v2 in v1[a1]:
                if v2 == a2:
                    continue
                v3 = dfs(v2, a1)
                if v3 > 0 or a3[v2]:
                    v1 += v3 + 2
            return v1
        return dfs(0, -1)
