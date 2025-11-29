class C1(object):

    def lastMarkedNodes(self, a1):
        """
        """

        def bfs(a1):
            v1 = -1
            v2 = [-1] * len(adj)
            v2[a1] = 0
            v3 = [a1]
            while v3:
                v1 = v3[0]
                v4 = []
                for v5 in v3:
                    for v6 in adj[v5]:
                        if v2[v6] != -1:
                            continue
                        v2[v6] = v2[v5] + 1
                        v4.append(v6)
                v3 = v4
            return (v2, v1)
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v2, v3 = bfs(0)
        v5, v4 = bfs(v3)
        v6, v2 = bfs(v4)
        return [v3 if v5[w] > v6[w] else v4 for v7 in range(len(v1))]
