class C1(object):

    def processQueries(self, a1, a2, a3):
        """
        """

        def iter_dfs(a1):
            v1 = [a1]
            while v1:
                v2 = v1.pop()
                if lookup[v2] != -1:
                    continue
                lookup[v2] = a1
                for v3 in reversed(adj[v2]):
                    v1.append(v3)
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)
        v5 = [-1] * a1
        for v6 in range(a1):
            iter_dfs(v6)
        v7 = [[] for v2 in range(a1)]
        for v6 in reversed(range(a1)):
            v7[v5[v6]].append(v6)
        v8 = []
        v9 = [True] * a1
        for v10, v11 in a3:
            v11 -= 1
            if v10 == 1:
                if v9[v11]:
                    v8.append(v11 + 1)
                    continue
                while v7[v5[v11]] and (not v9[v7[v5[v11]][-1]]):
                    v7[v5[v11]].pop()
                v8.append(v7[v5[v11]][-1] + 1 if v7[v5[v11]] else -1)
            else:
                v9[v11] = False
        return v8
