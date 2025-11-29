class C1(object):

    def criticalConnections(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4, a5, a6, a7):
            if a6[a3]:
                return
            a6[a3] = True
            v1 = a5[a3] = a4[0]
            a4[0] += 1
            for v2 in a1[a3]:
                if v2 == a2:
                    continue
                dfs(a1, a3, v2, a4, a5, a6, a7)
                a5[a3] = min(a5[a3], a5[v2])
                if a5[v2] > v1:
                    a7.append([a3, v2])
        v1 = [[] for v2 in range(a1)]
        v3, v4, v5 = ([0], [0] * a1, [False] * a1)
        v6 = []
        for v7, v8 in a2:
            v1[v7].append(v8)
            v1[v8].append(v7)
        dfs(v1, -1, 0, v3, v4, v5, v6)
        return v6
