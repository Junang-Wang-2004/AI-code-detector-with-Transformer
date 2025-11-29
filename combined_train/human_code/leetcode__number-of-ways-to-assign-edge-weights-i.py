class C1(object):

    def assignEdgeWeights(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def bfs():
            v1 = [False] * len(adj)
            v1[0] = True
            v2 = -1
            v3 = [0]
            while v3:
                v4 = []
                for v5 in v3:
                    for v6 in adj[v5]:
                        if v1[v6]:
                            continue
                        v1[v6] = True
                        v4.append(v6)
                v3 = v4
                v2 += 1
            return v2
        v2 = [[] for v3 in range(len(a1) + 1)]
        for v4, v5 in a1:
            v2[v4 - 1].append(v5 - 1)
            v2[v5 - 1].append(v4 - 1)
        return pow(2, bfs() - 1, v1)
