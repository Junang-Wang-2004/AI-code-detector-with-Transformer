class C1(object):

    def maxKDivisibleComponents(self, a1, a2, a3, a4):
        """
        """

        def bfs():
            v1 = 0
            v2 = [x % a4 for v3 in a3]
            v4 = [len(adj[u]) for v5 in range(len(adj))]
            v6 = [v5 for v5 in range(a1) if v4[v5] == 1]
            while v6:
                v7 = []
                for v5 in v6:
                    if not v2[v5]:
                        v1 += 1
                    for v8 in adj[v5]:
                        v2[v8] = (v2[v8] + v2[v5]) % a4
                        v4[v8] -= 1
                        if v4[v8] == 1:
                            v7.append(v8)
                v6 = v7
            return max(v1, 1)
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return bfs()
