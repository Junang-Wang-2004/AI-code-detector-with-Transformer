class C1(object):

    def constructGridLayout(self, a1, a2):
        """
        """

        def bfs(a1):
            v1 = [0] * a1
            v1[a1] = 1
            v2 = [a1]
            while v2:
                v3 = []
                for a1 in v2:
                    for v5 in adj[a1]:
                        if v1[v5]:
                            continue
                        v1[v5] = v1[a1] + 1
                        v3.append(v5)
                v2 = v3
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = min((len(x) for v6 in v1))
        v7 = [v3 for v3 in range(a1) if len(v1[v3]) == v5]
        v8 = bfs(v7[0])
        v7.sort(key=lambda x: v8[v6])
        v9 = bfs(v7[1])
        v10 = v8[v7[1]]
        v11 = a1 // v10
        v12 = [[0] * v10 for v2 in range(v11)]
        for v3 in range(a1):
            v13 = (v8[v3] + v9[v3] - (1 + v10)) // 2
            v14 = v8[v3] - 1 - v13
            v12[v13][v14] = v3
        return v12
