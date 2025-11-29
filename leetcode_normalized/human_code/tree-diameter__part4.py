class C1(object):

    def treeDiameter(self, a1):
        """
        """

        def bfs(a1):
            v1 = v2 = -1
            v3 = [False] * len(adj)
            v3[a1] = True
            v4 = [a1]
            while v4:
                v1, v2 = (v1 + 1, v4[0])
                v5 = []
                for v6 in v4:
                    for v7 in adj[v6]:
                        if v3[v7]:
                            continue
                        v3[v7] = True
                        v5.append(v7)
                v4 = v5
            return (v1, v2)
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v2, v5 = bfs(0)
        v6, v2 = bfs(v5)
        return v6
