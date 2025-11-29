class C1(object):

    def minScore(self, a1, a2):
        """
        """

        def bfs():
            v1 = [False] * len(adj)
            v2 = [0]
            v1[0] = True
            while v2:
                v3 = []
                for v4 in v2:
                    for v5, v6 in adj[v4]:
                        if v1[v5]:
                            continue
                        v1[v5] = True
                        v3.append(v5)
                v2 = v3
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3 - 1].append((v4 - 1, v5))
            v1[v4 - 1].append((v3 - 1, v5))
        v6 = bfs()
        return min((v5 for v3, v2, v5 in a2 if v6[v3 - 1]))
