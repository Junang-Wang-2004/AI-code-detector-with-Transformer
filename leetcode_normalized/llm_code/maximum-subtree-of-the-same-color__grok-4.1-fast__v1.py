class C1:

    def maximumSubtreeSize(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [0]

        def dfs(a1, a2):
            v1 = 1
            v2 = True
            for v3 in v2[a1]:
                if v3 == a2:
                    continue
                v4 = dfs(v3, a1)
                if v4 != -1 and a2[v3] == a2[a1]:
                    v1 += v4
                else:
                    v2 = False
            if not v2:
                v1 = -1
            v6[0] = max(v6[0], v1)
            return v1
        dfs(0, -1)
        return v6[0]
