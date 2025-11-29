class C1(object):

    def minimumTotalPrice(self, a1, a2, a3, a4):
        """
        """

        def dfs(a1, a2, a3):
            lookup[a1] += 1
            if a1 == a3:
                return True
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                if dfs(v1, a1, a3):
                    return True
            lookup[a1] -= 1
            return False

        def dfs2(a1, a2):
            v1, v2 = (a3[a1] * lookup[a1], a3[a1] // 2 * lookup[a1])
            for v3 in adj[a1]:
                if v3 == a2:
                    continue
                v4, v5 = dfs2(v3, a1)
                v1 += min(v4, v5)
                v2 += v4
            return (v1, v2)
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0] * a1
        for v3, v4 in a4:
            dfs(v3, -1, v4)
        return min(dfs2(0, -1))
