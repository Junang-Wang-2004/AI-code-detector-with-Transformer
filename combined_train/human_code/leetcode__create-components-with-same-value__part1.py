class C1(object):

    def componentValue(self, a1, a2):
        """
        """

        def bfs(a1):
            v1 = a1[:]
            v2 = [len(adj[u]) for v3 in range(len(adj))]
            v4 = [v3 for v3 in range(len(adj)) if v2[v3] == 1]
            while v4:
                v5 = []
                for v3 in v4:
                    if v1[v3] > a1:
                        return False
                    if v1[v3] == a1:
                        v1[v3] = 0
                    for v6 in adj[v3]:
                        v1[v6] += v1[v3]
                        v2[v6] -= 1
                        if v2[v6] == 1:
                            v5.append(v6)
                v4 = v5
            return True
        v1 = 0
        v2 = [[] for v3 in range(len(a1))]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = sum(a1)
        for v7 in reversed(range(2, len(a1) + 1)):
            if v6 % v7 == 0 and bfs(v6 // v7):
                return v7 - 1
        return 0
