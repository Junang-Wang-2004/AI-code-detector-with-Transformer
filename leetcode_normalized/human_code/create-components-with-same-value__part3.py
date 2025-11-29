class C1(object):

    def componentValue(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3):
            v1 = a1[a1]
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v1 += dfs(v2, a1, a3)
            return v1 if v1 != a3 else 0
        v1 = 0
        v2 = [[] for v3 in range(len(a1))]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = sum(a1)
        for v7 in reversed(range(2, len(a1) + 1)):
            if v6 % v7 == 0 and dfs(0, -1, v6 // v7) == 0:
                return v7 - 1
        return 0
