class C1(object):

    def minIncrease(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            v1 = v2 = 0
            for v3 in adj[a1]:
                if v3 == a2:
                    continue
                v4 = dfs(v3, a1)
                if v4 < v1:
                    continue
                if v4 > v1:
                    v1 = v4
                    v2 = 0
                v2 += 1
            result[0] -= v2
            return v1 + a3[a1]
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [a1 - 1]
        dfs(0, -1)
        return v5[0]
