class C1(object):

    def maxOutput(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2):
            v1 = [a3[a1], 0]
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v3 = dfs(v2, a1)
                result[0] = max(result[0], v1[0] + v3[1], v1[1] + v3[0])
                v1[0] = max(v1[0], v3[0] + a3[a1])
                v1[1] = max(v1[1], v3[1] + a3[a1])
            return v1
        v1 = [0]
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        dfs(0, -1)
        return v1[0]
