class C1(object):

    def countPairsOfConnectableServers(self, a1, a2):
        """
        """

        def bfs(a1, a2, a3):
            v1 = 0
            v2 = [(a1, a2, a3)]
            while v2:
                v3 = []
                for a1, a2, a3 in v2:
                    if a3 % a2 == 0:
                        v1 += 1
                    for v7, v8 in adj[a1]:
                        if v7 == a2:
                            continue
                        v3.append((v7, a1, a3 + v8))
                v2 = v3
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [0] * (len(a1) + 1)
        for v3 in range(len(v6)):
            v7 = 0
            for v4, v5 in v1[v3]:
                v8 = bfs(v4, v3, v5)
                v6[v3] += v7 * v8
                v7 += v8
        return v6
