class C1(object):

    def treeQueries(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3):
            L[a1] = cnt[0]
            cnt[0] += 1
            dist[a1] = a3
            for v1, v2 in adj[a1]:
                if v1 == a2:
                    continue
                lookup[v1] = v2
                dfs(v1, a1, a3 + v2)
            R[a1] = cnt[0]
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v3 -= 1
            v4 -= 1
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6, v7, v8, v9 = ([0] * a1, [0] * a1, [0] * a1, [0] * a1)
        v10 = [0]
        dfs(0, -1, 0)
        v11 = BIT(a1)
        v12 = []
        for v13 in a3:
            if v13[0] == 1:
                v2, v3, v4, v5 = v13
                v3 -= 1
                v4 -= 1
                if v6[v3] > v6[v4]:
                    v3, v4 = (v4, v3)
                v14 = v5 - v9[v4]
                v11.add(v6[v4], v14)
                v11.add(v7[v4], -v14)
                v9[v4] = v5
            else:
                v2, v15 = v13
                v15 -= 1
                v12.append(v8[v15] + v11.query(v6[v15]))
        return v12
