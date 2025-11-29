class C1(object):

    def maximumSubtreeSize(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            v1 = 1
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v3 = dfs(v2, a1)
                if v1 == -1:
                    continue
                if v3 == -1 or a2[v2] != a2[a1]:
                    v1 = -1
                    continue
                v1 += v3
            result[0] = max(result[0], v1)
            return v1
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0]
        dfs(0, -1)
        return v5[0]
