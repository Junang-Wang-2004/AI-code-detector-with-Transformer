class C1(object):

    def countGoodNodes(self, a1):
        """
        """

        def dfs(a1, a2):
            v1 = v2 = 0
            v3 = True
            for v4 in adj[a1]:
                if v4 == a2:
                    continue
                v5 = dfs(v4, a1)
                v1 += v5
                v2 += 1
                if v2 * v5 != v1:
                    v3 = False
            if v3:
                result[0] += 1
            return v1 + 1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0]
        dfs(0, -1)
        return v5[0]
