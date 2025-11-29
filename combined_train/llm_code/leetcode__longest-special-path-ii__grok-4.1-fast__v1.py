class C1:

    def longestSpecialPath(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a1:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = {}
        v8 = [0]
        v9 = [float('inf'), float('inf')]

        def dfs(a1, a2, a3, a4, a5):
            v1 = a2[a1] - 1
            v2 = v7.get(v1, -1)
            v7[v1] = a3
            v3, v4 = (a4, a5)
            if v3 < v4:
                v3, v4 = (v4, v3)
            v5 = v2
            if v5 > v3:
                v6, v7 = (v5, v3)
            elif v5 > v4:
                v6, v7 = (v3, v5)
            else:
                v6, v7 = (v3, v4)
            v8 = v7
            v9 = v8[a3] - v8[v8 + 1]
            v10 = a3 - v8
            v11 = -v9
            if v11 < v9[0] or (v11 == v9[0] and v10 < v9[1]):
                v9[0] = v11
                v9[1] = v10
            for v12, v13 in v2[a1]:
                if v12 == a2:
                    continue
                v8.append(v8[-1] + v13)
                dfs(v12, a1, a3 + 1, v6, v7)
                v8.pop()
            v7[v1] = v2
        dfs(0, -1, 0, -1, -1)
        return [-v9[0], v9[1]]
