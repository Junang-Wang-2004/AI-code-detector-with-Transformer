class C1(object):

    def countCompleteComponents(self, a1, a2):
        """
        """

        def bfs(a1):
            if lookup[a1]:
                return False
            v1 = v2 = 0
            lookup[a1] = True
            v3 = [a1]
            while v3:
                v4 = []
                v1 += len(v3)
                for a1 in v3:
                    v2 += len(adj[a1])
                    for v6 in adj[a1]:
                        if lookup[v6]:
                            continue
                        lookup[v6] = True
                        v4.append(v6)
                v3 = v4
            return v1 * (v1 - 1) == v2
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [False] * a1
        return sum((bfs(v3) for v3 in range(a1) if not v5[v3]))
