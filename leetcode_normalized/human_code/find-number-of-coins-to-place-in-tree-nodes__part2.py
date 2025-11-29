class C1(object):

    def placedCoins(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            v1 = [a2[a1]]
            for v2 in adj[a1]:
                if v2 == a2:
                    continue
                v1.extend(dfs(v2, a1))
                v1.sort()
                if len(v1) > 5:
                    v1 = v1[:2] + v1[-3:]
            result[a1] = 1 if len(v1) < 3 else max(v1[0] * v1[1] * v1[-1], v1[-3] * v1[-2] * v1[-1], 0)
            return v1
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * len(a2)
        dfs(0, -1)
        return v5
