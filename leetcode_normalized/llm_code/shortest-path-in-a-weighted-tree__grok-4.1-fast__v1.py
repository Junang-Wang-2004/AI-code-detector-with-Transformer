class C1:

    def treeQueries(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v3 -= 1
            v4 -= 1
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [0] * a1
        v7 = [0] * a1
        v8 = [0] * a1
        v9 = [0] * a1
        v10 = [0]

        def dfs(a1, a2, a3):
            v6[a1] = v10[0]
            v10[0] += 1
            v8[a1] = a3
            for v1, v2 in v1[a1]:
                if v1 == a2:
                    continue
                v9[v1] = v2
                dfs(v1, a1, a3 + v2)
            v7[a1] = v10[0]
        dfs(0, -1, 0)
        v11 = [0] * (a1 + 2)

        def ft_update(a1, a2):
            a1 += 1
            while a1 <= a1:
                v11[a1] += a2
                a1 += a1 & -a1

        def ft_query(a1):
            a1 += 1
            v2 = 0
            while a1 > 0:
                v2 += v11[a1]
                a1 -= a1 & -a1
            return v2
        v12 = []
        for v13 in a3:
            if v13[0] == 1:
                v2, v14, v15, v16 = v13
                v17 = v14 - 1
                v18 = v15 - 1
                if v6[v17] > v6[v18]:
                    v17, v18 = (v18, v17)
                v19 = v16 - v9[v18]
                ft_update(v6[v18], v19)
                ft_update(v7[v18], -v19)
                v9[v18] = v16
            else:
                v2, v20 = v13
                v20 -= 1
                v12.append(v8[v20] + ft_query(v6[v20]))
        return v12
